# WebSocket Streaming TTS (Text-to-Speech v1)

Low-latency text-to-speech via WebSocket for real-time use cases.

## What it does

Opens a WebSocket connection to Deepgram's `/v1/speak` endpoint and sends text as JSON messages. Audio chunks are received as binary frames, enabling low-latency playback. This approach is ideal for conversational AI and real-time applications.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `aura-2-thalia-en` | Natural-sounding English voice |
| `encoding` | `linear16` | Raw PCM audio encoding |

## Example output

```
WebSocket TTS audio saved to /tmp/deepgram_tts_ws.raw (98304 bytes)
```

## Prerequisites

- `curl` and `websocat` installed
- Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
