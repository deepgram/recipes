# Stream Audio File for Transcription (Speech-to-Text v1)

Stream a local audio file over WebSocket for real-time transcription with incremental results.

## What it does

Opens a WebSocket connection and sends a local audio file in chunks, simulating a live audio stream. Deepgram returns transcripts incrementally as chunks arrive. This is useful for processing large files when you want results before the entire file has been uploaded, or when building a pipeline that processes audio in real time.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"nova-3"` | Transcription model |
| `smart_format` | `True` | Format numbers, dates, etc. |

## Example output

```
Streaming 4379648 bytes over WebSocket
Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk,
it's also worth noting that we've come a long way since then...
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
