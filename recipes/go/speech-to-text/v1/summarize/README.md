# Summarization (Speech-to-Text v1)

Generate AI-powered summaries of transcribed audio content to quickly understand key points.

## What it does

Analyzes the full transcript and generates a concise summary highlighting the main points and key information. This feature helps you quickly understand long recordings without reading the entire transcript.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Summarize` | `"v2"` | Enables AI-powered summarization using version 2 |

## Example output

```
Summary: Discussion about celebrating the first all-female spacewalk team while looking forward to it becoming normal, honoring women who didn't have the same opportunities in the past.

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