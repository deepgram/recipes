# Configure LLM Provider (Voice Agents v1)

Use a custom LLM provider (OpenAI or Anthropic) as the think model for your voice agent.

## What it does

The voice agent's think stage can be configured to use different LLM providers. This example shows how to configure Anthropic's Claude as the LLM instead of the default OpenAI. The provider type and model name are set in the `think` section of the settings configuration.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `think.provider.type` | `anthropic` | LLM provider |
| `think.model` | `claude-sonnet-4-20250514` | Model to use |
| `think.instructions` | string | System prompt for the agent |

## Example output

```json
{
  "type": "SettingsConfiguration",
  "agent": {
    "think": {
      "provider": { "type": "anthropic" },
      "model": "claude-sonnet-4-20250514"
    }
  }
}

Voice agent configured with Anthropic LLM provider.
```

## Prerequisites

- Deepgram CLI installed (`curl -fsSL https://deepgram.com/install.sh | sh`)
- `DEEPGRAM_API_KEY` environment variable set
- `python3` installed

## Run

```bash
bash example.sh
```

## Test

```bash
bash example_test.sh
```
