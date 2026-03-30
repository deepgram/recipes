# Multichannel (Speech-to-Text v1)

Transcribes each audio channel independently for stereo or multi-track recordings.

## What it does

The `--multichannel` flag instructs Deepgram to treat each audio channel as a separate stream and transcribe them independently. This is ideal for call center recordings where the agent and caller are on separate channels, or any stereo recording where each speaker has their own track.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `--model` | `nova-3` | Specifies the Nova 3 transcription model |
| `--multichannel` | (flag) | Enables independent per-channel transcription |

## Example output

```
[Channel 0] Yeah, as confirmed, I'd like to inform you that we have had temporary loss of communication.
[Channel 1] Copy that. We're monitoring from the ground.
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```