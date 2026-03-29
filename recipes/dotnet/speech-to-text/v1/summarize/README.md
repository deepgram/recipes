# Summarize

Automatically generates concise summaries of transcribed audio content using Deepgram's summarization feature.

The summarization feature analyzes the full transcript and extracts the key points, providing a condensed overview that captures the main themes and important information discussed in the audio.

## Key Parameters

- `Summarize = "v2"` - Enables summarization with version 2 of the algorithm (note: use string "v2", not boolean)

## Output

The summary is returned in the response at `response.Results.Summary.Short` and provides a brief overview of the content:

```
Summary: NASA astronaut Kjell Lindgren discusses the importance of spacewalks for International Space Station maintenance and scientific research.
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable to your Deepgram API key
- .NET 8.0 or later

## Run

```bash
dotnet run
```