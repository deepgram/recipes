# Wake Word Activation (Voice Agents v1)

Activate a voice agent only after detecting a wake phrase in audio, minimizing cloud API usage and cost.

## What it does

Implements a two-phase activation pattern for hands-free voice experiences:

1. **IDLE phase** — Transcribes audio with Deepgram STT (nova-3) and scans the transcript for a configurable wake phrase (e.g., "spacewalk").
2. **ACTIVE phase** — Once the wake phrase is detected, opens a Voice Agent WebSocket session with listen-think-speak pipeline and begins a conversation.

This pattern is the foundation for smart speakers, kiosk deployments, accessibility interfaces, and automotive voice systems where you want to avoid streaming audio to the cloud until the user explicitly activates the agent.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `WAKE_PHRASE` | `"spacewalk"` | The phrase that triggers agent activation |
| `model` (STT) | `"nova-3"` | Speech-to-text model for wake word detection |
| `think.provider.model` | `"gpt-4o-mini"` | LLM model for the agent's think stage |
| `speak.provider.model` | `"aura-2-thalia-en"` | TTS model for agent speech output |
| `audio.input.encoding` | `"linear16"` | Input audio encoding for the agent session |
| `audio.input.sample_rate` | `24000` | Input audio sample rate |

## Example output

```
STATE: IDLE — listening for wake phrase…
STATE: WAKE_WORD_DETECTED — 'spacewalk' found in audio
STATE: AGENT_ACTIVE — opening voice agent session
Agent: The first all-female spacewalk took place on October 18, 2019...
STATE: IDLE — agent session ended
```

## Prerequisites

- Python 3.10+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `pip install -r recipes/python/requirements.txt`

## Run

```bash
python example.py
```

## Test

```bash
pytest example_test.py -v --timeout=120
```
