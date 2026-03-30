# Configure LLM Provider (Voice Agents v1)

Use OpenAI or Anthropic as the think model for your voice agent.

## What it does

The voice agent's "think" stage uses an LLM to generate responses to user speech. This recipe shows how to configure a specific LLM provider (OpenAI's GPT-4o-mini), set the temperature for response creativity, and provide a custom system prompt that shapes the agent's personality and knowledge domain.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `think.provider.type` | `"open_ai"` | LLM provider. Also supports `"anthropic"`. |
| `think.provider.model` | `"gpt-4o-mini"` | Specific model from the provider |
| `think.provider.temperature` | `0.7` | Controls response randomness (0=deterministic, 1=creative) |
| `think.prompt` | `str` | System prompt that shapes agent behaviour |

## Example output

```
Agent configured with OpenAI gpt-4o-mini as think provider
Connection opened
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
