# Transcribe Audio from URL (STT v2)

Uses the v2 API for high-accuracy English audio transcription.

## What it does

The v2 API endpoint uses the `flux-general-en` model, designed specifically for English with higher accuracy. When you specify a `flux-*` model, the CLI automatically uses the `/v2/listen` endpoint instead of `/v1/listen`.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `source` | URL | Remote audio file URL |
| `--model` | `flux-general-en` | High-accuracy English model (v2) |

## Example output

```
Yeah, as much as it's funny when I think of anything that's related to outer space...
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
