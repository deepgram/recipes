// Recipe: WebSocket Streaming TTS (Text-to-Speech v1)
// ====================================================
// Low-latency TTS via WebSocket for real-time use cases.
// Audio chunks arrive as events, enabling immediate playback.
//
// See also: generate-audio (REST file), stream-audio (REST streaming).

using Deepgram;
using Deepgram.Models.Speak.v2.WebSocket;

Library.Initialize();

// Set "DEEPGRAM_API_KEY" environment variable to your Deepgram API Key
var speakClient = ClientFactory.CreateSpeakWebSocketClient();
long totalBytes = 0;

await speakClient.Subscribe(new EventHandler<AudioResponse>((sender, e) =>
{
    if (e.Stream != null)
    {
        var bytes = e.Stream.ToArray();
        totalBytes += bytes.Length;
        Console.WriteLine($"Received audio chunk: {bytes.Length} bytes");
    }
}));

await speakClient.Subscribe(new EventHandler<OpenResponse>((sender, e) =>
{
    Console.WriteLine("WebSocket connection opened");
}));

var speakSchema = new SpeakSchema()
{
    Encoding = "linear16",
    SampleRate = 48000,
    // Other params: Model (default voice used if omitted)
};

bool connected = await speakClient.Connect(speakSchema);
if (!connected) { Console.WriteLine("Failed to connect"); return; }

speakClient.SpeakWithText("Hello from Deepgram WebSocket streaming!");
speakClient.Flush();

await Task.Delay(5000);
Console.WriteLine($"Total audio bytes received: {totalBytes}");

await speakClient.Stop();
Library.Terminate();
