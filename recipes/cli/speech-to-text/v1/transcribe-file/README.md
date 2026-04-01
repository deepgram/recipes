# Transcribe Local Audio File (STT v1)

Transcribes a local audio file by passing its file path directly to the Deepgram CLI. The CLI uploads the file to the Deepgram API and returns the transcript.

## What it does

The `dg listen` command accepts a local file path. It detects the audio format automatically, uploads the file, and returns a formatted transcript. This is ideal for processing recordings already stored on disk.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `nova-3` | Deepgram's latest and most accurate STT model |
| `--smart-format` | (flag) | Applies automatic formatting: punctuation, numbers, dates |

## Example output

```
Yeah, as much as, it's funny when I think about it. Like, I realize I can't even imagine
what it would be like to be mass. You know, the first mass space walk.
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- `curl` installed (to download sample audio)
- Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
