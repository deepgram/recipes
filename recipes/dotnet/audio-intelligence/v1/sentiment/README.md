# Sentiment Analysis (Audio Intelligence v1)

Analyzes the emotional tone of speech segments, classifying each portion as positive, negative, or neutral with confidence scores. This feature is valuable for customer service analysis, meeting insights, content moderation, or understanding audience reactions to presentations.

## How it works

The sentiment analysis feature processes the transcript and evaluates the emotional context of the spoken words, providing segment-level sentiment classification along with confidence scores to help understand the speaker's emotional state throughout the audio.

## Key Parameters

- `Model = "nova-3"` — Required for sentiment analysis (highest accuracy model)
- `Sentiment = true` — Enables sentiment analysis for each speech segment
- `SmartFormat = true` — Improves analysis quality with proper text formatting

## Example Output

```
Sentiment Analysis:
[positive] NASA announces a successful spacewalk mission where astronauts completed repairs.
  Confidence: 0.85

[neutral] The six-hour operation involved two crew members working outside the station.
  Confidence: 0.92

[positive] The mission restored full power generation capability to the space station.
  Confidence: 0.78
```

Each segment shows:
- **Sentiment**: positive, negative, or neutral classification
- **Text**: The spoken content being analyzed
- **Confidence**: Score from 0.0 to 1.0 indicating analysis certainty

## Prerequisites

- .NET 8.0 or later
- Deepgram API Key set as `DEEPGRAM_API_KEY` environment variable

## Run the Example

```bash
dotnet run
```