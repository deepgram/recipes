# Stream Audio Response

Stream text-to-speech audio data directly from the API response without creating intermediate files.

## How it works

This recipe demonstrates how to use the REST streaming API to receive audio data as a stream. Instead of generating a complete file first, the audio is streamed directly from the response and saved to disk. This approach is useful for handling larger audio files or when you need to process audio data as it arrives.

## Key parameters

- **Model**: `aura-2-thalia-en` - A high-quality English voice model  
- **Encoding**: `linear16` - Uncompressed PCM audio format
- **Stream processing**: Direct stream-to-file copying

## What you'll see

The example will stream audio data and display:

```
Streaming audio...
Text: This is a streaming text-to-speech example using linear16 encoding.
Model: aura-2-thalia-en
Encoding: linear16
Audio streamed successfully!
Output file: streamed_output.wav
File size: 96000 bytes
Content-Type: audio/wav
```

## Prerequisites

- .NET 8.0 or later
- `DEEPGRAM_API_KEY` environment variable set

## Run the example

```bash
dotnet run
```

The streamed audio file (`streamed_output.wav`) will be created in the same directory and can be played with any audio player.