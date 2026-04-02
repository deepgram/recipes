# Sentiment Analysis (STT v1)

Analyses sentiment (positive, negative, or neutral) per segment of the transcript.

## What it does

The `--sentiment` flag enables segment-level sentiment analysis. Deepgram classifies each segment of the transcript as positive, negative, or neutral with a confidence score. This is useful for analysing customer calls, feedback recordings, and meeting sentiment.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `nova-3` | Deepgram transcription model |
| `--sentiment` | flag | Enables sentiment analysis |

## Example output

```
Yeah, as much as, it's funny when I think of anything that's related to outer space...

Sentiment: positive (0.85), neutral (0.72)
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
