# Dynamic Persona Switching (Voice Agents v1)

Switch a voice agent's personality, system prompt, and TTS voice mid-session without disconnecting.

## What it does

Defines three distinct agent personas — sales, support, and billing — each with its own system prompt and aura-2 voice model. After establishing a voice agent session with the sales persona, the example hot-swaps to the support persona using `send_update_prompt()` and `send_update_speak()`. The agent then responds to a user message using the new persona's behavior and voice. Conversation context is preserved across switches because the WebSocket session stays open.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `AgentV1UpdatePrompt.prompt` | `str` | New system prompt that shapes agent behavior |
| `AgentV1UpdateSpeak.speak` | `SpeakSettingsV1` | New TTS provider and voice model |
| `send_update_prompt()` | method | Update the agent's prompt mid-session |
| `send_update_speak()` | method | Switch the agent's TTS voice mid-session |

## Persona definitions

| Persona | Voice Model | Behavior |
|---------|-------------|----------|
| Sales | `aura-2-thalia-en` | Friendly, highlights product benefits |
| Support | `aura-2-arcas-en` | Precise, gives step-by-step technical help |
| Billing | `aura-2-luna-en` | Clear, focused on charges and dates |

## Example output

```
Agent started with persona: sales
Switched to persona: support (voice=aura-2-arcas-en)
Confirmed: PromptUpdated
Confirmed: SpeakUpdated
[agent] I'd be happy to help you troubleshoot. First, can you tell me what error
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
pytest example_test.py -v
```
