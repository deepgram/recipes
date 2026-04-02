# Generate Audio to File (TTS v1)

Converts text to speech and saves the result as an audio file.

## What it does

The `dg speak` command sends text to Deepgram's TTS API and saves the generated audio to a file. The `-o` flag specifies the output file path. This example uses the `aura-2-thalia-en` voice model to generate a natural-sounding English audio file.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `-m` | `aura-2-thalia-en` | Voice model to use |
| `-o` | file path | Output audio file path |

## Example output

```
Audio saved to /tmp/deepgram_output.mp3 (15432 bytes)
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- `DEEPGRAM_API_KEY` environment variable set

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
