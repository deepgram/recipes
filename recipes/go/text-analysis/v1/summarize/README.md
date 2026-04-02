# Text Summarization (Text Analysis v1)

Generates a concise summary from plain text input using Deepgram's text analysis API. The summary condenses the input text into a brief overview of its key points.

## What it does

The summarize feature analyzes text content and produces a short summary that captures the main ideas. This is useful for processing long-form content, meeting notes, articles, or any text where a quick overview is needed.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `summarize` | `true` | Generate a summary of the input text |
| `language` | `"en"` | Language of the input text |

## Example output

```
Summary: Deepgram provides speech AI APIs including Nova-3 for transcription and Aura for text-to-speech, supporting real-time and pre-recorded audio across multiple languages.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```
