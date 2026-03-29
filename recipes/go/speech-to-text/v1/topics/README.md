# Topic Detection (Speech-to-Text v1)

Identify and extract key topics and themes from transcribed audio content.

## What it does

Analyzes the transcript to automatically identify relevant topics and themes discussed in the audio. Each segment of text is analyzed to determine what subjects are being discussed, helping you quickly understand the content structure and main themes.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Topics` | `true` | Enables topic detection and classification |

## Example output

```
Topic Analysis:
Text: "Yeah, as as much as it's worth celebrating, the first, spacewalk, with an all female team"
Topics:
  - Space exploration
  - Gender equality
  - Achievements

Text: "I think many of us are looking forward to it just being normal"
Topics:
  - Social progress
  - Normalization

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