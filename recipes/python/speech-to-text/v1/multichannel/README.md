# Multichannel Transcription (Speech-to-Text v1)

Transcribe each audio channel independently, producing a separate transcript per channel.

## What it does

When `multichannel=True` is set, Deepgram processes each audio channel as a separate stream. This is ideal for stereo recordings where different speakers occupy different channels (e.g., call-centre recordings with agent on one channel and caller on the other). Each channel gets its own transcript in the response.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `multichannel` | `True` | Transcribe each audio channel independently |
| `model` | `"nova-3"` | Transcription model |
| `smart_format` | `True` | Format numbers, dates, etc. |

## Example output

```
Channel 0: Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk...
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
