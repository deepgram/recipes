# Transcribe Local Audio File (STT v1)

Transcribes a local audio file by sending it directly to Deepgram.

## What it does

The `dg listen` command auto-detects when the source argument is a local file path and uploads the file contents to Deepgram for transcription. This is different from URL-based transcription where Deepgram fetches the audio itself. File-based transcription is useful when your audio is not publicly accessible or when you want to process local recordings.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `nova-3` | Deepgram transcription model |
| `--smart-format` | flag | Enables smart formatting |

## Example output

```
Yeah, as much as, it's funny when I think of anything that's related to
outer space, I think of is the first, the first shuttle launch...
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- `DEEPGRAM_API_KEY` environment variable set
- `curl` installed (to download the demo audio file)

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
