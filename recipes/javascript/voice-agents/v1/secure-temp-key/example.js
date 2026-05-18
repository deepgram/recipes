/**
 * Recipe: Secure Temporary Key for Voice Agent (Voice Agents v1)
 * ================================================================
 * Mint a short-lived JWT with auth.v1.tokens.grant(), then connect
 * to the Voice Agent API using only that token.  The main API key
 * never reaches the client — this is the recommended browser pattern.
 */

import { DeepgramClient } from "@deepgram/sdk";

const AUDIO_URL = "https://dpgr.am/spacewalk.wav";

async function main() {
  const admin = new DeepgramClient();
  const { access_token, expires_in } = await admin.auth.v1.tokens.grant({
    ttl_seconds: 60,
  });
  console.log(`Temporary token granted (expires in ${expires_in}s)`);

  const agent = new DeepgramClient({ accessToken: access_token });
  const conn = await agent.agent.v1.createConnection();

  conn.on("message", (data) => {
    if (data.type === "SettingsApplied") console.log("Settings applied");
    else if (data.type === "ConversationText") {
      console.log(`${data.role === "assistant" ? "Agent" : "User"}: ${data.content}`);
    }
  });
  conn.on("error", (err) => console.error("Error:", err));

  conn.connect();
  await conn.waitForOpen();
  conn.sendSettings({
    type: "Settings",
    audio: {
      input: { encoding: "linear16", sample_rate: 24000 },
      output: { encoding: "linear16", sample_rate: 16000, container: "wav" },
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
  const buf = Buffer.from(await resp.arrayBuffer());
  for (let i = 0; i < buf.length; i += 4096) conn.sendMedia(buf.subarray(i, i + 4096));
  await new Promise((r) => setTimeout(r, 15000));
  conn.close();
}

main().catch(console.error);
