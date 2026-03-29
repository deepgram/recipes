# WebSocket Streaming TTS (Text-to-Speech v1)

Low-latency text-to-speech via WebSocket for real-time applications where immediate audio generation is critical.

## What it does

This recipe demonstrates WebSocket-based TTS that provides the lowest latency for audio generation. Unlike REST APIs that return complete audio files, WebSocket TTS streams audio chunks as they're generated. You can send text, receive audio data in real-time, and flush the connection to ensure all pending audio is delivered.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| WebSocket connection | TTS v1 | Real-time bidirectional communication |
| `sendText()` | Text message | Send text content for conversion |
| `sendFlush()` | Flush command | Force delivery of pending audio |
| `onSpeakV1Audio()` | Audio callback | Receive audio data chunks |

## Example output

```
Flushed — audio generated
Received 42876 bytes of audio
```

## Prerequisites

- Java 11+
- Maven 3.9+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `mvn install -DskipTests`

## Run

```bash
cd recipes/java/text-to-speech/v1/websocket-streaming
mvn exec:java -Dexec.mainClass="Example"
```