/**
 * Recipe: Find and Replace (Speech-to-Text v1)
 * ===============================================
 * Demonstrates the `replace` feature, which finds and replaces specific
 * terms in the transcript output.
 *
 * Without replace: transcript contains the original spoken terms.
 * With replace:    specified terms are substituted with replacements in
 *                  the final transcript.
 *
 * Format: "original:replacement" — each entry replaces one term.
 * Useful for normalizing terminology, correcting consistent misrecognitions,
 * or anonymizing specific words.
 */

import { DeepgramClient } from "@deepgram/sdk";

const AUDIO_URL = "https://dpgr.am/spacewalk.wav";

async function main() {
  const client = new DeepgramClient();

  const response = await client.listen.v1.media.transcribeUrl({
    url: AUDIO_URL,
    model: "nova-3",
    smart_format: true,
    replace: ["capsule:spacecraft"],  // <-- THIS is the feature this recipe demonstrates.
                                      // Replaces "capsule" with "spacecraft" in the transcript.
    // Format: "original:replacement" per entry
  });

  const transcript = response.results?.channels?.[0]?.alternatives?.[0]?.transcript;
  if (transcript) {
    console.log(transcript);
  }
}

main().catch(console.error);
