// Recipe: Configure LLM Provider (Voice Agents v1)
// ==================================================
// Demonstrates configuring a custom LLM provider for the voice agent's
// "think" step. The agent uses: listen (STT) → think (LLM) → speak (TTS).
//
// The Think provider controls which LLM processes user speech.
// See also: connect (basic setup), custom-tts (voice selection).

using Deepgram;
using Deepgram.Models.Agent.v2.WebSocket;

Library.Initialize();

var agentClient = ClientFactory.CreateAgentWebSocketClient();

await agentClient.Subscribe(new EventHandler<WelcomeResponse>((sender, e) =>
{
    Console.WriteLine($"Welcome received: {e}");
}));

var settings = new SettingsSchema();
settings.Agent.Think.Provider.Type = "open_ai";          // <-- LLM provider
settings.Agent.Think.Provider.Model = "gpt-4o-mini";     // <-- LLM model
settings.Agent.Think.Prompt = "You are a helpful assistant."; // <-- custom prompt
// Other providers: anthropic, etc. Other models: gpt-4o, etc.
settings.Agent.Listen.Provider.Type = "deepgram";
settings.Agent.Listen.Provider.Model = "nova-3";
settings.Agent.Speak.Provider.Type = "deepgram";
settings.Agent.Speak.Provider.Model = "aura-2-thalia-en";
settings.Agent.Greeting = "Hello! I am powered by a custom LLM.";
settings.Audio.Input.Encoding = "linear16";
settings.Audio.Input.SampleRate = 24000;
settings.Audio.Output.Encoding = "linear16";
settings.Audio.Output.SampleRate = 24000;
settings.Audio.Output.Container = "none";

Console.WriteLine($"LLM: {settings.Agent.Think.Provider.Type}/{settings.Agent.Think.Provider.Model}");
bool connected = await agentClient.Connect(settings);
Console.WriteLine($"Connected: {connected}");

await Task.Delay(5000);
await agentClient.Stop();
Console.WriteLine("Agent session completed");

Library.Terminate();
