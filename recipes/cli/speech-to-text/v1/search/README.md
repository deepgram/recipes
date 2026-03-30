# Search (Speech-to-Text v1)

Finds specific words or phrases in audio with timing and confidence scores.

## What it does

Enables the `search` parameter which looks for specific terms in the audio. Each match includes the start/end time and a confidence score, making it easy to find key moments in long recordings without reading the entire transcript.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Highest-accuracy transcription model |
| `search` | `spacewalk` | First search term |
| `search` | `moon` | Second search term |

## Example output

```
Found "spacewalk" at 1.20s-1.80s (confidence: 0.95)
Found "moon" at 5.30s-5.60s (confidence: 0.91)
```

## Prerequisites

- `curl` and `python3` installed
- Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
