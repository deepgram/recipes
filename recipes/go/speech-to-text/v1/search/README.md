# Search (Speech-to-Text v1)

Search for specific terms and phrases within transcribed audio and get their timestamps and confidence scores.

## What it does

Searches the transcribed audio for specific keywords or phrases and returns their locations with precise timestamps. This is useful for finding mentions of important terms, names, or topics within long audio recordings without having to read through the entire transcript.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Search` | `[]string{"spacewalk", "female", "opportunities"}` | List of terms to search for in the transcript |

## Example output

```
Search Results:
Search term: spacewalk
  Found at: 12.4 - 13.2 seconds
  Confidence: 0.945

Search term: female  
  Found at: 15.6 - 16.1 seconds
  Confidence: 0.892

Search term: opportunities
  Found at: 45.2 - 46.8 seconds
  Confidence: 0.923

Full Transcript: Yeah, as as much as it's worth celebrating, the first, spacewalk, with an all female team, I think many of us are looking forward to it just being normal and I think if it signifies anything, it is to honour the the women who came before us who were skilled and qualified, but didn't have the same opportunities that we have today.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```