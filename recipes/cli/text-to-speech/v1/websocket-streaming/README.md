# WebSocket Streaming TTS (TTS v1)

Low-latency text-to-speech using streaming input.

## What it does

Demonstrates piping text to `dg speak` via stdin for streaming input. The CLI reads text from stdin when no text argument is provided, enabling pipeline-based TTS workflows. The generated audio is saved to a file.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `-m` | `aura-2-thalia-en` | Voice model to use |
| `-o` | file path | Output audio file path |
| stdin | text | Text piped from another command |

## Example output

```
Audio saved to /tmp/deepgram_ws_output.mp3 (18240 bytes)
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
