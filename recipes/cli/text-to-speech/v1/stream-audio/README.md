# Stream Audio Response (TTS v1)

Streams TTS audio as it generates via REST streaming.

## What it does

When no `-o` flag is given and stdout is not a terminal, `dg speak` streams the audio bytes to stdout. This allows piping audio directly to a player (`ffplay`), encoder, or any processing pipeline without saving to disk first.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `-m` | `aura-2-thalia-en` | Voice model to use |
| (no `-o`) | | Streams audio to stdout |

## Example output

```
Streamed 15432 bytes of audio to stdout
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
