/**
 * Recipe: Measurements (Speech-to-Text v1)
 * ==========================================
 * Demonstrates the `measurements` feature, which converts spoken
 * measurements to standard abbreviations in the transcript.
 *
 * Without measurements: "five feet six inches" stays as words.
 * With measurements:    spoken values are formatted as "5 ft 6 in" or
 *                       similar standard abbreviations.
 *
 * Useful for technical, medical, or scientific transcription where
 * consistent measurement formatting is important.
 */

import { DeepgramClient } from "@deepgram/sdk";

const AUDIO_URL = "https://dpgr.am/spacewalk.wav";

async function main() {
  const client = new DeepgramClient();

  const response = await client.listen.v1.media.transcribeUrl({
    url: AUDIO_URL,
    model: "nova-3",
    smart_format: true,
    measurements: true,  // <-- THIS is the feature this recipe demonstrates.
                         // Converts spoken measurements to standard abbreviations.
  });

  const transcript = response.results?.channels?.[0]?.alternatives?.[0]?.transcript;
  if (transcript) {
    console.log(transcript);
  }
}

main().catch(console.error);
