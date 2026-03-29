# Custom TTS Voice Model

Configures a voice agent to use a specific text-to-speech voice model, demonstrating how to customize the agent's speaking voice and audio output settings.

## What this demonstrates

Voice agents can use different TTS voice models to change how they sound when speaking. Deepgram offers various Aura voice models with different characteristics, accents, and speaking styles. This example shows how to configure a specific voice model and monitor audio output.

## Key parameters

- `Agent.Speak.Provider.Type = "deepgram"` - TTS provider (Deepgram, OpenAI, etc.)
- `Agent.Speak.Provider.Model = "aura-2-arcas-en"` - Specific voice model (vs default thalia)
- `Audio.Output.Encoding = "linear16"` - Audio format for TTS output
- `Audio.Output.SampleRate = 24000` - Audio quality/sample rate
- `Audio.Output.Container = "none"` - Audio container format

## Example output

```
Configuring voice agent with custom TTS settings:
TTS Provider: deepgram
TTS Voice Model: aura-2-arcas-en
Audio Output Encoding: linear16
Audio Output Sample Rate: 24000Hz
Connection result: True
Connected with custom TTS voice! Welcome: Hello! I'm speaking with the Arcas voice model.
Audio response received with 52480 bytes
Custom TTS voice configuration successful!
The agent will speak using the Arcas voice model
Agent session completed
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable
- Requires `OPENAI_API_KEY` for LLM provider (or configure different provider)

## Run the example

```bash
dotnet run
```