# Search (Speech-to-Text v1)

Find specific words or phrases in audio with confidence scores and timestamps.

## What it does

When `search` is set, Deepgram searches the audio signal for the specified terms and returns matches with confidence scores and time positions. Unlike text search over a transcript, this operates at the audio level, so it can find terms even if they would be transcribed differently.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `search` | `"spacewalk"` | Term(s) to search for in the audio. Pass a list for multiple terms. |
| `model` | `"nova-3"` | Transcription model |
| `smart_format` | `True` | Format numbers, dates, etc. |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk...

Search results:
  Query: "spacewalk" — 2 hit(s)
    [5.12s - 5.68s] confidence: 0.98
    [42.31s - 42.89s] confidence: 0.95
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
