# Sentiment Analysis (Speech-to-Text v1)

Analyze the emotional tone and sentiment expressed in transcribed audio content.

## What it does

Examines the transcript to determine the emotional sentiment of different segments, classifying them as positive, negative, or neutral. Each segment receives a sentiment label and confidence score, helping you understand the speaker's emotional state throughout the audio.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Sentiment` | `true` | Enables sentiment analysis of transcript segments |

## Example output

```
Sentiment Analysis:
Text: "Yeah, as as much as it's worth celebrating, the first, spacewalk, with an all female team"
Sentiment: positive
Sentiment Score: 0.842

Text: "I think many of us are looking forward to it just being normal"
Sentiment: positive
Sentiment Score: 0.756

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