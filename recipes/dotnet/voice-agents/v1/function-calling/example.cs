// Recipe: Function Calling (Voice Agents v1)
// ============================================
// Demonstrates subscribing to function call events from the voice agent.
// When the LLM decides to call a function, a FunctionCallRequestResponse
// event fires with the function name and arguments.
//
// See also: connect (basic setup), custom-llm (LLM configuration).

using Deepgram;
using Deepgram.Models.Agent.v2.WebSocket;

Library.Initialize();

var agentClient = ClientFactory.CreateAgentWebSocketClient();

await agentClient.Subscribe(new EventHandler<WelcomeResponse>((sender, e) =>
{
    Console.WriteLine($"Welcome received: {e}");
}));

await agentClient.Subscribe(new EventHandler<FunctionCallRequestResponse>((sender, e) =>
{
    Console.WriteLine($"Function call: {e}");
}));

var settings = new SettingsSchema();
settings.Agent.Think.Provider.Type = "open_ai";
settings.Agent.Think.Provider.Model = "gpt-4o-mini";
settings.Agent.Listen.Provider.Type = "deepgram";
settings.Agent.Listen.Provider.Model = "nova-3";
settings.Agent.Speak.Provider.Type = "deepgram";
settings.Agent.Speak.Provider.Model = "aura-2-thalia-en";
settings.Agent.Greeting = "Hello! I can help with weather and calculations.";
settings.Audio.Input.Encoding = "linear16";
settings.Audio.Input.SampleRate = 24000;
settings.Audio.Output.Encoding = "linear16";
settings.Audio.Output.SampleRate = 24000;
settings.Audio.Output.Container = "none";

Console.WriteLine("Function calling event handler registered");
bool connected = await agentClient.Connect(settings);
Console.WriteLine($"Connected: {connected}");

await Task.Delay(5000);
await agentClient.Stop();
Console.WriteLine("Agent session completed");

Library.Terminate();
