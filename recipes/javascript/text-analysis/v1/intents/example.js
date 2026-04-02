/**
 * Recipe: Intent Recognition (Text Analysis v1)
 * ================================================
 * Demonstrates the `intents` feature on Deepgram's text analysis API,
 * which detects speaker intents from plain text input.
 *
 * Text analysis (Read API) works directly on text — no audio required.
 * This is different from speech-to-text intent detection, which operates
 * on transcribed audio.
 */

import { DeepgramClient } from "@deepgram/sdk";

const TEXT =
  "I'd like to return this product and get a refund. " +
  "The item arrived damaged and I'm very disappointed with the quality. " +
  "Can you also update my shipping address for future orders?";

async function main() {
  const client = new DeepgramClient();

  const response = await client.read.v1.text.analyze({
    text: TEXT,
    language: "en",
    intents: true,  // <-- THIS enables intent recognition on plain text.
  });

  const intents = response.results?.intents;
  if (intents?.segments) {
    for (const segment of intents.segments) {
      console.log(`Text: ${segment.text}`);
      for (const intent of segment.intents) {
        console.log(`  Intent: ${intent.intent} (confidence: ${intent.confidence_score.toFixed(4)})`);
      }
    }
  }
}

main().catch(console.error);
