# Entity Detection (Speech-to-Text v1)

Identify named entities — people, places, organisations, dates, and more — in your audio transcript.

## What it does

When `detect_entities=True` is set, Deepgram identifies and categorises named entities mentioned in the audio. Each entity is returned with its category label, text value, confidence score, and position in the transcript. This is useful for extracting structured information from conversations or recordings.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `detect_entities` | `True` | Enable entity detection in the transcript |
| `model` | `"nova-3"` | Transcription model |
| `smart_format` | `True` | Format numbers, dates, etc. |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk...

Detected entities:
  [DATE] 50th anniversary (confidence: 0.95)
  [PERSON] Ed White (confidence: 0.92)
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
