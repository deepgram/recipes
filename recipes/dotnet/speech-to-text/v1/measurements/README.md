# Measurements (Speech-to-Text v1)

Convert spoken measurements to their standard abbreviations in the transcript output.

## What it does

Enables automatic conversion of spoken measurement terms into their standard written abbreviations. For example, "five milligrams" becomes "5 mg", "three kilometers per hour" becomes "3 km/h". This is useful for scientific, medical, and engineering transcripts where precise measurement notation matters.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Measurements` | `true` | Convert spoken measurements to abbreviations |
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
