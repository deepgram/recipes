# Generate Audio to File (Text-to-Speech v1)

Convert text to audio file using Deepgram's Text-to-Speech API.

## What it does

This example demonstrates how to generate audio from text using Deepgram's Text-to-Speech API. The service converts the provided text into natural-sounding speech and saves it as an audio file, allowing you to specify voice models and audio settings.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"aura-2-thalia-en"` | Specifies the voice model to use for speech generation |

## Example output

```
Audio saved: output.wav (12345 bytes)
Model: aura-2-thalia-en, Characters: 42
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```