# Topic Detection (Audio Intelligence v1)

Automatically identifies key topics and themes discussed throughout the audio content using AI analysis. This feature extracts meaningful subjects and discussion points, making it ideal for meeting summaries, content categorization, research analysis, or podcast indexing.

## How it works

The topic detection feature analyzes the complete transcript to identify recurring themes, subjects, and discussion points. It segments the content and assigns relevant topics to each portion, helping you understand what was discussed and when.

## Key Parameters

- `Model = "nova-3"` — Required for topic detection (highest accuracy model)
- `Topics = true` — Enables AI-powered topic identification
- `SmartFormat = true` — Improves topic analysis with proper text formatting

## Example Output

```
Detected Topics:
Topic: space exploration
  Confidence: 0.91
  Context: NASA announces a successful spacewalk mission where astronauts completed repairs

Topic: technical operations
  Confidence: 0.87
  Context: The six-hour operation involved two crew members working outside the station

Topic: mission success
  Confidence: 0.83
  Context: The mission restored full power generation capability to the space station
```

Each detected topic includes:
- **Topic**: The identified theme or subject matter
- **Confidence**: Score from 0.0 to 1.0 indicating detection certainty
- **Context**: The relevant text segment where the topic was identified

## Prerequisites

- .NET 8.0 or later
- Deepgram API Key set as `DEEPGRAM_API_KEY` environment variable

## Run the Example

```bash
dotnet run
```