/**
 * STT v2 streaming with interim result assembly and final transcript reconstruction.
 */

import { DeepgramClient } from "@deepgram/sdk";

const AUDIO_URL = "https://dpgr.am/spacewalk.wav";

async function main() {
  const client = new DeepgramClient();
  const resp = await fetch(AUDIO_URL);
  const audioBuffer = Buffer.from(await resp.arrayBuffer());
  const finalTurns = new Map();

  const connection = await client.listen.v2.createConnection({
    model: "flux-general-en",
  });

  connection.on("message", (data) => {
    if (data.type !== "TurnInfo") return;
    const idx = data.turn_index;
    const event = data.event;
    if (["Update", "StartOfTurn", "EagerEndOfTurn", "TurnResumed"].includes(event)) {
      console.log(`[interim turn ${idx}] ${data.transcript}`);
    } else if (event === "EndOfTurn") {
      finalTurns.set(idx, data.transcript);
      console.log(`[final  turn ${idx}] ${data.transcript}`);
    }
  });

  connection.on("error", (err) => console.error("Error:", err));

  connection.connect();
  await connection.waitForOpen();

  const CHUNK_SIZE = 4096;
  for (let i = 0; i < audioBuffer.length; i += CHUNK_SIZE) {
    connection.sendMedia(audioBuffer.subarray(i, i + CHUNK_SIZE));
  }

  connection.sendCloseStream({ type: "CloseStream" });
  await new Promise((resolve) => setTimeout(resolve, 15000));
  connection.close();

  const keys = [...finalTurns.keys()].sort((a, b) => a - b);
  const transcript = keys.map((k) => finalTurns.get(k)).join(" ");
  console.log(`\n--- Assembled transcript ---\n${transcript}`);
}

main().catch(console.error);
