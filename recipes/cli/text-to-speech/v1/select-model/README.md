# Select Voice Model (TTS v1)

Choose from available aura-2 voice models for text-to-speech.

## What it does

The `-m` flag selects which voice model to use for speech generation. Deepgram offers multiple aura-2 voices with different characteristics. This example uses `aura-2-arcas-en` to demonstrate model selection.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `-m` | `aura-2-arcas-en` | Voice model to use |
| `-o` | file path | Output audio file path |

## Available models

- `aura-2-thalia-en` — Female, warm
- `aura-2-arcas-en` — Male, professional
- `aura-2-luna-en` — Female, conversational
- And more — use `dg models --type tts` to list all

## Example output

```
Generated audio with aura-2-arcas-en (14280 bytes)
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
