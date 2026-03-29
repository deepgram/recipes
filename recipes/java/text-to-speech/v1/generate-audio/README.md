# Generate Audio to File (Text-to-Speech v1)

Converts text to speech audio and saves to a file using Deepgram's REST API.

## What it does

This recipe demonstrates basic text-to-speech conversion by generating audio from text and saving it to a local file. The `generate()` method returns an InputStream of audio bytes that can be written to disk or streamed to other destinations.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `aura-2-thalia-en` | Voice model selection (aura-2 series) |
| `text` | Text string | The text content to convert to speech |
| `encoding` | (optional) | Audio encoding format (default: mp3) |
| `container` | (optional) | Audio container format |

## Example output

```
Audio saved: output.mp3 (42876 bytes)
```

## Prerequisites

- Java 11+
- Maven 3.9+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `mvn install -DskipTests`

## Run

```bash
cd recipes/java/text-to-speech/v1/generate-audio
mvn exec:java -Dexec.mainClass="Example"
```