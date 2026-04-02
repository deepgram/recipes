/**
 * Recipe: Filler Words (Speech-to-Text v1)
 * ==========================================
 * Demonstrates the `filler_words` feature, which captures filler words
 * like "uh", "um", "mhm", and "uh huh" in the transcript.
 *
 * Without filler_words: fillers are omitted from the transcript.
 * With filler_words:    fillers appear in the transcript as spoken,
 *                       useful for conversation analysis and verbatim records.
 *
 * Note: smart_format typically removes fillers, so disable it or use
 * filler_words=true to retain them.
 */

import { DeepgramClient } from "@deepgram/sdk";

const AUDIO_URL = "https://dpgr.am/spacewalk.wav";

async function main() {
  const client = new DeepgramClient();

  const response = await client.listen.v1.media.transcribeUrl({
    url: AUDIO_URL,
    model: "nova-3",
    filler_words: true,  // <-- THIS is the feature this recipe demonstrates.
                         // Includes "uh", "um", etc. in the transcript.
    punctuate: true,
  });

  const transcript = response.results?.channels?.[0]?.alternatives?.[0]?.transcript;
  if (transcript) {
    console.log(transcript);
  }
}

main().catch(console.error);
