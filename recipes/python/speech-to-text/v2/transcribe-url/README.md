# Transcribe Audio from URL — v2 API (Speech-to-Text v2)

Transcribe English audio using the flux-general-en model, Deepgram's highest-accuracy English model.

## What it does

Uses the flux-general-en model for pre-recorded transcription. This model is optimised for English audio and offers improved accuracy over nova-3 for English-only use cases. The Python SDK accesses this via the same `transcribe_url()` method — just set `model="flux-general-en"`.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"flux-general-en"` | v2 English-optimised transcription model |
| `smart_format` | `True` | Format numbers, dates, etc. |
| `url` | `"https://..."` | URL of the hosted audio file |

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
