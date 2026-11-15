# Inject Live Context into Voice Agent (Voice Agents v1)

Update a voice agent's system prompt mid-conversation with external context — such as a screen description from a vision model — so the agent can reference what the user is currently seeing.

## What it does

This recipe demonstrates the **multimodal context injection** pattern for Deepgram voice agents. While the voice agent handles real-time speech (listen-think-speak), your application can independently gather context from other sources — screen captures analyzed by a vision model, CRM lookups, sensor data — and inject that context into the agent's prompt using `send_update_prompt`. The agent's next response will incorporate the new context without interrupting the conversation flow.

The pattern works like this:

1. Connect a voice agent with a base system prompt
2. Capture external context (this example simulates a screen description)
3. Call `send_update_prompt` to append the context to the system prompt
4. The agent now "sees" the context and can reference it when responding

## Key parameters

| Method / Parameter | Value | Description |
|---|---|---|
| `send_update_prompt` | `AgentV1UpdatePrompt(prompt=...)` | Replaces the agent's system prompt mid-session |
| `send_inject_user_message` | `AgentV1InjectUserMessage(content=...)` | Injects a text message as if the user spoke it |
| `listen.provider.model` | `"nova-3"` | STT model for the listen stage |
| `think.provider.model` | `"gpt-4o-mini"` | LLM model for the think stage |
| `speak.provider.model` | `"aura-2-thalia-en"` | TTS model for the speak stage |

## Example output

```
Injecting screen context: The user's screen shows an error dialog: 'Connection timed out on port 443'.
[user] What's on my screen right now?
[assistant] I can see you have an error dialog showing a connection timeout on port 443. This usually means the HTTPS connection to the server failed. Check your firewall settings or try again in a few moments.
```

## Extending this pattern

In a production application, replace the hardcoded `SCREEN_CONTEXT` string with a periodic screen-capture loop:

1. Capture a screenshot (e.g. `PIL.ImageGrab` or `mss`)
2. Send it to a vision model (GPT-4o, Claude, Gemini) to get a text description
3. Call `agent.send_update_prompt(...)` with the updated description
4. Repeat on a configurable interval (e.g. every 5 seconds)

The voice agent conversation continues uninterrupted while the context updates happen in the background.

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
