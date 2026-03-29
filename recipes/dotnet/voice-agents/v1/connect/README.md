# Connect to Voice Agent

Establishes a basic connection to Deepgram's Voice Agent service with default settings and subscribes to event handlers.

## What this demonstrates

Voice agents provide real-time conversational AI capabilities by combining speech recognition, language models, and text-to-speech in a single WebSocket connection. This example shows the fundamental connection pattern and event handling.

## Key parameters

- `Agent.Think.Provider.Type = "open_ai"` - LLM provider for conversation logic
- `Agent.Think.Provider.Model = "gpt-4o-mini"` - Specific LLM model to use  
- `Agent.Listen.Provider.Model = "nova-3"` - Speech recognition model
- `Agent.Speak.Provider.Model = "aura-2-thalia-en"` - Text-to-speech voice
- `Agent.Greeting` - Welcome message the agent speaks when connected

## Example output

```
Connection attempt result: True
Agent connected! Welcome message: Hello! I'm your voice assistant.
Successfully received welcome: Hello! I'm your voice assistant.
Agent session completed
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable
- Requires `OPENAI_API_KEY` for LLM provider (or configure different provider)

## Run the example

```bash
dotnet run
```