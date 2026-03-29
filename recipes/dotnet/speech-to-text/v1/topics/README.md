# Topics

Automatically identifies and categorizes topics discussed in transcribed audio content using Deepgram's topic detection feature.

The topic detection feature analyzes the transcript to identify different subjects and themes being discussed, providing confidence scores for each detected topic. This is useful for content categorization, meeting summaries, and understanding the main themes in conversations.

## Key Parameters

- `Topics = true` - Enables automatic topic detection and categorization

## Output

Topics are returned in the response at `response.Results.Topics.Segments` as a list of segments, each containing detected topics with confidence scores:

```
Topics detected:
- Space exploration (confidence: 0.95)
- NASA (confidence: 0.87)
- International Space Station (confidence: 0.82)
- Scientific research (confidence: 0.73)
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable to your Deepgram API key
- .NET 8.0 or later

## Run

```bash
dotnet run
```