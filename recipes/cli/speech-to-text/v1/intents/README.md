# Intent Recognition (Speech-to-Text v1)

Detects speaker intents and communicative purposes within transcribed audio.

## What it does

Enables the `intents` parameter which runs AI-powered intent recognition on the transcript. Each speech segment is analyzed for its purpose — informing, requesting, describing, etc. This is an Audio Intelligence feature.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Required model for intent recognition |
| `intents` | `true` | Enables intent detection |

## Example output

```
Intent: inform (confidence: 0.92)
Intent: describe (confidence: 0.85)
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
