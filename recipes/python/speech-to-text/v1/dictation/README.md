# Dictation Mode (Speech-to-Text v1)

Interprets dictation-style spoken punctuation commands and converts them to their written equivalents in the transcript. When speakers say words like "period", "comma", or "new paragraph", dictation mode replaces them with the actual punctuation marks.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"nova-3"` | Transcription model |
| `dictation` | `True` | Enable dictation mode — spoken punctuation becomes written punctuation |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of
the spacewalk, it's also worth noting that we've come a long way
since then...
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
