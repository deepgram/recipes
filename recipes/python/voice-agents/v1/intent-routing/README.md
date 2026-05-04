# Intent-Aware Voice Agent Routing (Voice Agents v1)

Configure a Deepgram Voice Agent with a system prompt that classifies caller intent and routes to department-specific responses — no external telephony dependencies required.

## What it does

Opens a WebSocket connection to Deepgram's Agent API and configures the agent's "think" stage with a system prompt that acts as an IVR (Interactive Voice Response) dispatcher. The prompt instructs the LLM to greet the caller, classify their intent as billing, support, or sales, confirm the department, and then respond with department-appropriate guidance. This demonstrates how prompt engineering alone can drive call routing logic inside a voice agent session.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `think.prompt` | IVR routing prompt | System prompt that defines intent categories and per-department behavior |
| `think.provider.model` | `"gpt-4o-mini"` | LLM that performs intent classification and generates responses |
| `listen.provider.model` | `"nova-3"` | STT model for the listen stage |
| `speak.provider.model` | `"aura-2-thalia-en"` | TTS model for spoken responses |
| `audio.input.encoding` | `"linear16"` | Input audio encoding |
| `audio.input.sample_rate` | `24000` | Input audio sample rate |

## Example output

```
Voice agent configured with intent-routing IVR prompt
Connection opened
Event: SettingsApplied
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
