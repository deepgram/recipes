# Live Streaming Transcription (STT v2)

WebSocket streaming with the v2 listen endpoint using flux-general-en.

## What it does

Streams raw audio over a WebSocket connection for real-time transcription using the v2 API. This example uses `ffmpeg` to convert a WAV file into raw linear16 audio and pipes it to `dg listen`. The CLI automatically routes to the v2 WebSocket endpoint when a `flux-*` model is specified. Unlike v1's interim/final result pairs, v2 uses contextual turn detection to deliver turn-based transcription results.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `flux-general-en` | V2 English-optimized model with turn detection |
| `--encoding` | `linear16` | Raw audio encoding format |

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
