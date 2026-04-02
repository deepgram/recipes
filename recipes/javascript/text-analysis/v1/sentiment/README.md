# Sentiment Analysis — Text Analysis v1

Sentiment analysis on the Read API detects positive, negative, and neutral sentiment from plain text input — no audio required. The response includes an overall average sentiment score and per-segment breakdowns.

This is useful for analyzing customer feedback, reviews, support tickets, or any text where understanding emotional tone matters.

## Key parameters

| Parameter | Type | Description |
|---|---|---|
| `sentiment` | `boolean` | Enable sentiment analysis |
| `language` | `string` | Language of the text (e.g., `en`) |

## Sample output

```
Average sentiment: positive (score: 0.6234)
  [positive] I absolutely love this product! It exceeded all my expectations.
  [negative] However, the shipping was terrible and took three weeks to arrive.
  [positive] Overall, I'm satisfied with my purchase despite the delivery issues.
```

## Prerequisites

- Node.js 20+
- A [Deepgram API key](https://console.deepgram.com/signup?jump=keys)

## Run

```bash
export DEEPGRAM_API_KEY="your-api-key"
npm install
node example.js
```
