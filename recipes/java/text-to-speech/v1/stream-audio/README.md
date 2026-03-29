# Stream Audio Response (Text-to-Speech v1)

Streams TTS audio as it generates via REST API, reading chunks incrementally for low-latency playback.

## What it does

This recipe demonstrates how to stream audio data as it's generated rather than waiting for the entire response. It reads the audio InputStream in chunks, allowing you to process or play audio data progressively. This approach is useful for applications requiring immediate audio playback or real-time processing.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `encoding` | `linear16` | Raw audio encoding ideal for streaming |
| `container` | `none` | No container wrapper for direct audio data |
| `model` | `aura-2-thalia-en` | Voice model selection |
| `text` | Text string | Content to convert to speech |

## Example output

```
Received 12 chunks, 48576 bytes total
```

## Prerequisites

- Java 11+
- Maven 3.9+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `mvn install -DskipTests`

## Run

```bash
cd recipes/java/text-to-speech/v1/stream-audio
mvn exec:java -Dexec.mainClass="Example"
```