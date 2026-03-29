# Transcribe Local Audio File (Speech-to-Text v1)

Read a local audio file and send it to Deepgram for transcription.

## What it does

Reads audio file bytes from disk and sends them directly to Deepgram's pre-recorded
transcription endpoint. The response structure is identical to URL-based transcription —
only the input method differs.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Model` | `"nova-3"` | Transcription model — nova-3 is the most accurate |
| `SmartFormat` | `true` | Automatically format numbers, currencies, dates |

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
