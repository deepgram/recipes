# Select Audio Encoding

Choose different audio encodings to control file size, quality, and compatibility for your text-to-speech output.

## How it works

This recipe demonstrates how to select different audio encodings when generating speech. The encoding determines the audio format, compression level, and resulting file characteristics. Different encodings are optimized for different use cases, from high-quality uncompressed audio to efficient compressed formats.

## Key parameters

- **Encoding**: `mp3` - Compressed audio format for smaller file sizes
- **Container**: `none` - No additional container wrapping
- **Model**: `aura-2-thalia-en` - Voice model for generation
- **Format options**: Multiple encoding types available

## What you'll see

The example will generate audio using the selected encoding and display:

```
Generating audio with selected encoding...
Text: This example demonstrates selecting different audio encodings for text-to-speech output.
Selected encoding: mp3
Container: none
Audio generated successfully!
Encoding used: mp3
Output file: encoding_output.mp3
File size: 12847 bytes

Other available encodings include:
- linear16 (uncompressed PCM)
- mp3 (compressed, smaller files)
- opus (low-latency, efficient)
- flac (lossless compression)
- aac (high-quality compression)
- mulaw (telephone quality)
```

## Available Encodings

- **linear16**: Uncompressed PCM audio, highest quality, largest files
- **mp3**: Popular compressed format, good quality-to-size ratio
- **opus**: Modern codec, excellent for streaming and low-latency applications
- **flac**: Lossless compression, smaller than linear16 but larger than lossy formats
- **aac**: Advanced Audio Codec, efficient compression with good quality
- **mulaw**: Traditional telephony codec, smallest files but lower quality

## Prerequisites

- .NET 8.0 or later
- `DEEPGRAM_API_KEY` environment variable set

## Run the example

```bash
dotnet run
```

The generated audio file (`encoding_output.mp3`) will be created using the specified encoding format.