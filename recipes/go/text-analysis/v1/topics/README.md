# Topic Detection (Text Analysis v1)

Identifies topics discussed in plain text input using Deepgram's text analysis API. Each text segment is annotated with detected topics and their confidence scores.

## What it does

The topics feature analyzes text content to identify the subjects being discussed. It breaks the text into segments and assigns topic labels to each, making it useful for content categorization, tagging, and organization.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `topics` | `true` | Enable topic detection on the text |
| `language` | `"en"` | Language of the input text |

## Example output

```
Text: The stock market saw significant gains today as technology companies reported strong quarterly earnings.
  Topic: Finance (confidence: 0.92)
  Topic: Technology (confidence: 0.85)
Text: In sports news, the championship finals drew record viewership numbers across streaming platforms.
  Topic: Sports (confidence: 0.94)
  Topic: Media (confidence: 0.78)
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```
