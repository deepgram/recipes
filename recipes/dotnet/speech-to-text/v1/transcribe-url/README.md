# Transcribe Audio from URL (Speech-to-Text v1)

Send a URL pointing to a hosted audio file for transcription using the Deepgram REST API.

## What it does

Makes a single REST API call to Deepgram's pre-recorded transcription endpoint with an audio URL.
Deepgram downloads the audio, transcribes it, and returns the full result including the transcript text,
confidence scores, and word-level timing.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Model` | `"nova-3"` | Transcription model — nova-3 is the most accurate for most use cases |
| `SmartFormat` | `true` | Automatically format numbers, currencies, dates, and addresses |

## Example output

```
Yeah, as much as it's worth celebrating the 50th anniversary of
the spacewalk, it's also worth noting that we've come a long way
since then...
```

## Prerequisites

- .NET 8.0+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `dotnet restore`

## Run

```bash
dotnet run
```
