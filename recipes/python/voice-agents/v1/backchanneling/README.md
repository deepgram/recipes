# Backchanneling — Inject Acknowledgments (Voice Agents v1)

Inject brief acknowledgment phrases into a voice agent conversation so the agent feels more natural and engaged, without interrupting the user's speech.

## What it does

Human conversations include constant backchanneling — listeners signal engagement with brief acknowledgments like "mm-hmm", "I see", and "got it" at natural pause points. This recipe uses `send_inject_agent_message` with `behavior="queue"` to inject short agent utterances that play after the current turn finishes, creating a more natural conversational flow. The queued behavior ensures the backchannel never interrupts the user or an in-progress agent response.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `AgentV1InjectAgentMessage.message` | `"mm-hmm"` | The brief acknowledgment text the agent speaks |
| `AgentV1InjectAgentMessage.behavior` | `"queue"` | Queues the message after the current turn — never interrupts |
| `behavior="default"` | *(alternative)* | Speaks only if no turn is in progress; otherwise `InjectionRefused` |
| `behavior="interrupt"` | *(alternative)* | Immediately interrupts the current speaker |

## Behavior options

- **`queue`** (used here) — Appends the message after any in-progress speech. Ideal for backchanneling because it never cuts off the user.
- **`default`** — Speaks only when idle. The server returns `InjectionRefused` if a turn is active.
- **`interrupt`** — Immediately speaks, cutting off whoever is talking. Useful for urgent interjections but not for subtle acknowledgments.

## Example output

```
Connection opened
Agent configured — injecting backchannels between user messages
Backchannel queued: "mm-hmm"
Event: ConversationText
[assistant] mm-hmm
Received 4800 bytes of agent audio
[user] I've been working on a new project involving speech recognition.
Backchannel queued: "got it"
[assistant] got it
Received 3200 bytes of agent audio
[user] The goal is to make voice interfaces feel more human and natural.
Event: AgentThinking
[assistant] That sounds like a great goal...
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
