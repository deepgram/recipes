# Topic Detection (Speech-to-Text v1)

Identifies key topics discussed in the audio with confidence scores.

## What it does

Enables the `topics` parameter which runs AI-powered topic detection on the transcript. The response includes topic segments, each containing one or more detected topics with confidence scores. This is an Audio Intelligence feature.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Required model for topic detection |
| `topics` | `true` | Enables topic identification |

## Example output

```
Topic: space exploration (confidence: 0.95)
Topic: astronaut activities (confidence: 0.87)
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
