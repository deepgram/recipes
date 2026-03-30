# Select Audio Encoding (Text-to-Speech v1)

Choose the output audio encoding and container format for generated speech.

## What it does

By default, Deepgram TTS returns mp3 audio. You can request different encodings such as linear16 (raw PCM), opus, flac, aac, or mulaw. The `container` parameter controls whether the output includes a container header (e.g., WAV) or is raw headerless audio.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `encoding` | `"linear16"` | Output encoding. Options: `linear16`, `mp3`, `opus`, `flac`, `aac`, `mulaw` |
| `container` | `"wav"` | Container format. Use `"none"` for headerless raw audio. |
| `sample_rate` | `24000` | Output sample rate in Hz |
| `model` | `"aura-2-thalia-en"` | Voice model |

## Example output

```
Saved output.wav (48256 bytes) — encoding: linear16, container: wav
```

## Prerequisites

- Python 3.10+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `pip install -r recipes/python/requirements.txt`

## Run

```bash
python example.py
```

## Test

```bash
pytest example_test.py -v
```
