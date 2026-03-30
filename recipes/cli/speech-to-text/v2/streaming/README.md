# Live Streaming Transcription — v2 (Speech-to-Text v2)

Streams audio over WebSocket using the v2 flux-general-en model for real-time transcription.

## What it does

Pipes raw PCM audio into the Deepgram CLI which connects to the v2 WebSocket endpoint using the `flux-general-en` model. This English-only model provides higher accuracy for streaming use cases. The example uses ffmpeg to convert a WAV file to raw audio, simulating a live source.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--encoding` | `linear16` | Specifies raw PCM audio format |
| `--model` | `flux-general-en` | Uses the v2 flux English-only model |

## Example output

```
Yeah, as confirmed, I'd like to inform you that we have had
temporary loss of communication with the ISS.
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- `ffmpeg` installed
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