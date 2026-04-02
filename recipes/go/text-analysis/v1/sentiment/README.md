# Sentiment Analysis (Text Analysis v1)

Analyzes sentiment (positive, negative, or neutral) on plain text input using Deepgram's text analysis API. Each text segment receives a sentiment label and confidence score, plus an overall average sentiment.

## What it does

The sentiment feature evaluates the emotional tone of text content. It breaks the text into segments and classifies each as positive, negative, or neutral with a confidence score. An overall average sentiment is also provided.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `sentiment` | `true` | Enable sentiment analysis on the text |
| `language` | `"en"` | Language of the input text |

## Example output

```
Average: positive (0.65)
[positive] (0.93) I absolutely love this product! It exceeded all my expectations.
[negative] (0.85) However, the shipping was terribly slow and the packaging was damaged.
[positive] (0.72) Overall, the customer service team was helpful and resolved my concerns.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```
