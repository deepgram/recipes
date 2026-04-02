/**
 * Recipe: Key Term Prompting (Speech-to-Text v1)
 * =================================================
 * Demonstrates the `keyterm` feature, which boosts recognition of specific
 * key terms when using the Nova-3 model.
 *
 * Without keyterm: the model uses default vocabulary recognition.
 * With keyterm:    specified terms get improved recognition accuracy,
 *                  especially useful for domain-specific vocabulary.
 *
 * keyterm is the Nova-3 replacement for the older keywords feature.
 * Pass an array of strings — no boost values needed (unlike keywords).
 */

import { DeepgramClient } from "@deepgram/sdk";

const AUDIO_URL = "https://dpgr.am/spacewalk.wav";

async function main() {
  const client = new DeepgramClient();

  const response = await client.listen.v1.media.transcribeUrl({
    url: AUDIO_URL,
    model: "nova-3",
    smart_format: true,
    keyterm: ["spacewalk", "Leonov", "capsule"],  // <-- THIS is the feature this recipe demonstrates.
                                                    // Boosts recognition of these terms on Nova-3.
  });

  const transcript = response.results?.channels?.[0]?.alternatives?.[0]?.transcript;
  if (transcript) {
    console.log(transcript);
  }
}

main().catch(console.error);
