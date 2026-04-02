# Entity Detection (STT v1)

Identifies named entities in the transcript — people, organisations, locations, and dates.

## What it does

Enabling the `detect_entities` parameter tells Deepgram to scan the transcript for named entities and classify each one by type (e.g. `PERSON`, `ORG`, `DATE`, `LOCATION`). This is useful for extracting structured data from spoken content.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `nova-3` | Deepgram transcription model |
| `detect_entities` | `true` | Enables named entity detection |

## Example output

```
DATE: March 18th, 1965
PERSON: Alexei Leonov
ORG: NASA
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
