/**
 * Recipe: Dynamic Context Injection (Voice Agents v1)
 * =====================================================
 * Update prompts and inject messages into an active voice agent session.
 * Use UpdatePrompt to change agent behavior mid-conversation and
 * InjectAgentMessage to make the agent speak without the LLM.
 */

import { DeepgramClient } from "@deepgram/sdk";

const AUDIO_URL = "https://dpgr.am/spacewalk.wav";

async function main() {
  const client = new DeepgramClient();
  const connection = await client.agent.v1.createConnection();

  connection.on("message", (data) => {
    if (data.type === "SettingsApplied") {
      console.log("Settings applied — injecting initial context");
      connection.sendInjectAgentMessage({
        type: "InjectAgentMessage",
        message: "Welcome! I am your general assistant.",
      });
      setTimeout(() => {
        console.log("Updating prompt to specialist persona");
        connection.sendUpdatePrompt({
          type: "UpdatePrompt",
          prompt: "You are a NASA space mission specialist. Answer only about space missions.",
        });
      }, 3000);
      setTimeout(() => {
        console.log("Injecting user question after prompt update");
        connection.sendInjectUserMessage({
          type: "InjectUserMessage",
          content: "Tell me about the spacewalk mission.",
        });
      }, 5000);
    } else if (data.type === "PromptUpdated") {
      console.log("Prompt updated successfully");
    } else if (data.type === "ConversationText") {
      console.log(`${data.role === "assistant" ? "Agent" : "User"}: ${data.content}`);
    } else if (data.type === "InjectionRefused") {
      console.log("Injection refused — agent is speaking");
    }
  });

  connection.on("error", (err) => console.error("Error:", err));
  connection.connect();
  await connection.waitForOpen();

  connection.sendSettings({
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
        prompt: "You are a friendly general assistant. Keep responses brief.",
      },
      speak: { provider: { type: "deepgram", model: "aura-2-thalia-en" } },
    },
  });

  const resp = await fetch(AUDIO_URL);
  const buffer = Buffer.from(await resp.arrayBuffer());
  for (let i = 0; i < buffer.length; i += 4096) {
    connection.sendMedia(buffer.subarray(i, i + 4096));
  }

  await new Promise((resolve) => setTimeout(resolve, 20000));
  connection.close();
}

main().catch(console.error);
