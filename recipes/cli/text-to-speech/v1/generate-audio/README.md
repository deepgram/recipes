# Generate Audio to File (Text-to-Speech v1)

Convert text to speech and save the resulting audio to a file.

## What it does

Sends text to Deepgram's `/v1/speak` endpoint and saves the returned audio to an MP3 file. Uses the aura-2-thalia-en voice model which produces natural-sounding English speech. The file size is printed to confirm successful generation.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `aura-2-thalia-en` | Natural-sounding English voice |

## Example output

```
Audio saved to /tmp/deepgram_tts_output.mp3 (24576 bytes)
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
