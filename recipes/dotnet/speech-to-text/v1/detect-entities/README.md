# Detect Entities

Automatically identifies and categorizes named entities such as people, places, organizations, and other proper nouns within transcribed audio using Deepgram's entity detection feature.

The entity detection feature recognizes specific named entities mentioned in conversations, making it useful for information extraction, content indexing, and understanding key subjects discussed in audio content.

## Key Parameters

- `DetectEntities = true` - Enables named entity recognition and categorization

## Output

Entities are returned in the response at `response.Results.Entities.Entities` with entity labels, values, and confidence scores:

```
Entities detected:
PERSON: Kjell Lindgren (confidence: 0.95)
ORG: NASA (confidence: 0.98)
FACILITY: International Space Station (confidence: 0.87)
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable to your Deepgram API key
- .NET 8.0 or later

## Run

```bash
dotnet run
```