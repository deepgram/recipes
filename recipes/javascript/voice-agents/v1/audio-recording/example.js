import { DeepgramClient } from "@deepgram/sdk";
import { writeFileSync } from "node:fs";

const AUDIO_URL = "https://dpgr.am/spacewalk.wav";

async function main() {
  const client = new DeepgramClient();
  const connection = await client.agent.v1.createConnection();
  const audioChunks = [];

  connection.on("message", (data) => {
    if (data.type === "SettingsApplied") console.log("Settings applied");
    else if (data.type === "ConversationText") {
      console.log(`${data.role === "assistant" ? "Agent" : "User"}: ${data.content}`);
    }
  });
  connection.on("error", (err) => console.error("Error:", err));

  connection.socket.addEventListener("message", (event) => {
    if (typeof event.data !== "string") audioChunks.push(Buffer.from(event.data));
  });

  connection.connect();
  await connection.waitForOpen();
  connection.sendSettings({
    type: "Settings",
    audio: {
      input: { encoding: "linear16", sample_rate: 24000 },
      output: { encoding: "linear16", sample_rate: 16000, container: "none" },
    },
    agent: {
      language: "en",
      listen: { provider: { type: "deepgram", model: "nova-3" } },
      think: {
        provider: { type: "open_ai", model: "gpt-4o-mini" },
        prompt: "You are a friendly AI assistant. Keep responses brief.",
      },
      speak: { provider: { type: "deepgram", model: "aura-2-thalia-en" } },
      greeting: "Hello! How can I help you today?",
    },
  });

  const resp = await fetch(AUDIO_URL);
  const buffer = Buffer.from(await resp.arrayBuffer());
  for (let i = 0; i < buffer.length; i += 4096) connection.sendMedia(buffer.subarray(i, i + 4096));

  await new Promise((resolve) => setTimeout(resolve, 15000));
  connection.close();

  const recorded = Buffer.concat(audioChunks);
  writeFileSync("session_audio.raw", recorded);
  console.log(`Recorded ${recorded.length} bytes of agent audio to session_audio.raw`);
}

main().catch(console.error);
