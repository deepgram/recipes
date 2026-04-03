# Sentiment Analysis (Text Analysis)

Analyzes sentiment (positive, negative, neutral) on plain text input using the Deepgram Read API. Returns both an overall average sentiment and per-segment breakdowns, without requiring any audio input.

## What this feature does

Sentiment analysis evaluates the emotional tone of text content, classifying segments as positive, negative, or neutral with confidence scores. This is useful for customer feedback analysis, social media monitoring, and content moderation where you already have text.

## Key parameters

- **sentiment=true**: Enables sentiment analysis on the text input
- **language=en**: Specifies the language of the input text

## Sample output

```
Average sentiment: positive (score: 0.65)
  [positive] I absolutely love this product! It exceeded all my expectations.
  [negative] However, the shipping was terrible and took three weeks to arrive.
  [positive] Overall, I'm satisfied with my purchase despite the delivery issues.
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable

## Run the example

```bash
cargo run
```
