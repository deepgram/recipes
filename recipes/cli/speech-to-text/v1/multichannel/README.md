# Multichannel (Speech-to-Text v1)

Transcribes each audio channel independently for multi-track recordings.

## What it does

Enables the `multichannel` parameter which produces a separate transcript for each audio channel. For stereo recordings where different speakers are on different channels (e.g. call center recordings), this gives you per-channel transcripts instead of a single mixed result.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Highest-accuracy transcription model |
| `multichannel` | `true` | Transcribes each audio channel independently |

## Example output

```
[Channel 0] Yeah, as much as it's worth celebrating the 50th anniversary...
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
