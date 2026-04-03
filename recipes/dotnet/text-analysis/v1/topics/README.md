# Topic Detection (Text Analysis v1)

Identify key topics discussed in plain text input using Deepgram's text analysis API.

## What it does

Analyzes plain text to detect topics throughout the input. The API segments the text and returns identified topics with confidence scores for each segment. This works directly on text — no audio file is needed. Useful for content categorization, document tagging, and understanding what subjects are covered in text.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Topics` | `true` | Enable topic detection |
| `Language` | `"en"` | Input text language (English required) |

## Example output

```json
{
  "results": {
    "topics": {
      "segments": [
        { "text": "Deepgram is an AI speech company...", "topics": [{"topic": "Speech Recognition Technology", "confidence_score": 0.93}] }
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
