# Select Voice Model (Text-to-Speech v1)

Choose different voice models for text-to-speech generation.

## What it does

This example demonstrates how to select specific voice models when generating speech from text using Deepgram's Text-to-Speech API. Different models provide various voice characteristics, accents, and speaking styles to match your application's needs.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"aura-2-arcas-en"` | Specifies the voice model to use for speech generation |

## Example output

```
Voice: aura-2-arcas-en
Audio saved: 12345 bytes
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```