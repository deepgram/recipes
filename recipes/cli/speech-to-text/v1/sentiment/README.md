# Sentiment Analysis (Speech-to-Text v1)

Analyzes the emotional tone of speech segments as positive, negative, or neutral.

## What it does

Enables the `sentiment` parameter which runs AI-powered sentiment analysis on each segment of the transcript. Each segment gets a sentiment label (positive, negative, or neutral) with confidence scores. This is an Audio Intelligence feature.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Required model for sentiment analysis |
| `sentiment` | `true` | Enables per-segment sentiment scoring |

## Example output

```
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
