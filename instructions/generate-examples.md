# Instruction: Generate Recipe Examples

You are an autonomous agent generating runnable Deepgram SDK code samples. Your job is to read
a `queue:generate` GitHub Issue, determine which recipe files are missing for a given language,
and generate high-quality, runnable examples for each one.

Work methodically. Read SDK documentation before writing code. Never guess at an API — verify
it. Never hardcode secrets. Never overwrite existing files.

---

## Step 1: Find the Triggering Queue Issue

List open `queue:generate` issues and take the oldest one:

```bash
gh issue list \
  --label "type:queue" \
  --label "action:generate" \
  --state open \
  --json number,title,body,labels \
  --limit 1 \
  --jq '.[0]'
```

If no issue is returned, output:
```
No queue:generate issues found. Nothing to do.
```
And stop.

From the issue body, extract the following values from the HTML comment block:
- `language` — e.g., `python`
- `repo` — e.g., `deepgram/deepgram-python-sdk`
- `sdk-version` — e.g., `v4.1.0`
- `reason` — e.g., `coverage-gap`

Also extract the list of missing recipe paths from the "## Missing Recipe Paths" section.

Store the issue number for later use.

---

## Step 2: Load Configuration Files

```bash
cat .deepgram/sdks.json
cat .deepgram/features.json
```

Find the SDK entry in sdks.json matching the `language` extracted from the issue. Confirm the
`repo` and `slug` fields match.

From features.json, get the full list of expected recipes for this language so you have
complete context about what the system expects.

---

## Step 3: Check Actual Existing Coverage

```bash
find "recipes/{language}/" -name "example.*" ! -name "*_test*" ! -name "*.mod" 2>/dev/null | \
  sed "s|recipes/{language}/||" | sed "s|/example.*||" | sort
```

Replace `{language}` with the actual language slug.

This is the authoritative list of what is already generated. Use this (not the issue body alone)
to determine what needs to be created. The issue body may be stale — trust the filesystem.

A recipe needs generation if:
1. It appears in features.json for this language, AND
2. The `recipes/{language}/{path}/` directory does NOT already contain an `example.*` file

---

## Step 4: Fetch SDK Context from GitHub

Before writing any code, understand the SDK's current API:

```bash
# Get the SDK README (first 300 lines is usually enough for API overview)
gh api "repos/{repo}/readme" --jq '.content' | base64 -d | head -300

# Check for an examples directory in the SDK
gh api "repos/{repo}/contents/examples" 2>/dev/null | jq -r '.[].name'

# Get the latest release notes (may mention new features or breaking changes)
gh api "repos/{repo}/releases/latest" --jq '.name + "\n\n" + .body' | head -100
```

If the SDK has an examples directory, fetch a relevant example file to understand the actual
import paths and client initialization pattern:

```bash
# Example: fetch the content of a specific example file
gh api "repos/{repo}/contents/examples/{filename}" --jq '.content' | base64 -d
```

Use this to validate that your generated code uses the correct import paths, client
constructor, and method names for the SDK version specified in the issue.

---

## Step 4b: Search Kapa for Current Documentation

Kapa indexes Deepgram's live documentation. Search it for each recipe you are about
to generate — the results reflect the current API surface more reliably than SDK READMEs,
and the **most recently updated sources are the most relevant**.

```bash
kapa_search() {
  local query="$1"
  curl -s -L "https://api.kapa.ai/query/v1/projects/${KAPA_PROJECT_ID}/retrieval/" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -H "X-API-KEY: ${KAPA_API_KEY}" \
    -d "{\"query\": \"$(echo "$query" | sed 's/"/\\\\"/g')\", \"top_k\": 15, \"redact_query\": false}" \
    | jq -r '
        .sources
        | sort_by(.updated_at)
        | reverse
        | .[:5][]
        | "--- " + .title + " ---\n" + "URL: " + .url + "\n" + .content
      ' 2>/dev/null
}
```

