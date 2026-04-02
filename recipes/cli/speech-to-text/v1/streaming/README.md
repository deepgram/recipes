# Live Streaming Transcription (STT v1)

WebSocket-based real-time transcription from a live audio stream.

## What it does

Streams raw audio over a WebSocket connection for real-time transcription. This example uses `ffmpeg` to convert a WAV file into raw linear16 audio and pipes it to `dg listen`. The CLI automatically opens a WebSocket connection when it detects stdin audio. In production, you would use `--mic` for microphone input or pipe from any live audio source.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `nova-3` | Deepgram transcription model |
| `--encoding` | `linear16` | Raw audio encoding format |
| `--smart-format` | flag | Enables smart formatting |

## Example output

```
Yeah, as much as, it's funny when I think of anything that's related to outer space...
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- `ffmpeg` installed
- `DEEPGRAM_API_KEY` environment variable set

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
