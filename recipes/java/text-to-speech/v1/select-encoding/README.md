# Select Audio Encoding (Text-to-Speech v1)

Choose output audio encoding format to match your application's specific requirements and use cases.

## What it does

This recipe demonstrates how to specify different audio encodings for TTS output. Different encodings are optimized for various scenarios: linear16 for high-quality uncompressed audio, mp3 for file storage, opus for streaming, flac for lossless compression, aac for mobile apps, and mulaw for telephony systems.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `encoding` | `linear16` | Raw PCM audio encoding |
| `container` | `wav` | Audio container format (wav, none) |
| `model` | `aura-2-thalia-en` | Voice model selection |
| Available encodings | `linear16`, `mp3`, `opus`, `flac`, `aac`, `mulaw` | Different compression/quality options |

## Example output

```
Audio saved: output.wav (96144 bytes, encoding: linear16)
```

## Prerequisites

- Java 11+
- Maven 3.9+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `mvn install -DskipTests`

## Run

```bash
cd recipes/java/text-to-speech/v1/select-encoding
mvn exec:java -Dexec.mainClass="Example"
```