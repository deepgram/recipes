/**
 * Recipe: Profanity Filter (Speech-to-Text v1)
 * ===============================================
 * Demonstrates the `profanity_filter` feature, which masks profanity
 * in the transcript output.
 *
 * Without profanity_filter: profanity appears as spoken.
 * With profanity_filter:    profane words are replaced with asterisks
 *                           or similar masking characters.
 *
 * Useful for content moderation, broadcast compliance, or any context
 * where clean language output is required.
 */

import { DeepgramClient } from "@deepgram/sdk";

const AUDIO_URL = "https://dpgr.am/spacewalk.wav";

async function main() {
  const client = new DeepgramClient();

  const response = await client.listen.v1.media.transcribeUrl({
    url: AUDIO_URL,
    model: "nova-3",
    smart_format: true,
    profanity_filter: true,  // <-- THIS is the feature this recipe demonstrates.
                              // Masks profanity in the transcript output.
  });

  const transcript = response.results?.channels?.[0]?.alternatives?.[0]?.transcript;
  if (transcript) {
    console.log(transcript);
  }
}

main().catch(console.error);
