# Connect to Voice Agent (Voice Agents v1)

Establish a WebSocket voice agent session with default settings.

## What it does

Opens a WebSocket connection to Deepgram's voice agent API at `wss://agent.deepgram.com/agent` and sends a configuration message to initialise the listen-think-speak pipeline. The agent uses nova-3 for speech recognition, gpt-4o-mini for conversation, and aura-2 for speech synthesis.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `listen.model` | `nova-3` | Speech recognition model |
| `think.model` | `gpt-4o-mini` | LLM for conversation |
| `speak.model` | `aura-2-thalia-en` | TTS voice model |

## Example output

```
Welcome: {"type": "Welcome", ...}
Voice agent session initiated successfully
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
