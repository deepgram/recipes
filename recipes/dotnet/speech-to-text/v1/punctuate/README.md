# Punctuate (Speech-to-Text v1)

Adds basic punctuation and capitalization to speech transcripts without other formatting changes. This creates more readable text by inserting periods, commas, question marks, and proper sentence capitalization.

## Feature

The `Punctuate` parameter enables punctuation-only formatting:
- Adds periods, commas, question marks, exclamation marks
- Capitalizes sentence beginnings and proper nouns
- Does NOT format numbers, dates, or currencies (use smart-format for that)

## Key Parameters

- `Punctuate: true` - Enables basic punctuation and capitalization

## Example Output

Without punctuation:
```
yeah as much as its worth i mean you know from a scientific standpoint
```

With punctuation:
```
Yeah, as much as it's worth, I mean, you know, from a scientific standpoint.
```

## Prerequisites

- .NET 8.0 or later
- Deepgram API key set in `DEEPGRAM_API_KEY` environment variable

## Run

```bash
dotnet run
```