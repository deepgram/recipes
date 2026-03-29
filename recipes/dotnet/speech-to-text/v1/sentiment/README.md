# Sentiment

Analyzes the emotional tone and sentiment (positive, negative, neutral) of transcribed audio segments using Deepgram's sentiment analysis feature.

The sentiment analysis feature evaluates the emotional context of speech, helping understand the speaker's mood, attitude, and emotional state throughout the conversation. This is valuable for customer service analysis, meeting feedback, and content evaluation.

## Key Parameters

- `Sentiment = true` - Enables sentiment analysis on transcript segments

## Output

Sentiment analysis is returned in the response at `response.Results.Sentiments.Segments` with sentiment labels, text, and confidence scores:

```
Sentiment analysis:
[Neutral] NASA astronaut Kjell Lindgren talks about spacewalks (confidence: 0.87)
[Positive] These activities are crucial for maintaining the station (confidence: 0.92)
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable to your Deepgram API key
- .NET 8.0 or later

## Run

```bash
dotnet run
```