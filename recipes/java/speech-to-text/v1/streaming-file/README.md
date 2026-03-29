# Stream Audio File for Transcription (Speech-to-Text v1)

Stream a local audio file over WebSocket for real-time transcription, simulating a live audio source.

## What it does

Downloads a demo audio file and streams it in chunks over a WebSocket connection. The server processes each chunk and returns final transcription results. This demonstrates how to use the WebSocket API when your audio source is a file rather than a microphone.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `NOVA3` | Highest-accuracy transcription model |
| `smartFormat` | `true` | Formats numbers, dates, currencies |

## Example output

```
Streaming 3145728 bytes
Yeah, as you know, for prior to prior to the discovery. It was space walk.
```

## Prerequisites

- Java 11+
- Maven 3.9+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `mvn install -DskipTests`

## Run

```bash
cd recipes/java/speech-to-text/v1/streaming-file
mvn exec:java -Dexec.mainClass="Example"
```
