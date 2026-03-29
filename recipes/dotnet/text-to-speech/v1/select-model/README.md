# Select Voice Model

Choose different voice models to customize the speech characteristics and tone for your text-to-speech generation.

## How it works

This recipe demonstrates how to select from Deepgram's collection of voice models. Each model has unique characteristics such as gender, tone, and speaking style. By changing the model parameter, you can achieve different vocal qualities to match your application's needs.

## Key parameters

- **Model**: `aura-2-arcas-en` - A male, conversational English voice
- **Text**: Input text to convert to speech
- **Model options**: Various voices with different characteristics

## What you'll see

The example will generate audio using the selected model and display:

```
Generating audio with selected voice model...
Text: This example demonstrates selecting different voice models for text-to-speech generation.
Selected model: aura-2-arcas-en
Audio generated successfully!
Voice model used: aura-2-arcas-en
Output file: model_output.mp3
File size: 18456 bytes

Other available models include:
- aura-2-thalia-en (female, warm)
- aura-2-luna-en (female, friendly)
- aura-2-zeus-en (male, authoritative)
- aura-2-arcas-en (male, conversational)
```

## Available Models

- **aura-2-thalia-en**: Female voice with warm, natural tone
- **aura-2-luna-en**: Female voice with friendly, approachable style
- **aura-2-zeus-en**: Male voice with authoritative, commanding presence
- **aura-2-arcas-en**: Male voice with conversational, casual tone

## Prerequisites

- .NET 8.0 or later
- `DEEPGRAM_API_KEY` environment variable set

## Run the example

```bash
dotnet run
```

The generated audio file (`model_output.mp3`) will be created using the specified voice model.