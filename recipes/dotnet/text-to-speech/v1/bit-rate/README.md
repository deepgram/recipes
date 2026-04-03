# Bit Rate Control (Text-to-Speech v1)

Control the output audio bit rate for compressed encodings like MP3 in Deepgram's TTS API.

## What it does

Sets the bit rate for compressed audio output. Lower bit rates produce smaller files suitable for bandwidth-constrained scenarios, while higher bit rates yield better audio quality. This parameter only affects compressed encodings (mp3, opus) — it has no effect on uncompressed formats like linear16.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `BitRate` | `"48000"` | Output bit rate in bits per second |
| `Encoding` | `"mp3"` | Compressed encoding format |
| `Model` | `"aura-2-thalia-en"` | TTS voice model |

## Example output

```
Audio saved: 12345 bytes (48kbps mp3)
```

## Prerequisites

- .NET 8.0+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `dotnet restore`

## Run

```bash
dotnet run
```
