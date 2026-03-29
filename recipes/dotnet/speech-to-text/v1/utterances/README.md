# Utterances (Speech-to-Text v1)

Segments transcripts into time-stamped utterances, providing precise timing information for each speech segment. This is essential for creating captions, analyzing speech patterns, or building time-synced applications.

## Feature

The `Utterances` parameter enables time-stamped segmentation:
- Splits transcript into natural speech segments
- Provides start and end timestamps for each utterance
- Identifies natural pauses and speech boundaries
- Useful for captions, subtitles, and time-based analysis

## Key Parameters

- `Utterances: true` - Enables utterance segmentation with timing

## Response Structure

When `Utterances=true`, the response includes utterance data at:
```
response.Results.Utterances
```

Each utterance contains:
- `Start` - Start time in seconds
- `End` - End time in seconds  
- `Transcript` - Text content of the utterance
- `Speaker` - Speaker ID (when combined with diarization)

## Example Output

Without utterances:
```
Complete transcript as one continuous block of text.
```

With utterances:
```
[0.5s - 3.2s] Yeah, as much as it's worth, I mean, you know.
[3.8s - 7.1s] From a scientific standpoint, it's fascinating.
[7.5s - 11.2s] The data we're collecting here is unprecedented.
```

## Prerequisites

- .NET 8.0 or later
- Deepgram API key set in `DEEPGRAM_API_KEY` environment variable

## Run

```bash
dotnet run
```