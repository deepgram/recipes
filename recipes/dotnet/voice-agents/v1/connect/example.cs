// Recipe: Connect to Voice Agent (Voice Agents v1)
// ==================================================
// Establishes a WebSocket voice agent session with default settings.
// The agent pipeline is: listen (STT) → think (LLM) → speak (TTS).
//
// This is the foundation recipe. See also: custom-llm, custom-tts,
// function-calling in sibling directories.

using Deepgram;
using Deepgram.Models.Agent.v2.WebSocket;

Library.Initialize();

var agentClient = ClientFactory.CreateAgentWebSocketClient();

await agentClient.Subscribe(new EventHandler<WelcomeResponse>((sender, e) =>
{
    Console.WriteLine($"Welcome received: {e}");
}));

await agentClient.Subscribe(new EventHandler<ConversationTextResponse>((sender, e) =>
{
    Console.WriteLine($"Agent: {e}");
}));

// Configure agent: listen → think → speak pipeline
var settings = new SettingsSchema();
settings.Agent.Think.Provider.Type = "open_ai";
settings.Agent.Think.Provider.Model = "gpt-4o-mini";
settings.Agent.Listen.Provider.Type = "deepgram";
settings.Agent.Listen.Provider.Model = "nova-3";
settings.Agent.Speak.Provider.Type = "deepgram";
settings.Agent.Speak.Provider.Model = "aura-2-thalia-en";
settings.Agent.Greeting = "Hello! I am your voice assistant.";
settings.Audio.Input.Encoding = "linear16";
settings.Audio.Input.SampleRate = 24000;
settings.Audio.Output.Encoding = "linear16";
settings.Audio.Output.SampleRate = 24000;
settings.Audio.Output.Container = "none";

bool connected = await agentClient.Connect(settings);
Console.WriteLine($"Connected: {connected}");

await Task.Delay(5000);
await agentClient.Stop();
Console.WriteLine("Agent session completed");

Library.Terminate();
