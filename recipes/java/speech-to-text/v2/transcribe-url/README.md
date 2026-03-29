# Transcribe Audio from URL (Speech-to-Text v2)

Use the v2 API with the flux-general-en model for high-accuracy English transcription.

## What it does

Sends a URL to the v1 REST endpoint but specifies the `flux-general-en` model, which is the v2 English-only high-accuracy model. This provides enhanced accuracy for English audio content.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `flux-general-en` | V2 English-only high-accuracy model |
| `smartFormat` | `true` | Formats numbers, dates, currencies |

## Example output

```
Yeah, as you know, prior to the discovery of the relevant, it was a spacewalk.
```

## Prerequisites

- Java 11+
- Maven 3.9+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `mvn install -DskipTests`

## Run

```bash
cd recipes/java/speech-to-text/v2/transcribe-url
mvn exec:java -Dexec.mainClass="Example"
```
