# Bit Rate Control (Text-to-Speech v1)

Controls the output audio bit rate for compressed encodings like MP3 and Opus. Lower bit rates produce smaller files suitable for bandwidth-constrained environments, while higher bit rates improve audio quality.

## What it does

The `bit_rate` parameter lets you specify the target bit rate (in bits per second) for compressed audio output. This gives you control over the quality-size tradeoff. Note: bit rate control only applies to compressed encodings (mp3, opus, etc.) — it has no effect on uncompressed formats like linear16.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `bit_rate` | `48000` | Target audio bit rate in bits per second |
| `encoding` | `"mp3"` | Compressed encoding format (required for bit rate to apply) |
| `model` | `aura-2-thalia-en` | Voice model for TTS |

## Example output

```
Bit rate: 48000 bps
Audio saved: 12480 bytes
Model: aura-2-thalia-en, Characters: 78
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```
