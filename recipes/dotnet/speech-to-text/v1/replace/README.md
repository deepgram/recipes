# Find and Replace (Speech-to-Text v1)

Find and replace specific terms in the transcript output with custom substitutions.

## What it does

Enables Deepgram's find-and-replace feature which searches for terms or phrases in the transcript and replaces them with specified alternatives. Each replacement pair uses the format "original:replacement". This is useful for correcting brand names, normalizing terminology, or substituting words across the entire transcript.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Replace` | `["spacewalk:space walk", "anniversary:milestone"]` | List of "find:replace" pairs |
| `Model` | `"nova-3"` | Transcription model |

## Example output

```
Yeah, as much as it's worth celebrating the 50th milestone of
the space walk, it's also worth noting that we've come a long way...
```

## Prerequisites

- .NET 8.0+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `dotnet restore`

## Run

```bash
dotnet run
```
