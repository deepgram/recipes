/**
 * Recipe: Multi-Turn Function Calling Chain (Voice Agents v1)
 * =============================================================
 * Chains sequential, dependent function calls across conversation turns.
 * Each function result feeds into the next: lookup_customer → get_orders
 * → check_return_eligibility → initiate_return.
 */

import { DeepgramClient } from "@deepgram/sdk";

const FUNCTIONS = [
  { name: "lookup_customer", description: "Find a customer by name",
    parameters: { type: "object", properties: { name: { type: "string" } }, required: ["name"] } },
  { name: "get_orders", description: "Get order history for a customer ID",
    parameters: { type: "object", properties: { customer_id: { type: "string" } }, required: ["customer_id"] } },
  { name: "check_return_eligibility", description: "Check if an order can be returned",
    parameters: { type: "object", properties: { order_id: { type: "string" } }, required: ["order_id"] } },
  { name: "initiate_return", description: "Start a return for an order",
    parameters: { type: "object", properties: { order_id: { type: "string" }, reason: { type: "string" } }, required: ["order_id", "reason"] } },
];

const MOCK_RESPONSES = {
  lookup_customer: '{"customer_id": "C-1234", "name": "Jane Smith", "email": "jane@example.com"}',
  get_orders: '{"orders": [{"order_id": "ORD-5678", "item": "Wireless Headphones", "date": "2026-10-15", "total": "$89.99"}]}',
  check_return_eligibility: '{"eligible": true, "return_window_days": 30, "days_remaining": 16}',
  initiate_return: '{"return_id": "RET-9012", "status": "approved", "label_url": "https://example.com/label/RET-9012"}',
};

let callCount = 0;

async function main() {
  const client = new DeepgramClient();
  const connection = await client.agent.v1.createConnection();

  connection.on("message", (data) => {
    if (data.type === "SettingsApplied") {
      console.log("Agent ready — sending return request");
      connection.sendInjectUserMessage({
        type: "InjectUserMessage",
        content: "I'm Jane Smith and I want to return the headphones I bought recently.",
      });
    } else if (data.type === "FunctionCallRequest") {
      for (const fn of data.functions) {
        callCount++;
        console.log(`Step ${callCount}: ${fn.name}(${fn.arguments})`);
        const content = MOCK_RESPONSES[fn.name] || '{"error": "unknown function"}';
        console.log(`  → ${content}`);
        connection.sendFunctionCallResponse({
          type: "FunctionCallResponse", id: fn.id, name: fn.name, content,
        });
      }
      if (callCount >= 4) {
        console.log(`\nChain complete: ${callCount} function calls executed`);
        setTimeout(() => connection.close(), 2000);
      }
    } else if (data.type === "ConversationText") {
      const role = data.role === "assistant" ? "Agent" : "User";
      console.log(`[${data.role}] ${data.content}`);
    }
  });

  connection.on("error", (err) => console.error("Error:", err));
  connection.connect();
  await connection.waitForOpen();
  console.log("Connection opened");

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
        prompt: "You are a customer service agent. When a user wants to return a product, " +
          "call these functions in order: lookup_customer, get_orders, " +
          "check_return_eligibility, then initiate_return. Pass results from each step to the next.",
        functions: FUNCTIONS,
      },
      speak: { provider: { type: "deepgram", model: "aura-2-thalia-en" } },
    },
  });

  await new Promise((resolve) => setTimeout(resolve, 30000));
  connection.close();
}

main().catch(console.error);
