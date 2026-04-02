# Select Audio Encoding (TTS v1)

Choose the output audio encoding format for text-to-speech.

## What it does

The `--encoding` flag selects the audio codec and the `--container` flag selects the file container. This allows generating audio in formats like linear16 (raw PCM), mp3, flac, opus, mulaw, alaw, or aac. Different formats suit different use cases — linear16 for audio processing, mp3 for web delivery, opus for low-bandwidth streaming.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `-m` | `aura-2-thalia-en` | Voice model to use |
| `--encoding` | `linear16` | Audio encoding format |
| `--container` | `wav` | Audio container format |
| `-o` | file path | Output audio file path |

## Example output

```
Generated linear16/wav audio (48320 bytes)
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
