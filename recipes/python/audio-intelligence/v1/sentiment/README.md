# Sentiment Analysis (Audio Intelligence v1)

Segment-level positive/negative/neutral sentiment scoring on audio content.

## What it does

When `sentiment=True` is set, Deepgram analyses the emotional tone of each segment in the transcript and labels it as positive, negative, or neutral. This is valuable for call-centre analytics, customer feedback processing, or understanding the emotional arc of conversations and recordings.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `sentiment` | `True` | Enable sentiment analysis |
| `model` | `"nova-3"` | Transcription model |
| `smart_format` | `True` | Format numbers, dates, etc. |

## Example output

```
Transcript: Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk...

Sentiment segments: 4
  [positive] Yeah, as much as it's worth celebrating the 50th anniversary
  [neutral] it's also worth noting that we've come a long way since then
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
