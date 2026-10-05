# Transcribe Local Audio File — v2 API (Speech-to-Text v2)

Read a local audio file into memory and transcribe it using the flux-general-en model, Deepgram's highest-accuracy English model.

## What it does

Loads audio bytes from a local file and sends them to Deepgram's `transcribe_file()` endpoint with `model="flux-general-en"`. The flux-general-en model is optimised for English audio and provides improved accuracy over nova-3 for English-only use cases. The response includes word-level timestamps and confidence scores, making it easy to build features like subtitle generation or keyword spotting.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `request` | `bytes` | Raw audio bytes read from the local file |
| `model` | `"flux-general-en"` | v2 English-optimised transcription model |
| `smart_format` | `True` | Automatically format numbers, currencies, dates, and addresses |

## Supported audio formats

The API accepts WAV, MP3, FLAC, OGG, and other common audio formats. The content type is detected automatically from the file bytes.

## Example output

```
Downloaded 4379648 bytes
Yeah, as much as it's worth celebrating the 50th anniversary of
the spacewalk, it's also worth noting that we've come a long way
since then...
  Yeah             0.08s - 0.39s  (conf: 0.997)
  as               0.40s - 0.48s  (conf: 0.998)
  much             0.48s - 0.64s  (conf: 0.999)
  ...
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
