# Intent Recognition (Text Analysis v1)

Detects speaker intents from plain text input using Deepgram's text analysis API. Unlike speech-to-text intent detection which works on audio, text analysis operates directly on text content — no audio file is needed.

## What it does

The intents feature analyzes text to identify what the speaker or writer is trying to accomplish. For example, a customer service message might contain intents like "return product", "request refund", or "update address". Each detected intent includes a confidence score.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `intents` | `true` | Enable intent recognition on the text |
| `language` | `"en"` | Language of the input text |

## Example output

```
Text: I'd like to return this product and get a refund.
  Intent: Return/Exchange Product (confidence: 0.95)
  Intent: Get Refund (confidence: 0.88)
Text: Can you also update my shipping address for future orders?
  Intent: Update Account Information (confidence: 0.91)
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```
