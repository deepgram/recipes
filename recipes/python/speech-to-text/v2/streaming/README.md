# Live Streaming Transcription — v2 API (Speech-to-Text v2)

Real-time transcription via WebSocket using the v2 API with flux-general-en and contextual turn detection.

## What it does

Opens a WebSocket connection to Deepgram's v2 streaming endpoint. The v2 API uses the flux-general-en model with contextual turn detection, meaning it understands conversational boundaries. Instead of v1's interim/final result pairs, v2 returns `TurnInfo` events that include the transcript, turn index, and event type.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"flux-general-en"` | v2 English model with turn detection |
| `encoding` | `"linear16"` | Audio encoding format |
| `sample_rate` | `"16000"` | Audio sample rate in Hz |

## Example output

```
[turn 0] Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk,
[turn 0] it's also worth noting that we've come a long way since then.
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
