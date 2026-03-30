# Transcribe Local Audio File (Speech-to-Text v1)

Read a local audio file and send it to the Deepgram REST API for transcription.

## What it does

Downloads a demo audio file, then sends the raw binary data to the `/v1/listen` endpoint using `Content-Type: audio/wav`. Deepgram transcribes the audio and returns the full transcript. This pattern works with any local audio format (wav, mp3, flac, ogg).

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Highest-accuracy transcription model |
| `smart_format` | `true` | Formats numbers, dates, currencies automatically |
| `Content-Type` | `audio/wav` | MIME type matching the audio file format |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of the spacewalk...
```

## Prerequisites

- `curl` and `python3` installed
- Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
