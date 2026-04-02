# Dictation Mode (Speech-to-Text v1)

Interprets spoken punctuation commands as literal punctuation marks in the transcript. When a speaker says "period", "comma", or "question mark", those words are replaced with their corresponding punctuation symbols.

This is ideal for hands-free document dictation workflows where the speaker explicitly controls punctuation placement, rather than relying on Deepgram's automatic punctuation inference.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Dictation` | `true` | Enable dictation mode — spoken punctuation becomes literal punctuation |
| `Model` | `"nova-3"` | Transcription model |
| `SmartFormat` | `true` | Recommended alongside dictation for clean formatting |

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
