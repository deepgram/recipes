/**
 * Recipe: Topic Detection (Text Analysis v1)
 * =============================================
 * Demonstrates the `topics` feature on Deepgram's text analysis API,
 * which identifies topics discussed in plain text input.
 *
 * Text analysis (Read API) works directly on text — no audio required.
 * Returns per-segment topic lists with confidence scores.
 */

import { DeepgramClient } from "@deepgram/sdk";

const TEXT =
  "The new electric vehicle from Tesla features a range of 400 miles " +
  "and uses a revolutionary battery technology. Meanwhile, SpaceX " +
  "successfully launched another batch of Starlink satellites into orbit. " +
  "In healthcare news, a new mRNA vaccine shows promising results in " +
  "early clinical trials for treating certain types of cancer.";

async function main() {
  const client = new DeepgramClient();

  const response = await client.read.v1.text.analyze({
    text: TEXT,
    language: "en",
    topics: true,  // <-- THIS enables topic detection on plain text.
  });

  const topics = response.results?.topics;
  if (topics?.segments) {
    for (const segment of topics.segments) {
      console.log(`Text: ${segment.text}`);
      for (const topic of segment.topics) {
        console.log(`  Topic: ${topic.topic} (confidence: ${topic.confidence_score.toFixed(4)})`);
      }
    }
  }
}

main().catch(console.error);
