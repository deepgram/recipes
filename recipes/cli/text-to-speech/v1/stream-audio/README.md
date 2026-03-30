# Stream Audio Response (Text-to-Speech v1)

Stream TTS audio as it generates using REST streaming with linear16 encoding.

## What it does

Sends text to Deepgram's `/v1/speak` endpoint with `encoding=linear16` and streams the audio response to a file. The streaming approach allows playback to begin before the full response is complete. Raw PCM audio is saved for maximum flexibility.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `aura-2-thalia-en` | Natural-sounding English voice |
| `encoding` | `linear16` | Raw PCM audio encoding |

## Example output

```
Streamed audio saved to /tmp/deepgram_tts_stream.raw (98304 bytes, linear16 PCM)
```

## Prerequisites

- `curl` installed
- Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
