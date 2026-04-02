# Filler Words (Speech-to-Text v1)

Captures spoken filler words like "uh", "um", "mhm", and "uh-huh" in the transcript output. By default, Deepgram removes these hesitation markers for cleaner transcripts. Enabling filler words preserves them, which is useful for conversation analysis, speaker profiling, and verbatim transcription.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"nova-3"` | Transcription model |
| `filler_words` | `True` | Include filler words ("uh", "um", etc.) in the transcript |
| `smart_format` | `True` | Auto-format numbers, dates, and addresses |

## Example output

```
Yeah, um, as much as it's worth celebrating the, uh, 50th anniversary of
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
