# Dynamic Context Injection (Voice Agents v1)

Dynamically update prompts, inject messages, and change agent behavior during an active voice agent session. This enables building agents that adapt in real time — loading customer data when a caller identifies themselves, switching personas based on conversation topic, or injecting context from external systems mid-conversation.

## What it does

Static voice agent prompts cannot handle conversations where context changes dynamically. This recipe demonstrates three mid-session control mechanisms:

1. **InjectAgentMessage** — Make the agent speak a specific phrase immediately, bypassing the LLM. Useful for scripted greetings or acknowledgments.
2. **UpdatePrompt** — Replace the system prompt while the session is active. The agent's behavior changes on the next LLM turn, enabling persona switching or context enrichment.
3. **InjectUserMessage** — Simulate a user utterance so the agent responds via the LLM with the new prompt context.

The recipe starts the agent as a general assistant, then switches it to a NASA specialist mid-conversation and asks a domain question — demonstrating how the agent's responses change after the prompt update.

## Key parameters

| Method | Type Field | Key Field | Description |
|--------|-----------|-----------|-------------|
| `sendInjectAgentMessage` | `"InjectAgentMessage"` | `message` | Agent speaks this text directly (no LLM) |
| `sendUpdatePrompt` | `"UpdatePrompt"` | `prompt` | Replaces the system prompt mid-session |
| `sendInjectUserMessage` | `"InjectUserMessage"` | `content` | Simulates user speech; agent responds via LLM |

## Example output

```
Settings applied — injecting initial context
Agent: Welcome! I am your general assistant.
Updating prompt to specialist persona
Prompt updated successfully
Injecting user question after prompt update
User: Tell me about the spacewalk mission.
Agent: The spacewalk mission involved astronauts performing extravehicular activities...
```

## Prerequisites

- Node.js 20+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `npm install`

## Run

```bash
node example.js
```
