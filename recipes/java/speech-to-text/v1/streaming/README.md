# Live Streaming Transcription (Speech-to-Text v1)

Real-time transcription via WebSocket — audio is streamed in chunks and transcripts are returned as they are recognized.

## What it does

Opens a WebSocket connection to Deepgram's v1 listen endpoint and streams audio data in chunks. The server returns interim (partial) and final transcription results as audio is received. This recipe downloads a demo file and streams it to simulate a live audio source.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `NOVA3` | Highest-accuracy transcription model |
| `smartFormat` | `true` | Formats numbers, dates, currencies |
| `interimResults` | `true` | Returns partial results as audio streams |

## Example output

```
Yeah, as you know, for prior to prior to the discovery. It was space walk.
```

## Prerequisites

- Java 11+
- Maven 3.9+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `mvn install -DskipTests`

## Run

```bash
cd recipes/java/speech-to-text/v1/streaming
mvn exec:java -Dexec.mainClass="Example"
```
