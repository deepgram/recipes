# Sentiment Analysis (Speech-to-Text v1)

Analyze the emotional tone of spoken audio, scoring each segment as positive, negative, or neutral.

## What it does

When `sentiment=True`, Deepgram evaluates the emotional tone of the transcript at both the
segment level and as an overall average. Each segment receives a sentiment label and a numerical
confidence score. This is useful for analyzing customer calls, feedback, or any audio where
emotional tone matters.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `sentiment` | `True` | Enable sentiment analysis |
| `model` | `"nova-3"` | Best model for transcription quality |

## Example output

```
Overall: positive (0.723)
  [positive] Yeah, as much as it's worth celebrating the 50th anniversary
  [neutral] of the spacewalk, it's also worth noting
```

## Prerequisites

- Python 3.10+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `pip install -r recipes/python/requirements.txt`

## Run

```bash
python example.py
```

## Test

```bash
pytest example_test.py -v
```
