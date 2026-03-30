# Entity Detection (Audio Intelligence v1)

Identify named entities in audio: people, organisations, locations, and more.

## What it does

Sends audio to the `/v1/listen` endpoint with `detect_entities=true` to run named entity recognition on the transcript. Each entity includes a label (type), value (text), and confidence score.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Required model for entity detection |
| `detect_entities` | `true` | Enables named entity recognition |

## Example output

```
PERSON: Neil Armstrong (confidence: 0.95)
EVENT: spacewalk (confidence: 0.90)
DATE: 50th anniversary (confidence: 0.88)
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
