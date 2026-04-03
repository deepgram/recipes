# Bit Rate Control

Controls the output audio bit rate for compressed encodings like MP3 in text-to-speech. Lower bit rates produce smaller files suitable for bandwidth-constrained applications, while higher bit rates offer better audio quality.

## What this feature does

The bit rate parameter specifies the target bit rate in bits per second for compressed audio output. This only applies to lossy encodings like MP3 — lossless formats like Linear16 and FLAC ignore this parameter. Common values include 32000 (32 kbps), 48000 (48 kbps), 64000 (64 kbps), and 128000 (128 kbps).

## Key parameters

- **bit_rate(48000)**: Sets the output bit rate to 48 kbps
- **encoding(Encoding::Mp3)**: Required — bit rate only applies to compressed formats
- **container(Container::None)**: No container wrapping for raw MP3 output

## Sample output

```
Generating MP3 audio with 48 kbps bit rate...
Text: "Hello world! This demonstrates bit rate control for Deepgram text-to-speech."
Output file: output.mp3
File size: 4521 bytes
Bit rate: 48 kbps (MP3)
Temporary file cleaned up
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable

## Run the example

```bash
cargo run
```
