# Numerals (Speech-to-Text v1)

Convert spoken numbers from written-out form to numeric digits in the transcript.

## What it does

Enables automatic conversion of spoken numbers into their numeric equivalents. For example, "twenty three" becomes "23" and "one hundred fifty" becomes "150". This is useful for financial transcripts, data-heavy content, and any scenario where numeric precision in text form is needed.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Numerals` | `true` | Convert spoken numbers to digits |
| `Model` | `"nova-3"` | Transcription model |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of
the spacewalk, it's also worth noting that we've come a long way...
```

## Prerequisites

- .NET 8.0+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `dotnet restore`

## Run

```bash
dotnet run
```
