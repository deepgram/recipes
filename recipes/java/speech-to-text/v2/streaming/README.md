# Live Streaming Transcription (Speech-to-Text v2)

V2 WebSocket streaming with the flux-general-en model for turn-based transcription.

## What it does

Opens a WebSocket connection to Deepgram's v2 listen endpoint using the flux-general-en model. V2 provides turn-based transcription with turn info events instead of the interim/final results pattern used in v1. Each turn includes a transcript, turn index, and event type.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `flux-general-en` | V2 English-only high-accuracy model |

## Example output

```
[turn 0] Yeah, as you know, prior to the discovery.
[turn 1] It was a spacewalk.
```

## Prerequisites

- Java 11+
- Maven 3.9+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `mvn install -DskipTests`

## Run

```bash
cd recipes/java/speech-to-text/v2/streaming
mvn exec:java -Dexec.mainClass="Example"
```
