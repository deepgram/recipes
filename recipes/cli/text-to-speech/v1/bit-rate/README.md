# Bit Rate Control (TTS v1)

Controls the output audio bit rate for compressed encodings like MP3.

## What it does

The `bit_rate` parameter controls the bit rate of compressed audio output from Deepgram's text-to-speech API. Lower bit rates (e.g., 32000) produce smaller files suitable for bandwidth-constrained environments, while higher bit rates (e.g., 128000) deliver better audio quality. This parameter only applies to compressed encodings like MP3 — it has no effect on uncompressed formats like linear16.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `aura-2-thalia-en` | Deepgram TTS voice model |
| `encoding` | `mp3` | Compressed audio encoding (required for bit rate control) |
| `bit_rate` | `48000` | Output bit rate in bits per second |

## Example output

```
Audio saved to /tmp/deepgram_bitrate.mp3 (12345 bytes, 48kbps MP3)
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- `DEEPGRAM_API_KEY` environment variable set

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
