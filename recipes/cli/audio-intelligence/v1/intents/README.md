# Intent Recognition (Audio Intelligence v1)

Detect caller/speaker intents from audio context.

## What it does

Sends audio to the `/v1/listen` endpoint with `intents=true` to identify the communicative purpose of each speech segment. Useful for understanding caller needs in contact centres and automating conversation routing.

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
