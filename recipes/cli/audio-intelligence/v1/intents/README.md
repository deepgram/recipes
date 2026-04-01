# Intent Recognition (Audio Intelligence v1)

Detects the goals or purposes behind what speakers are saying in the audio.

## What it does

Enables the `intents` parameter which analyses the transcript to identify speaker intents — the underlying goals or actions a speaker is trying to accomplish. Each segment of the transcript is returned with one or more detected intents and a confidence score. This is useful for understanding caller motivation in customer support, sales calls, or meeting recordings.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Required model for intent recognition |
| `intents` | `true` | Enables intent detection |

## Example output

```
Inform about event (confidence: 0.92)
Describe experience (confidence: 0.85)
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- `python3` installed
- Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
