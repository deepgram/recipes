# Filler Words (Speech-to-Text v1)

Capture filler words like "uh", "um", and "mhm" in the transcription output instead of silently removing them.

## What it does

By default, Deepgram removes filler words from transcripts for cleaner output. Enabling filler words preserves these disfluencies, which is useful for conversation analysis, speaker profiling, and linguistic research where natural speech patterns matter.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `FillerWords` | `true` | Include filler words ("uh", "um", "mhm") in transcript |
| `Model` | `"nova-3"` | Transcription model |

## Example output

```
Yeah, um, as much as it's worth, uh, celebrating the 50th anniversary of
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
