/**
 * Recipe: Sentiment Analysis (Text Analysis v1)
 * ================================================
 * Demonstrates the `sentiment` feature on Deepgram's text analysis API,
 * which analyzes sentiment (positive, negative, neutral) on plain text.
 *
 * Text analysis (Read API) works directly on text — no audio required.
 * Returns both an overall average sentiment and per-segment breakdowns.
 */

import { DeepgramClient } from "@deepgram/sdk";

const TEXT =
  "I absolutely love this product! It exceeded all my expectations. " +
  "However, the shipping was terrible and took three weeks to arrive. " +
  "Overall, I'm satisfied with my purchase despite the delivery issues.";

async function main() {
  const client = new DeepgramClient();

  const response = await client.read.v1.text.analyze({
    text: TEXT,
    language: "en",
    sentiment: true,  // <-- THIS enables sentiment analysis on plain text.
  });

  const sentiments = response.results?.sentiments;
  if (sentiments) {
    const avg = sentiments.average;
    console.log(`Average sentiment: ${avg.sentiment} (score: ${avg.sentiment_score.toFixed(4)})`);
    for (const segment of sentiments.segments) {
      console.log(`  [${segment.sentiment}] ${segment.text}`);
    }
  }
}

main().catch(console.error);
