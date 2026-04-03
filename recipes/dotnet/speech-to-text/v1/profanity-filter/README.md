# Profanity Filter (Speech-to-Text v1)

Mask profanity in the transcription output by replacing profane words with clean alternatives or removing them entirely.

## What it does

Enables Deepgram's profanity filter which detects recognized profanity and either replaces it with the nearest non-profane word or removes it from the transcript completely. This is useful for content moderation, broadcasting compliance, and customer-facing applications.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `ProfanityFilter` | `true` | Mask or remove profanity from the transcript |
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
