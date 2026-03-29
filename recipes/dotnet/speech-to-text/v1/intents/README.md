# Intents

Automatically detects speaker intents and purposes within transcribed audio content using Deepgram's intent recognition feature.

The intent detection feature analyzes the transcript to understand what speakers are trying to accomplish, communicate, or achieve. This is valuable for understanding conversation goals, customer service interactions, and meeting objectives.

## Key Parameters

- `Intents = true` - Enables automatic intent detection and analysis

## Output

Intents are returned in the response at `response.Results.Intents.Segments` as a list of segments, each containing detected intents with confidence scores:

```
Intents detected:
- Inform (confidence: 0.92)
- Educate (confidence: 0.84)
- Explain (confidence: 0.78)
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable to your Deepgram API key
- .NET 8.0 or later

## Run

```bash
dotnet run
```