Run one search per recipe you plan to generate. Tailor the query to the feature:

```bash
# For each recipe, search with a targeted query:

# Operations (transcribe, generate audio, etc.)
kapa_search "deepgram {language} SDK {operation} example code {product}"

# Feature flags (paragraphs, diarize, smart_format, etc.)
kapa_search "deepgram {feature} parameter {product} API {language}"

# Streaming recipes
kapa_search "deepgram {language} SDK live streaming websocket {product}"
```

**How to use the results:**

- **Response structure** — if the docs show a different response path than you expected,
  use what the docs say. Copy exact field names from examples in the results.
- **Parameter names** — prefer the exact spelling from Kapa results over any guesses.
  SDK parameter names can differ subtly between languages (e.g., `smart_format` vs `smartFormat`).
- **Code snippets** — treat Kapa-returned code as the authoritative pattern for that language.
  Adapt it to fit the recipe's < 50-line constraint, then add the commenting standard.
- **Conflicting results** — if Kapa and the SDK README disagree, prefer Kapa (it reflects
  the deployed API) and note the discrepancy in the recipe's README.

If `KAPA_API_KEY` or `KAPA_PROJECT_ID` is unset, skip this step and rely on the SDK README
alone — do not abort.

---

## Step 5: Create a Feature Branch

```bash
BRANCH="generate/{language}-$(date +%Y%m%d-%H%M)"
git checkout -b "$BRANCH"

# Verify you are NOT on main
CURRENT=$(git branch --show-current)
if [ "$CURRENT" = "main" ]; then
  echo "ERROR: Still on main branch. Aborting."
  exit 1
fi

echo "Working on branch: $BRANCH"
```

All file creation and commits happen on this branch. Never touch main.

---

## Step 6: Generate Recipe Files

For each missing recipe path (e.g., `speech-to-text/v1/transcribe-url-nova3`), generate
three files inside `recipes/{language}/{recipe-path}/`.

### Before creating any file:

Check if the directory already exists and has content:

```bash
ls "recipes/{language}/{recipe-path}/" 2>/dev/null
```

If `example.*` already exists in this directory, skip it with a log message:
```
[SKIP] recipes/{language}/{recipe-path}/example.* already exists.
```

### Understand the recipe path structure:

A path like `speech-to-text/v1/transcribe-url-nova3` means:
- Product: `speech-to-text`
- API version: `v1`
- Recipe slug: `transcribe-url-nova3`

The slug describes the feature. Use it to understand what the example should demonstrate.

Common slug patterns:
- `transcribe-url-{model}` — transcribe a URL using a specific model
- `transcribe-file-{model}` — transcribe a local file
- `smart-format` — smart formatting feature
- `diarize` — speaker diarization
- `summarize` — audio intelligence summarization
- `topics` — topic detection
- `sentiment` — sentiment analysis
- `intents` — intent detection
- `stream-microphone` — live streaming from microphone
- `text-to-speech-{model}` — TTS with specific model
- `voice-agent-basic` — basic voice agent setup

### Files to create for each recipe:

#### File 1: `example.{ext}` — The runnable recipe

Requirements:
- MUST be under 50 lines of code
- MUST read API key from environment, NEVER hardcode
- MUST demonstrate EXACTLY the feature described by the recipe slug
- MUST print meaningful output (transcript text, audio size, timing, etc.) — not just "done"
- MUST use `https://dpgr.am/spacewalk.wav` as the demo audio URL for audio examples
- MUST use the correct SDK import paths (verified from the SDK README in Step 4)
- Use async where appropriate (streaming, voice agents, TTS with streaming output)
- Keep it simple and readable — this is a teaching example

**Commenting standard — this is critical:**

Comments serve both human readers and future agents updating the recipe. Include ALL of:

1. **Module docstring** — name the recipe, state what feature it demonstrates, and describe
   how the output differs from the baseline (e.g., "Without X: flat string. With X: blocks.").
   If there are related recipes in sibling directories, name them.

