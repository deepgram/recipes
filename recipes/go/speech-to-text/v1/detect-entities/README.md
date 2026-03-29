# Entity Detection (Speech-to-Text v1)

Identify and extract named entities such as people, places, organizations, and other important objects from transcribed audio.

## What it does

Analyzes the transcript to automatically identify and classify named entities like person names, locations, organizations, dates, and other significant objects mentioned in the audio. This helps extract structured information from unstructured speech content.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `DetectEntities` | `true` | Enables named entity recognition and extraction |

## Example output

```
Detected Entities:
Entity: spacewalk
Type: EVENT
Confidence: 0.892

Entity: female team
Type: GROUP
Confidence: 0.756

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