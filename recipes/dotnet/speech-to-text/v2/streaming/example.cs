// Recipe: Live Streaming Transcription (Speech-to-Text v2)
// ========================================================
// Demonstrates real-time streaming with the v2 flux-general-en model,
// optimized for English audio with enhanced accuracy.
//
// Uses the same WebSocket client as v1 streaming but with the v2 model.
// See also: v1/streaming for the nova-3 variant.

using Deepgram;
using Deepgram.Models.Listen.v2.WebSocket;

Library.Initialize();

var liveClient = ClientFactory.CreateListenWebSocketClient();

await liveClient.Subscribe(new EventHandler<ResultResponse>((sender, e) =>
{
    var transcript = e.Channel.Alternatives[0].Transcript;
    if (!string.IsNullOrEmpty(transcript))
        Console.WriteLine($"Transcript: {transcript}");
}));

var liveSchema = new LiveSchema()
{
    Model = "flux-general-en",  // <-- v2 model for enhanced English transcription
    SmartFormat = true,
    Punctuate = true,
    // flux-general-en is English-only; for other languages use nova-3
};

bool connected = await liveClient.Connect(liveSchema);
if (!connected) { Console.WriteLine("Failed to connect"); return; }

using var http = new HttpClient();
var audioBytes = await http.GetByteArrayAsync("https://dpgr.am/spacewalk.wav");

for (int i = 0; i < audioBytes.Length; i += 8000)
{
    int len = Math.Min(8000, audioBytes.Length - i);
    var chunk = new byte[len];
    Array.Copy(audioBytes, i, chunk, 0, len);
    liveClient.Send(chunk);
    await Task.Delay(100);
}

await Task.Delay(3000);
await liveClient.Stop();
Library.Terminate();
