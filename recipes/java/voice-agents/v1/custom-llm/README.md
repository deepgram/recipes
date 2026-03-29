# Configure LLM Provider (Voice Agents v1)

Configures your voice agent to use Anthropic Claude as the language model instead of the default OpenAI GPT model. This allows you to choose different LLM providers based on your needs, preferences, or specific capabilities.

## Key Parameters

- **Think provider**: `ThinkSettingsV1Provider.anthropic()` sets Anthropic as the LLM provider
- **Model selection**: `AnthropicThinkProviderModel.CLAUDE_SONNET420250514` specifies the Claude model
- **Custom prompt**: Tailored system prompt for the specific LLM provider

## Prerequisites

- Java 11 or higher
- Maven 3.9 or higher
- `DEEPGRAM_API_KEY` environment variable set
- Anthropic API access enabled in your Deepgram account

## Run

```bash
cd recipes/java/voice-agents/v1/custom-llm
mvn exec:java -Dexec.mainClass="Example"
```

## Expected Output

```
Agent connected: req_12345678-abcd-1234-abcd-123456789abc
Settings applied (Anthropic Claude)
```

The agent successfully connects and configures itself to use Anthropic Claude as the language model for generating responses.