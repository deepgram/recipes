# Intent Recognition (Speech-to-Text v1)

Detect and classify user intentions and purposes within transcribed audio content.

## What it does

Analyzes the transcript to identify the speaker's intentions, goals, or purposes behind their words. This helps understand what the speaker is trying to accomplish, whether they're making requests, expressing opinions, giving instructions, or pursuing other goals.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Intents` | `true` | Enables intent recognition and classification |

## Example output

```
Intent Analysis:
Text: "Yeah, as as much as it's worth celebrating, the first, spacewalk, with an all female team"
Intents:
  - Express opinion
  - Acknowledge achievement

Text: "I think many of us are looking forward to it just being normal"
Intents:
  - Express hope
  - Share perspective

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