# Configure TTS Voice (Voice Agents v1)

Choose a specific aura-2 voice model for the agent's speech output.

## What it does

The voice agent's speak stage can be configured with different aura-2 voice models. This example uses `aura-2-arcas-en` instead of the default voice. Different voices have different characteristics — some are warmer, others more professional.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `speak.model` | `aura-2-arcas-en` | TTS voice model |

## Available voices

- `aura-2-thalia-en` — Female, warm
- `aura-2-arcas-en` — Male, professional
- `aura-2-luna-en` — Female, conversational

## Example output

```json
{
  "type": "SettingsConfiguration",
  "agent": {
    "speak": { "model": "aura-2-arcas-en" }
  }
}

Voice agent configured with aura-2-arcas-en TTS voice.
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- `DEEPGRAM_API_KEY` environment variable set
- `python3` installed

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
