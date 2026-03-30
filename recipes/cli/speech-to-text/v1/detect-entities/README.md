# Entity Detection (Speech-to-Text v1)

Identifies named entities in audio — people, places, organisations, dates, and more.

## What it does

Enables the `detect_entities` parameter which runs named entity recognition on the transcript. Each entity includes a label (type), value (text), and confidence score. This is an Audio Intelligence feature.

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
