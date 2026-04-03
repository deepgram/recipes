# Intent Recognition (Text Analysis v1)

Detect speaker intents directly from plain text input using Deepgram's text analysis API.

## What it does

Analyzes plain text to recognize speaker intents throughout the input. The API segments the text and returns detected intents for each segment, such as "return product", "track order", or "escalate to manager". This works directly on text — no audio file is needed.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Intents` | `true` | Enable intent detection |
| `Language` | `"en"` | Input text language (English required) |

## Example output

```json
{
  "results": {
    "intents": {
      "segments": [
        { "text": "I'd like to return this product...", "intents": [{"intent": "Return product", "confidence_score": 0.95}] }
      ]
    }
  }
}
```

## Prerequisites

- .NET 8.0+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `dotnet restore`

## Run

```bash
dotnet run
```
