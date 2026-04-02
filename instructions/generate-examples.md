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

## Step 5: For Each Missing Recipe, Open One PR

Work through every missing recipe path one at a time. For each recipe:

### 5a — Create a dedicated branch

```bash
PRODUCT=$(echo "{recipe_path}" | cut -d/ -f1)   # e.g. speech-to-text
VERSION=$(echo "{recipe_path}" | cut -d/ -f2)   # e.g. v1
SLUG=$(echo "{recipe_path}"    | cut -d/ -f3)   # e.g. paragraphs

BRANCH="recipe/{language}/${PRODUCT}/${VERSION}/${SLUG}"
git checkout main
git checkout -b "$BRANCH"

CURRENT=$(git branch --show-current)
[ "$CURRENT" = "main" ] && echo "ERROR: Still on main. Aborting." && exit 1
```

### 5b — Check the directory does not already exist

```bash
if [ -d "recipes/{language}/${PRODUCT}/${VERSION}/${SLUG}" ]; then
  echo "[SKIP] recipes/{language}/${PRODUCT}/${VERSION}/${SLUG} already exists."
  git checkout main
  continue
fi
```

### 5c — Generate the three recipe files

Create `recipes/{language}/${PRODUCT}/${VERSION}/${SLUG}/` and write:

1. **`example.{ext}`** — the runnable example (< 50 lines, feature-focused, commented)
2. **`example_test.{ext}`** — runs the example as a subprocess, asserts exit 0 + output
3. **`README.md`** — feature explanation, params table, sample output, run instructions

Follow the language templates, commenting standard, and API key rules in the sections below.

### 5d — Commit and push

```bash
git add "recipes/{language}/${PRODUCT}/${VERSION}/${SLUG}/"
git commit -m "feat({language}): ${PRODUCT} ${VERSION} — ${SLUG}"
git push origin "$BRANCH"
```

### 5e — Open PR (no auto-merge — waits for human)

```bash
PR_URL=$(gh pr create \
  --title "feat({language}): ${PRODUCT} ${VERSION} — ${SLUG}" \
  --label "type:samples" \
  --label "language:{language}" \
  --body "Adds the **${SLUG}** recipe for ${PRODUCT} ${VERSION} (${language}).

Closes part of #{issue_number}")
```

CI will run automatically. A human will review and merge.

### 5f — Return to main for the next recipe

```bash
git checkout main
```

Repeat steps 5a–5f for every missing recipe path.

---

## Step 6: Close the Queue Issue

After all PRs are opened:

```bash
gh issue close {issue_number} \
  --comment "Opened {N} PRs — one per recipe. Waiting for human review and merge."
```

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
- ONLY write files inside `recipes/{language}/{product}/{version}/{slug}/` — the three files for this one recipe
- NEVER touch README.md, COVERAGE.md, instructions/, .deepgram/, .github/, or any file outside the recipe directory
- NEVER overwrite an existing `example.*` file — skip and log a warning
- NEVER commit to the `main` branch
- Always work on the feature branch created in Step 5a

### When Unsure About SDK API
- Read the SDK README again (Step 4)
- Look at the SDK's examples directory for the specific feature
- Check the SDK's CHANGELOG or release notes for the version in the issue
- If the API is still unclear after checking the SDK, skip the recipe and add a comment in the PR noting which recipe needs manual review

### CLI recipes must use `dg` — NOT curl

The CLI language uses the official Deepgram CLI (`pip install deepctl`).
Commands: `dg` (or `deepctl` / `deepgram` — all aliases).

**STT (pre-recorded):**
```bash
dg listen https://dpgr.am/spacewalk.wav --model nova-3 --smart-format
dg listen audio.wav --diarize
dg listen audio.wav --paragraphs
dg listen audio.wav --summarize --topics --sentiment
dg listen audio.wav -o json | jq '.results.channels[0].alternatives[0].transcript'
```

**STT (streaming from file — no microphone, so CI can run it):**
```bash
ffmpeg -i audio.wav -f s16le -ar 16000 -ac 1 -loglevel quiet - \
  | dg listen --encoding linear16 --model nova-3 --smart-format
```

**TTS:**
```bash
dg speak "Hello from Deepgram" -o output.mp3
dg speak "Hello" -m aura-2-thalia-en -o output.mp3
```

**Audio intelligence (--summarize / --topics / --sentiment / --intents on dg listen):**
```bash
dg listen audio.wav --summarize --topics --intents --sentiment --model nova-3
```

**Standard test pattern (`example_test.sh`):**
```bash
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# set +e guards against bash 5.x exiting silently on non-zero command substitution
set +e
output=$(bash "$SCRIPT_DIR/example.sh" 2>&1)
status=$?
set -e

if [ $status -ne 0 ]; then
  echo "FAIL: example.sh exited with status $status"
  echo "$output"
  exit 1
fi

if [ -z "$output" ]; then
  echo "FAIL: example.sh produced no output"
  exit 1
fi

echo "PASS"
echo "$output" | head -3
```

NEVER use curl in CLI recipes. If you find yourself writing a curl command,
stop and find the equivalent `dg` subcommand instead.
