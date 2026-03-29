# Text Summarization (Audio Intelligence v1)

Generates a concise AI-powered summary of spoken content, extracting key points and themes from the transcript. This feature is ideal for meeting notes, lecture summaries, podcast analysis, or any scenario where you need to quickly understand the main topics discussed in audio content.

## How it works

The summarization feature uses advanced natural language processing to analyze the complete transcript and identify the most important information, condensing it into a short, readable summary that captures the essence of the spoken content.

## Key Parameters

- `Model = "nova-3"` — Required for summarization (highest accuracy model)
- `Summarize = "v2"` — Enables v2 summarization (string value, not boolean)
- `SmartFormat = true` — Improves summary quality with proper formatting

## Example Output

```
Summary:
NASA announces a successful spacewalk mission where astronauts completed repairs to the International Space Station's solar panel array. The six-hour operation involved two crew members working outside the station to replace damaged components and restore full power generation capability.
```

Note: Summary may be empty for very short audio files (under ~30 seconds). Longer content produces more meaningful summaries.

## Prerequisites

- .NET 8.0 or later
- Deepgram API Key set as `DEEPGRAM_API_KEY` environment variable

## Run the Example

```bash
dotnet run
```