/**
 * Recipe: Transcribe Audio from URL — v2 Model (Speech-to-Text v2)
 * ================================================================
 * Demonstrates pre-recorded transcription using the flux-general-en model
 * (Deepgram's v2 English model). Pre-recorded transcription uses the same
 * v1.media.transcribeUrl() method — the "v2" refers to the model name, not
 * a different API endpoint (unlike streaming, which has a distinct v2 WebSocket).
 *
 * See also: speech-to-text/v2/streaming for the v2 WebSocket API.
 * See also: speech-to-text/v1/transcribe-url for the v1 equivalent.
 */

import { DeepgramClient } from "@deepgram/sdk";

const AUDIO_URL = "https://dpgr.am/spacewalk.wav";

async function main() {
  const client = new DeepgramClient();

  // flux-general-en is the v2 English model — accessed via v1.media (same endpoint)
  const response = await client.listen.v1.media.transcribeUrl({
    url: AUDIO_URL,
    model: "flux-general-en",
    smart_format: true,
  });

  const transcript = response.results?.channels?.[0]?.alternatives?.[0]?.transcript;
  if (transcript) {
    console.log(transcript);
  }
}

main().catch(console.error);