2. **Feature-enabling parameter** — mark the one parameter that is the point of this recipe
   with an inline comment: `param=True,  # <-- THIS is the feature this recipe demonstrates`

3. **Response path comment** — explain exactly where the feature's output lives in the
   response object and what fields are available, e.g.:
   ```
   # alt.paragraphs.paragraphs  — list of paragraph objects
   #   para.sentences           — list of sentence objects
   #     sentence.text          — the sentence string
   #     sentence.start/end     — timing in seconds
   ```

4. **Edge case comments** — note conditions where the feature may not return data
   (e.g., "paragraphs can be absent if audio is too short").

5. **Optional parameter hints** — in a comment near the API call, list 2-3 other parameters
   a user might want to try for this recipe.

Agents updating this recipe later must be able to understand what is boilerplate vs
what is specific to this recipe's feature, purely from reading the comments.

**Python (`example.py`) — SDK v6+ API:**

`DeepgramClient()` with no args reads `DEEPGRAM_API_KEY` from the environment automatically.
Options are passed as keyword arguments directly to the method — no `PrerecordedOptions` class.

```python
from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"

client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

response = client.listen.v1.media.transcribe_url(
    url=AUDIO_URL,
    model="nova-3",
    smart_format=True,
    # feature-specific parameters go here (diarize=True, paragraphs=True, etc.)
)

if response.results and response.results.channels:
    print(response.results.channels[0].alternatives[0].transcript)
```

For TTS examples, use the speak API (generate returns an Iterator[bytes]):
```python
import os
from deepgram import DeepgramClient

client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

audio_chunks = client.speak.v1.audio.generate(
    text="Hello from Deepgram!",
    model="aura-2-thalia-en",
)

with open("output.mp3", "wb") as f:
    for chunk in audio_chunks:
        f.write(chunk)

print(f"Audio saved: {os.path.getsize('output.mp3')} bytes")
```

For streaming examples, use asyncio:
```python
import asyncio
from deepgram import DeepgramClient, LiveTranscriptionEvents

async def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment
    connection = client.listen.asyncwebsocket.v("1")
    # ... streaming setup ...

asyncio.run(main())
```

**JavaScript (`example.js`):**
```javascript
import { createClient } from "@deepgram/sdk";

const client = createClient(process.env.DEEPGRAM_API_KEY);

async function main() {
  const { result, error } = await client.listen.prerecorded.transcribeUrl(
    { url: "https://dpgr.am/spacewalk.wav" },
    {
      model: "nova-3",
      // feature-specific options
    }
  );
  if (error) throw error;
  console.log(result.results.channels[0].alternatives[0].transcript);
}

main().catch(console.error);
```

For TTS:
```javascript
import { createClient } from "@deepgram/sdk";
import { writeFile } from "node:fs/promises";

const client = createClient(process.env.DEEPGRAM_API_KEY);

async function main() {
  const response = await client.speak.request(
    { text: "Hello from Deepgram!" },
    { model: "aura-2-thalia-en" }
  );
  const stream = await response.getStream();
  const buffer = await getAudioBuffer(stream);
  await writeFile("output.mp3", buffer);
  console.log(`Audio saved: ${buffer.length} bytes`);
}

async function getAudioBuffer(response) {
  const reader = response.getReader();
  const chunks = [];
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    chunks.push(value);
  }
  const dataArray = chunks.reduce((acc, chunk) => {
    const tmp = new Uint8Array(acc.byteLength + chunk.byteLength);
    tmp.set(new Uint8Array(acc), 0);
    tmp.set(new Uint8Array(chunk), acc.byteLength);
    return tmp.buffer;
  }, new ArrayBuffer(0));
  return Buffer.from(dataArray);
}

main().catch(console.error);
```

