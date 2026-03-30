# WebSocket Streaming TTS (Text-to-Speech v1)

Low-latency text-to-speech via WebSocket for real-time conversational use cases.

## What it does

Opens a WebSocket connection to Deepgram's TTS endpoint and sends text messages incrementally. Audio is synthesised and returned in real time as binary chunks. This is ideal for conversational UIs where text arrives word-by-word (e.g., from an LLM) and you want to start playing audio as early as possible.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"aura-2-thalia-en"` | Voice model |
| `encoding` | `"linear16"` | Audio encoding for the WebSocket stream |
| `sample_rate` | `24000` | Output sample rate in Hz |

## Example output

```
Received 48000 bytes of audio via WebSocket
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
