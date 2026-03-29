// Recipe: Configure TTS Voice (Voice Agents v1)
// ================================================
// Demonstrates choosing a specific aura-2 voice for the agent's speech.
// The "speak" step converts LLM text output to audio.
//
// Available voices: aura-2-thalia-en, aura-2-arcas-en, aura-2-luna-en, etc.
// See also: connect (basic setup), custom-llm (LLM selection).

using Deepgram;
using Deepgram.Models.Agent.v2.WebSocket;

Library.Initialize();

var agentClient = ClientFactory.CreateAgentWebSocketClient();

await agentClient.Subscribe(new EventHandler<WelcomeResponse>((sender, e) =>
{
    Console.WriteLine($"Welcome received: {e}");
}));

var settings = new SettingsSchema();
settings.Agent.Think.Provider.Type = "open_ai";
settings.Agent.Think.Provider.Model = "gpt-4o-mini";
settings.Agent.Listen.Provider.Type = "deepgram";
settings.Agent.Listen.Provider.Model = "nova-3";
settings.Agent.Speak.Provider.Type = "deepgram";
settings.Agent.Speak.Provider.Model = "aura-2-arcas-en";  // <-- custom voice model
// Try: aura-2-thalia-en, aura-2-luna-en, aura-2-zeus-en
settings.Agent.Greeting = "Hello! I am speaking with the Arcas voice.";
settings.Audio.Input.Encoding = "linear16";
settings.Audio.Input.SampleRate = 24000;
settings.Audio.Output.Encoding = "linear16";
settings.Audio.Output.SampleRate = 24000;
settings.Audio.Output.Container = "none";

Console.WriteLine($"TTS voice: {settings.Agent.Speak.Provider.Model}");
bool connected = await agentClient.Connect(settings);
Console.WriteLine($"Connected: {connected}");

await Task.Delay(5000);
await agentClient.Stop();
Console.WriteLine("Agent session completed");

Library.Terminate();
