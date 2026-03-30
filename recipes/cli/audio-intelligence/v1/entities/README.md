# Entity Detection (Audio Intelligence v1)

Identifies named entities in the audio — people, organisations, locations, dates, and other proper nouns.

## What it does

Enables the `detect_entities` parameter which scans the transcript for named entities and classifies each one by type. The response includes entity segments, each containing one or more entities with a label (e.g. `PERSON`, `ORG`, `DATE`, `LOCATION`) and the recognised text. This is useful for extracting structured data from spoken content.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Required model for entity detection |
| `detect_entities` | `true` | Enables named entity detection |

## Example output

```
DATE: March 18th, 1965
PERSON: Alexei Leonov
ORG: NASA
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