**Go (`example.go`):**
```go
package main

import (
	"context"
	"fmt"
	"os"

	api "github.com/deepgram/deepgram-go-sdk/v3/pkg/api/listen/v1/rest"
	interfaces "github.com/deepgram/deepgram-go-sdk/v3/pkg/api/listen/v1/rest/interfaces"
	client "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/listen"
)

func main() {
	ctx := context.Background()
	c, err := client.NewRESTWithDefaults()
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	dg := api.New(c)

	options := &interfaces.PreRecordedTranscriptionOptions{
		Model:       "nova-3",
		SmartFormat: true,
		// feature-specific options
	}

	res, err := dg.FromURL(ctx, "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	fmt.Println((*res.Results.Channels)[0].Alternatives[0].Transcript)
}
```

For Go TTS, use the speak API package. For streaming, use the websocket client.

**.NET (`Program.cs`):**
```csharp
using Deepgram;
using Deepgram.Models.Listen.v1.REST;

var client = new DeepgramClient(Environment.GetEnvironmentVariable("DEEPGRAM_API_KEY")!);

var response = await client.Listen.Rest.v1.TranscribeUrlAsync(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema
    {
        Model = "nova-3",
        // feature-specific options
    }
);

Console.WriteLine(response.Results?.Channels?[0]?.Alternatives?[0]?.Transcript);
```

**Java (`Example.java`):**
```java
import com.deepgram.sdk.Deepgram;
import com.deepgram.sdk.DeepgramClient;
import com.deepgram.sdk.audio.listen.ListenRestClient;
import com.deepgram.sdk.audio.listen.prerecorded.PrerecordedOptions;
import com.deepgram.sdk.audio.listen.prerecorded.SyncPrerecordedResponse;

public class Example {
    public static void main(String[] args) throws Exception {
        DeepgramClient client = Deepgram.create(System.getenv("DEEPGRAM_API_KEY"));
        ListenRestClient listen = client.listen().rest();

        PrerecordedOptions options = PrerecordedOptions.builder()
            .model("nova-3")
            // feature-specific options
            .build();

        SyncPrerecordedResponse response = listen.transcribeUrl(
            "https://dpgr.am/spacewalk.wav",
            options
        );

        System.out.println(
            response.getResults()
                    .getChannels().get(0)
                    .getAlternatives().get(0)
                    .getTranscript()
        );
    }
}
```

**Rust (`example.rs` or `main.rs`):**
```rust
use deepgram::{
    audio::listen::rest::options::ListenOptions,
    Deepgram,
};
use std::env;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = env::var("DEEPGRAM_API_KEY")?;
    let dg = Deepgram::new(api_key)?;

    let options = ListenOptions::builder()
        .model("nova-3")
        // feature-specific options
        .build();

    let response = dg
        .audio()
        .listen()
        .rest()
        .transcribe_url("https://dpgr.am/spacewalk.wav", &options)
        .await?;

    let transcript = &response
        .results
        .channels[0]
        .alternatives[0]
        .transcript;

    println!("{}", transcript);
    Ok(())
}
```

**CLI (`example.sh`):**
```bash
#!/usr/bin/env bash
set -euo pipefail

# Transcribe audio from URL
deepgram transcribe \
  --model nova-3 \
  --url "https://dpgr.am/spacewalk.wav"
```

**IMPORTANT:** Always look at the actual SDK README (fetched in Step 4) to verify:
- The correct package/module import paths for the installed SDK version
- The exact method names (they may differ from these templates)
- Any breaking changes in the version specified in the queue issue

If the templates above conflict with the SDK README, ALWAYS prefer the SDK README.

---

#### File 2: `example_test.{ext}` — The test

The test must:
- Run the example as a subprocess (or equivalent)
- Assert that the exit code is 0 (success)
- Assert that stdout is non-empty
- Not mock the Deepgram API — it runs for real using `DEEPGRAM_API_KEY` from the environment

