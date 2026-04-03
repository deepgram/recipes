# Sentiment Analysis (Text Analysis v1)

Analyze sentiment (positive, negative, neutral) directly from plain text input using Deepgram's text analysis API.

## What it does

Detects sentiment shifts throughout the input text by segmenting it and assigning a sentiment label and confidence score to each segment. This works directly on text — no audio file is needed. Useful for customer feedback analysis, review processing, and content moderation.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Sentiment` | `true` | Enable sentiment analysis |
| `Language` | `"en"` | Input text language (English required) |

## Example output

```json
{
  "results": {
    "sentiments": {
      "segments": [
        { "text": "I absolutely love this product...", "sentiment": "positive", "confidence": 0.97 }
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
