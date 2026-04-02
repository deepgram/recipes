# Stream Audio File for Transcription (STT v1)

Streams a local audio file over WebSocket for real-time transcription.

## What it does

Sends audio from a local file incrementally over a WebSocket connection rather than uploading it all at once. This demonstrates real-time processing of file-based audio. The file is converted to raw linear16 using `ffmpeg` and piped into `dg listen`, which opens a streaming WebSocket session.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `nova-3` | Deepgram transcription model |
| `--encoding` | `linear16` | Raw audio encoding for stdin streams |

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
