# Sentiment Analysis (Audio Intelligence v1)

Segment-level positive/negative/neutral sentiment scoring for audio content.

## What it does

Sends audio to the `/v1/listen` endpoint with `sentiment=true` to classify each speech segment's emotional tone. Returns both an overall average sentiment and per-segment sentiment labels with confidence scores.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Required model for sentiment analysis |
| `sentiment` | `true` | Enables per-segment sentiment scoring |

## Example output

```
Overall sentiment: positive (confidence: 0.78)
  positive: Yeah, as much as it's worth celebrating the 50th anniversary...
  neutral: And there were other things happening at the same time...
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
