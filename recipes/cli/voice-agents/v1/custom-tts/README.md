# Configure TTS Voice (Voice Agents v1)

Choose a specific aura-2 voice model for the agent's speech output.

## What it does

Demonstrates selecting a specific TTS voice for the voice agent's "speak" step. Swap the `speak.model` parameter to change the voice personality — Deepgram offers multiple aura-2 voices with different character and tone.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `speak.model` | `aura-2-arcas-en` | Alternative voice (deeper, authoritative) |

## Example output

```
Welcome: {"type": "Welcome", ...}
Voice agent with custom TTS voice initiated successfully
```

## Prerequisites

- `websocat` and `python3` installed
- Set `DEEPGRAM_API_KEY` environment variable

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
