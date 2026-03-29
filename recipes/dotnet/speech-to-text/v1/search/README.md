# Search

Finds specific words or phrases within audio content with precise timestamps and confidence scores using Deepgram's search feature.

The search feature allows you to locate exact instances of specified terms in the transcript, providing timing information and confidence scores for each match. This is useful for content indexing, keyword spotting, and finding specific mentions in long audio recordings.

## Key Parameters

- `Search = new List<string> { "spacewalk", "NASA" }` - Enables search for specified words or phrases

## Output

Search results are returned in the response at `response.Results.Channels[0].Search` with timing and confidence information:

```
Search results:
Found 'NASA' at 1.23s-1.67s (confidence: 0.95)
Found 'spacewalk' at 4.52s-5.18s (confidence: 0.92)
Found 'spacewalk' at 8.91s-9.47s (confidence: 0.88)
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable to your Deepgram API key
- .NET 8.0 or later

## Run

```bash
dotnet run
```