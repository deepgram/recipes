# Custom LLM Configuration

Configures a voice agent with a custom LLM provider, model, and system prompt to customize the agent's personality and behavior.

## What this demonstrates

Voice agents can be customized with different LLM providers and models to change how they think and respond. The system prompt allows you to define the agent's personality, expertise domain, and response style.

## Key parameters

- `Agent.Think.Provider.Type = "open_ai"` - Specify the LLM provider (OpenAI, Anthropic, etc.)
- `Agent.Think.Provider.Model = "gpt-4o-mini"` - Choose the specific model variant
- `Agent.Think.Prompt` - Custom system prompt that defines agent behavior and personality
- Different providers support different models and capabilities

## Example output

```
Configuring voice agent with custom LLM settings:
LLM Provider: open_ai
LLM Model: gpt-4o-mini
Custom Prompt: You are a helpful assistant that always responds with enthusiasm and uses emojis.
Connection result: True
Connected with custom LLM! Welcome: Hello! I'm your custom AI assistant with a personalized prompt!
Custom LLM configuration successful!
Agent session completed
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable
- Set `OPENAI_API_KEY` for OpenAI provider (or configure different provider with appropriate API key)

## Run the example

```bash
dotnet run
```