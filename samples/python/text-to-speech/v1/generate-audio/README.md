# Generate Audio to File (Text-to-Speech v1)

Convert text to speech using an aura-2 voice model and save the audio to a file.

## What it does

Makes a REST request to Deepgram's TTS endpoint, which returns audio in the requested format.
The SDK saves the audio directly to a file. This is ideal for batch audio generation, podcasts,
notifications, and any scenario where you need audio as a file.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `"aura-2-thalia-en"` | Voice model — see available voices below |
| `encoding` | `"mp3"` | Output format: `mp3`, `linear16`, `opus`, `flac`, `aac`, `mulaw` |

## Available aura-2 voices (English)

- `aura-2-thalia-en` — Warm, conversational female voice
- `aura-2-arcas-en` — Clear, professional male voice
- `aura-2-luna-en` — Bright, expressive female voice
- `aura-2-zeus-en` — Deep, authoritative male voice

## Example output

```
Saved output.mp3: 48320 bytes (audio/mpeg)
```

## Prerequisites

- Python 3.10+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `pip install -r samples/python/requirements.txt`

## Run

```bash
python example.py
# Produces output.mp3
```

## Test

```bash
pytest example_test.py -v
```
