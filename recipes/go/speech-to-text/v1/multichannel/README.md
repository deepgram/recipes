# Multichannel Transcription (Speech-to-Text v1)

Transcribe audio with multiple channels, processing each channel separately to get individual transcripts.

## What it does

Enables multichannel processing to transcribe audio files where different speakers or audio sources are recorded on separate channels. This is useful for stereo recordings, conference calls, or multi-track audio where you need separate transcripts for each channel.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Multichannel` | `true` | Processes each audio channel separately |

## Example output

```
Multichannel transcription results:
Channel 0:
  Transcript: Yeah, as as much as it's worth celebrating, the first, spacewalk, with an all female team, I think many of us are looking forward to it just being normal and I think if it signifies anything, it is to honour the the women who came before us who were skilled and qualified, but didn't have the same opportunities that we have today.
Channel 1:
  Transcript: (Empty or different content based on audio channel separation)
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```