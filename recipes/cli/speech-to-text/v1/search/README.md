# Search (STT v1)

Finds specific words or phrases in audio with confidence scores.

## What it does

The `search` parameter tells Deepgram to look for specific terms in the audio and return each occurrence with a timestamp and confidence score. Multiple search terms can be specified. This is useful for finding key moments in recordings without reading the full transcript.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Deepgram transcription model |
| `search` | `space`, `shuttle` | Words or phrases to find |

## Example output

```
space found at 2.34s (confidence: 0.98)
shuttle found at 8.12s (confidence: 0.95)
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
