# Smart Format (Speech-to-Text v1)

Automatically format transcription output with proper numbers, dates, currencies, and addresses.

## What it does

Enables Deepgram's smart formatting which converts spoken forms into written forms.
For example, "twenty three dollars" becomes "$23", dates are formatted properly,
and addresses are structured. This includes punctuation automatically.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `SmartFormat` | `true` | Enable automatic formatting of numbers, dates, currencies |
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
