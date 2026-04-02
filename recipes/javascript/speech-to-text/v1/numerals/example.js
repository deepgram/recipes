/**
 * Recipe: Numerals (Speech-to-Text v1)
 * ======================================
 * Demonstrates the `numerals` feature, which converts spoken numbers
 * into numeric digits in the transcript.
 *
 * Without numerals: "nineteen sixty five" stays as words.
 * With numerals:    spoken numbers are converted to digits like "1965".
 *
 * This is similar to what smart_format does for numbers, but numerals
 * gives explicit control over just the number formatting behavior.
 */

import { DeepgramClient } from "@deepgram/sdk";

const AUDIO_URL = "https://dpgr.am/spacewalk.wav";

async function main() {
  const client = new DeepgramClient();

  const response = await client.listen.v1.media.transcribeUrl({
    url: AUDIO_URL,
    model: "nova-3",
    punctuate: true,
    numerals: true,  // <-- THIS is the feature this recipe demonstrates.
                     // Converts spoken numbers to numeric digits.
  });

  const transcript = response.results?.channels?.[0]?.alternatives?.[0]?.transcript;
  if (transcript) {
    console.log(transcript);
  }
}

main().catch(console.error);
