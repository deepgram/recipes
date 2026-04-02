# Sentiment Analysis (Text Analysis v1)

Analyzes sentiment on plain text input without requiring audio.

## What it does

The `--sentiment` flag on `dg read` analyzes text to determine overall sentiment — positive, negative, or neutral — along with a confidence score. This is useful for analyzing customer reviews, feedback forms, support tickets, and any text where understanding the emotional tone matters.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--sentiment` | flag | Enables sentiment analysis on the text |

## Example output

```
Sentiment: positive (0.93)
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
