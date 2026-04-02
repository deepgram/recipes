# Multichannel (STT v1)

Transcribes each audio channel independently.

## What it does

Enabling the `multichannel` parameter tells Deepgram to produce a separate transcript for each audio channel. This is ideal for stereo call recordings where each participant is on a different channel. Since the CLI does not expose a `--multichannel` flag directly, this example uses `dg api` to pass the parameter.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Deepgram transcription model |
| `multichannel` | `true` | Transcribe channels independently |

## Example output

```
Channel 0: Yeah, as much as, it's funny when I think of anything that's related to outer space...
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
