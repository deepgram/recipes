# Transcribe Audio from URL (Speech-to-Text v1)

Send a URL pointing to a hosted audio file for transcription using the Deepgram REST API.

## What it does

Makes a single REST API call to Deepgram's pre-recorded transcription endpoint with an audio URL.
Deepgram downloads the audio, transcribes it, and returns the full result including the transcript text,
confidence scores, and word-level timing.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"nova-3"` | Transcription model — nova-3 is the most accurate for most use cases |
| `smart_format` | `True` | Automatically format numbers, currencies, dates, and addresses |
| `url` | `"https://..."` | URL of the hosted audio file (mp3, wav, flac, ogg, etc.) |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of
the spacewalk, it's also worth noting that we've come a long way
since then...
```

## Prerequisites

- Python 3.10+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `pip install -r samples/python/requirements.txt`

## Run

```bash
python example.py
```

## Test

```bash
pytest example_test.py -v
```
