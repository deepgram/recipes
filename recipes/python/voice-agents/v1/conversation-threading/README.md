# Conversation Threading (Voice Agents v1)

Resume a voice agent conversation across sessions by injecting prior conversation history.

## What it does

When a voice agent session ends — whether the user disconnects, a network error occurs, or the conversation spans multiple days — the conversation context is lost. This recipe demonstrates how to persist conversation turns to a JSON file and replay them into a new agent session using `send_inject_user_message()` and `send_inject_agent_message()`. The agent picks up exactly where the prior session left off, referencing earlier context in its response.

On first run, seed conversation turns are used. On subsequent runs, the persisted thread file is loaded, so the agent retains memory across sessions.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `send_inject_user_message` | `AgentV1InjectUserMessage(content=...)` | Replay a prior user turn into the session |
| `send_inject_agent_message` | `AgentV1InjectAgentMessage(message=...)` | Replay a prior assistant turn into the session |
| `think.prompt` | `"Continue the conversation..."` | Instructs the LLM to use injected context |
| `listen.provider.model` | `"nova-3"` | STT model for the listen stage |
| `think.provider.model` | `"gpt-4o-mini"` | LLM model for the think stage |
| `speak.provider.model` | `"aura-2-thalia-en"` | TTS model for the speak stage |

## Example output

```
Loaded 2 prior turns from thread
Prior context injected — asking follow-up
Agent: The first all-female spacewalk lasted about 7 hours and 17 minutes.
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