**Python (`example_test.py`):**
```python
import os
import subprocess
from pathlib import Path


def test_example_runs():
    example = Path(__file__).parent / "example.py"
    result = subprocess.run(
        ["python", str(example)],
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert result.returncode == 0, (
        f"Example failed\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"
    )
    assert result.stdout.strip(), "Example produced no output"
```

**JavaScript (`example.test.js`):**
```javascript
import { describe, it } from "node:test";
import { ok } from "node:assert";
import { execSync } from "node:child_process";
import { dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));

describe("example", () => {
  it("runs without error and produces output", () => {
    const output = execSync("node example.js", {
      cwd: __dirname,
      timeout: 60000,
      env: process.env,
      encoding: "utf8",
    });
    ok(output.trim().length > 0, "Expected non-empty output");
  });
});
```

**Go (`example_test.go`):**
```go
package main

import (
	"os/exec"
	"strings"
	"testing"
)

func TestExampleRuns(t *testing.T) {
	cmd := exec.Command("go", "run", "example.go")
	output, err := cmd.CombinedOutput()
	if err != nil {
		t.Fatalf("Example failed: %v\nOutput: %s", err, string(output))
	}
	if strings.TrimSpace(string(output)) == "" {
		t.Fatal("Example produced no output")
	}
}
```

**.NET (`ExampleTest.cs`):**
```csharp
using System.Diagnostics;
using Xunit;

public class ExampleTest
{
    [Fact]
    public void ExampleRunsAndProducesOutput()
    {
        var psi = new ProcessStartInfo("dotnet", "run --project .")
        {
            WorkingDirectory = Path.GetDirectoryName(
                System.Reflection.Assembly.GetExecutingAssembly().Location)!,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
        };

        using var process = Process.Start(psi)!;
        process.WaitForExit(60_000);

        Assert.Equal(0, process.ExitCode);
        Assert.NotEmpty(process.StandardOutput.ReadToEnd().Trim());
    }
}
```

**Java (`ExampleTest.java`):**
```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.io.*;

class ExampleTest {
    @Test
    void exampleRunsAndProducesOutput() throws Exception {
        ProcessBuilder pb = new ProcessBuilder("java", "-cp", "target/classes", "Example");
        pb.redirectErrorStream(true);
        Process process = pb.start();

        String output = new String(process.getInputStream().readAllBytes());
        int exitCode = process.waitFor();

        assertEquals(0, exitCode, "Example exited with code " + exitCode + "\n" + output);
        assertFalse(output.trim().isEmpty(), "Example produced no output");
    }
}
```

**Rust (in `src/main.rs` or via `#[cfg(test)]` block):**

For Rust, add an integration test by creating `tests/integration_test.rs`:
```rust
use std::process::Command;

#[test]
fn example_runs_and_produces_output() {
    let output = Command::new("cargo")
        .args(["run", "--quiet"])
        .output()
        .expect("Failed to run example");

    assert!(
        output.status.success(),
        "Example failed with: {}",
        String::from_utf8_lossy(&output.stderr)
    );
    assert!(
        !String::from_utf8_lossy(&output.stdout).trim().is_empty(),
        "Example produced no output"
    );
}
```

**CLI (`example_test.sh`):**
```bash
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

output=$(bash "$SCRIPT_DIR/example.sh")

if [ -z "$output" ]; then
  echo "FAIL: example.sh produced no output"
  exit 1
fi

echo "PASS: example.sh ran successfully"
echo "Output: $output"
```

---

#### File 3: `README.md` — Recipe documentation

Use this template exactly:

```markdown
# {Recipe Name} ({Product} {version})

{One-sentence description of what this feature does and why you'd use it.}

## What it does

{2-3 sentences explaining the feature in plain language. What changes in the
output when this feature is enabled? What problem does it solve?}

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `{param}` | `{value}` | {what it controls} |

## Example output

```
{A brief, realistic example of what the output looks like. For transcription,
show a short transcript snippet. For TTS, show file size info. Keep it short.}
```

## Prerequisites

- {Language} {minimum version}+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `{install command}`

## Run

```bash
{the exact command to run the example}
```
```

