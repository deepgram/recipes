# Stream Audio File for Transcription (Speech-to-Text v1)

Stream local audio files over WebSocket for transcription.

## What it does

This example demonstrates how to stream a local audio file to Deepgram's Speech-to-Text WebSocket API for transcription. Unlike live streaming, this approach allows you to process pre-recorded audio files by streaming their contents over the WebSocket connection.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `encoding` | `"linear16"` | Specifies the audio encoding format |
| `sample_rate` | `8000` | Sets the audio sample rate in Hz |

## Example output

```
[Transcript results]
Stream file transcription complete
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```