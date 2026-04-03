# Text Summarization (Text Analysis v1)

Generate a concise summary from plain text input using Deepgram's text analysis API.

## What it does

Analyzes plain text and produces a brief summary of its content. This works directly on text — no audio file is needed. Useful for condensing long documents, articles, meeting notes, or any text content into a quick overview.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Summarize` | `true` | Enable text summarization |
| `Language` | `"en"` | Input text language (English required) |

## Example output

```json
{
  "results": {
    "summary": {
      "text": "Deepgram provides speech recognition and text-to-speech APIs with the Nova-3 model, along with audio intelligence features accessible through multiple language SDKs."
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
