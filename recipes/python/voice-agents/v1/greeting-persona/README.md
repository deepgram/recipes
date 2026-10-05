# Greeting and Persona Configuration (Voice Agents v1)

Configure a voice agent with a custom greeting message and a system prompt that defines its personality, conversational style, and behavioral constraints.

## What it does

When a voice agent session starts, the agent automatically speaks the `greeting` message without waiting for user input. The `think.prompt` system prompt shapes every subsequent response — defining the agent's name, tone, topic scope, and response length. Together, these two settings let you build branded, on-topic voice experiences.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `agent.greeting` | `"Hello! I'm Nova..."` | Message the agent speaks when the session starts |
| `think.prompt` | *(persona string)* | System prompt defining personality, tone, topic scope, and guardrails |
| `think.provider.model` | `"gpt-4o-mini"` | LLM model powering the agent's responses |
| `speak.provider.model` | `"aura-2-thalia-en"` | TTS voice for the agent |

## Persona configuration options

- **Identity**: Give the agent a name and role ("You are Nova, a space exploration guide")
- **Tone**: Set conversational style ("warm, enthusiastic tone")
- **Topic scope**: Restrict what the agent will discuss ("only discuss space, astronomy, and NASA missions")
- **Redirect behavior**: Define how the agent handles off-topic questions ("politely redirect to space exploration")
- **Response length**: Control verbosity ("two to three sentences maximum")

## Example output

```
Agent configured with custom greeting and persona
Greeting: Hello! I'm Nova, your space exploration guide. Ask me anything about the cosmos!
Persona prompt: You are Nova, a friendly space exploration guide. You speak...
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
