# Select Audio Encoding (Text-to-Speech v1)

Choose the output audio encoding and container format for TTS generation.

## What it does

Demonstrates selecting the audio encoding format (linear16, mp3, flac, mulaw, alaw, opus, aac) and container (none, wav, ogg) for TTS output. This example generates a WAV file with linear16 encoding.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `aura-2-thalia-en` | Natural-sounding English voice |
| `encoding` | `linear16` | Raw PCM audio encoding |
| `container` | `wav` | WAV file container format |

## Example output

```
Audio saved as WAV with linear16 encoding (98304 bytes)
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
