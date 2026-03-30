# Live Streaming Transcription (Speech-to-Text v1)

Real-time transcription via WebSocket, receiving interim and final results as audio is spoken.

## What it does

Opens a WebSocket connection to Deepgram's v1 streaming API and sends audio chunks in real time. As audio arrives, Deepgram returns interim (partial) results and final results. Interim results update as more context arrives; final results are committed and won't change. This recipe simulates live audio by downloading a WAV file and streaming it in chunks.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"nova-3"` | Transcription model |
| `smart_format` | `True` | Format numbers, dates, etc. |
| `interim_results` | `True` | Receive partial transcripts as audio is being processed |

## Example output

```
[interim] Yeah as much as it's worth
[final] Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk,
[interim] it's also worth noting
[final] it's also worth noting that we've come a long way since then...
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
