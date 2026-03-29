# Select Voice Model (Text-to-Speech v1)

Choose from available aura-2 voice models to get different voice characteristics and qualities.

## What it does

This recipe demonstrates how to select specific voice models from Deepgram's aura-2 series. Different models provide distinct voice characteristics, allowing you to choose the most appropriate voice for your application's needs. The example uses aura-2-arcas-en to show the model selection parameter.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `model` | `aura-2-arcas-en` | Specific voice model from aura-2 series |
| `text` | Text string | Content to convert to speech |
| Available models | `aura-2-thalia-en`, `aura-2-arcas-en`, `aura-2-asteria-en` | Different voice characteristics |

## Example output

```
Audio saved: output.mp3 (43127 bytes, model: aura-2-arcas-en)
```

## Prerequisites

- Java 11+
- Maven 3.9+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `mvn install -DskipTests`

## Run

```bash
cd recipes/java/text-to-speech/v1/select-model
mvn exec:java -Dexec.mainClass="Example"
```