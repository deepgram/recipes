# Keywords

Improves recognition accuracy for specific words by applying boost multipliers using Deepgram's keyword enhancement feature.

The keywords feature allows you to specify important terms that should receive enhanced recognition accuracy. This is particularly useful for proper nouns, technical terminology, brand names, and domain-specific vocabulary that might otherwise be misrecognized.

## Key Parameters

- `Keywords = new List<string> { "Deepgram:2", "spacewalk:1.5" }` - Enables keyword boosting
- Format: `"word:boost"` where boost is a float multiplier (typically 1.0-3.0)
- Higher boost values increase recognition confidence for specified words

## Output

The enhanced transcript shows improved accuracy for the specified keywords:

```
Enhanced transcript with keyword boosting:
NASA astronaut Kjell Lindgren talks about spacewalks and how Deepgram technology helps transcribe space communications.
```

The keywords improve overall transcript quality rather than appearing in a separate section.

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable to your Deepgram API key
- .NET 8.0 or later

## Run

```bash
dotnet run
```