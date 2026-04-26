# Conversation Memory (Voice Agents v1)

Maintain conversation context across multiple turns so a voice agent can reference prior statements, remember user preferences, and build on earlier exchanges.

## What it does

Configures a Deepgram voice agent with two memory mechanisms:

1. **Initial context** — Pre-loads conversation history into the agent's settings using `AgentV1SettingsAgentContext` with `messages`. This lets the agent "remember" facts from a previous session (e.g., the user's name or preferences).

2. **Dynamic prompt updates** — Listens for `ConversationText` events, accumulates them in a local memory list, and periodically calls `send_update_prompt()` to inject the conversation history into the system prompt. A sliding window (last 10 turns) keeps the context within token limits.

Together these patterns give the agent multi-turn coherence without requiring an external database.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `agent.context.messages` | `list[History]` | Pre-loaded conversation history messages |
| `context.messages[].type` | `"History"` | Message type for conversation history entries |
| `context.messages[].role` | `"user"` / `"assistant"` | Who spoke the message |
| `send_update_prompt()` | method | Dynamically update the agent's system prompt mid-session |
| `AgentV1UpdatePrompt.prompt` | `str` | New system prompt including accumulated context |

## Example output

```
Agent configured with conversation memory
Loaded 2 prior context messages
Connection opened
Event: SettingsApplied
[user] What's my name?
[assistant] Your name is Alice! You also mentioned that you like jazz.
Prompt updated with 2 turns in memory
Connection closed
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
