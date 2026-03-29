# Generate Audio File

Generate speech audio from text and save it to a file using Deepgram's Text-to-Speech API.

## How it works

This recipe demonstrates how to convert text to speech using the REST API and save the resulting audio to a file. The example uses the `aura-2-thalia-en` model to generate high-quality speech audio from the provided text.

## Key parameters

- **Model**: `aura-2-thalia-en` - A high-quality English voice model
- **Text**: The input text to convert to speech
- **Output format**: MP3 audio file

## What you'll see

The example will generate an MP3 file containing the spoken text and display:

```
Generating audio...
Text: Hello from Deepgram! This is a text-to-speech example using the aura 2 model.
Model: aura-2-thalia-en
Audio generated successfully!
Output file: output.mp3
File size: 15432 bytes
```

## Prerequisites

- .NET 8.0 or later
- `DEEPGRAM_API_KEY` environment variable set

## Run the example

```bash
dotnet run
```

The generated audio file (`output.mp3`) will be created in the same directory and can be played with any audio player.