# Paragraphs (Speech-to-Text v1)

Organize transcripts into logical paragraphs using Deepgram's paragraph segmentation feature.

## What it does

This feature automatically segments long-form speech into coherent paragraphs based on natural speech patterns, pauses, and topic changes. Each paragraph contains structured sentences, making the transcript easier to read and process for document creation or analysis.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `paragraphs` | `true` | Enables automatic paragraph segmentation of transcripts |
| `punctuate` | `true` | Required dependency for paragraph feature to work properly |

## Example output

```
Paragraphs:
Paragraph 1: That's one small step for man, one giant leap for mankind.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```