# Connect to Voice Agent (Voice Agents v1)

Establishes a WebSocket voice agent session with default settings.

## What it does

Demonstrates the configuration payload for connecting to Deepgram's Voice Agent API. The voice agent uses a listen-think-speak pipeline: STT for listening, an LLM for thinking, and TTS for speaking. This example prints the settings configuration that would be sent over the WebSocket connection.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `listen.model` | `nova-3` | STT model for voice input |
| `think.model` | `gpt-4o-mini` | LLM model for processing |
| `speak.model` | `aura-2-thalia-en` | TTS model for voice output |

## Example output

```json
{
  "type": "SettingsConfiguration",
  "audio": { ... },
  "agent": { ... }
}

Voice agent configuration ready.
In production, send this payload over a WebSocket to wss://agent.deepgram.com/agent
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