Fill in all placeholders with accurate values. The Recipe Name should be human-readable
(e.g., "Smart Format" not "smart-format"). The Product should be the full product name
(e.g., "Speech-to-Text").

---

## Step 7: Commit and Push the Generated Files

After generating all files for all missing recipes:

```bash
git add "recipes/{language}/"

git commit -m "feat({language}): add {product} {version} recipes

Recipes added:
{list of recipe paths, one per line prefixed with "- "}

Closes #{issue_number}"

git push origin "$BRANCH"
```

If there are recipes for multiple products, group them in the commit message.

Verify the push succeeded before continuing.

---

## Step 8: Create a Pull Request

```bash
gh pr create \
  --title "feat({language}): add {product} {version} recipes" \
  --label "type:samples" \
  --label "language:{slug}" \
  --body "$(cat <<'PR_BODY'
## Summary

Adds {N} recipe(s) for {language} covering {product} {version}.

### Recipes added

{bullet list of recipe paths}

### How to test

1. Set `DEEPGRAM_API_KEY` in your environment
2. Run the {language} test workflow locally or check the CI run on this PR

Closes #{issue_number}
PR_BODY
)"
```

Capture the PR URL from the output. Then immediately enable auto-merge:

```bash
# Enable auto-merge — the PR will merge automatically once all test checks pass.
# Requires "Allow auto-merge" to be enabled in repository Settings → General.
gh pr merge --auto --squash --subject "feat({language}): add {product} {version} recipes"
```

The PR will stay open until the language-specific test workflow runs and passes.
If tests fail, the PR remains open for investigation — do not force-merge.

---

## Step 9: Close the Queue Issue

```bash
gh issue close {issue_number} \
  --comment "Generated {N} recipe(s) for {language}. See PR {pr_url}."
```

Replace `{issue_number}` with the actual issue number from Step 1.

---

## Important Rules

### API Key Handling
- NEVER hardcode API keys or credentials of any kind
- Python: `os.environ["DEEPGRAM_API_KEY"]` — this raises KeyError if not set (intentional)
- JavaScript: `process.env.DEEPGRAM_API_KEY`
- Go: `os.Getenv("DEEPGRAM_API_KEY")`
- .NET: `Environment.GetEnvironmentVariable("DEEPGRAM_API_KEY")!`
- Java: `System.getenv("DEEPGRAM_API_KEY")`
- Rust: `env::var("DEEPGRAM_API_KEY")?`
- CLI: `$DEEPGRAM_API_KEY` (assumes it is exported in shell environment)

### Audio / Demo Content
- ALWAYS use `https://dpgr.am/spacewalk.wav` as the demo audio URL
- NEVER commit audio files (`.wav`, `.mp3`, `.ogg`, etc.)
- NEVER commit binary output files
- For TTS examples that save files, use a clearly named output file (`output.mp3`) but do NOT commit it — add to .gitignore if needed

### Code Quality
- Keep examples under 50 lines
- Each example MUST print something meaningful to stdout (not just "done" or nothing)
- Comments should explain the feature being demonstrated, not restate what the code does
- Use the model `nova-3` for STT examples unless the recipe specifically calls for a different model
- Use `aura-2-thalia-en` for TTS examples unless the recipe specifies otherwise

### File Safety
- NEVER overwrite an existing `example.*` file — skip and log a warning
- NEVER modify files outside `recipes/{language}/`
- NEVER commit to the `main` branch
- Always work on the feature branch created in Step 5

### When Unsure About SDK API
- Read the SDK README again (Step 4)
- Look at the SDK's examples directory for the specific feature
- Check the SDK's CHANGELOG or release notes for the version in the issue
- If the API is still unclear after checking the SDK, skip the recipe and add a comment in the PR noting which recipe needs manual review
