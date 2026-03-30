# Select Voice Model (Text-to-Speech v1)

Choose from available aura-2 voice models to change the voice personality.

## What it does

Demonstrates selecting a specific voice model for TTS generation. Deepgram offers multiple aura-2 voices with different character and tone. Swap the `model` parameter to try different voices while keeping everything else the same.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `aura-2-arcas-en` | Alternative voice model (deeper, authoritative) |

## Example output

```
Audio generated with aura-2-arcas-en model (24576 bytes)
```

## Prerequisites

- `curl` installed
- Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
