# Keywords (Speech-to-Text v1)

Improve transcription accuracy for specific important words by boosting their recognition priority.

## What it does

Increases the likelihood that specific important words will be correctly recognized in the transcript by applying a boost factor. This is particularly useful for technical terms, proper nouns, domain-specific vocabulary, or any words that are critical to understanding the content accurately.

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `Keywords` | `[]string{"spacewalk:2", "female:1.5", "opportunities:1.8"}` | List of keywords with boost factors (higher = more likely to be recognized) |

## Example output

```
Transcript with Keyword Boosting:
Yeah, as as much as it's worth celebrating, the first, spacewalk, with an all female team, I think many of us are looking forward to it just being normal and I think if it signifies anything, it is to honour the the women who came before us who were skilled and qualified, but didn't have the same opportunities that we have today.

Keywords boosted: spacewalk (2x), female (1.5x), opportunities (1.8x)
Higher boost values improve recognition accuracy for those specific words.
```

## Prerequisites

- Go 1.19+
- Set `DEEPGRAM_API_KEY` environment variable
- Install dependencies: `go mod download`

## Run

```bash
go run example.go
```