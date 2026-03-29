// Recipe: Live Streaming Transcription (Speech-to-Text v1)
// ========================================================
// Demonstrates real-time transcription using WebSocket connection.
// Downloads audio, then streams it in chunks to simulate live audio.
//
// This recipe uses the WebSocket API (v2 namespace in SDK) with nova-3.
// See also: streaming-file (sibling) for a simpler file-streaming variant.

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
    Model = "nova-3",
    Punctuate = true,
    SmartFormat = true,  // <-- formats numbers, dates, currencies
    // Other useful params: Diarize, InterimResults, Utterances
};

bool connected = await liveClient.Connect(liveSchema);
if (!connected) { Console.WriteLine("Failed to connect"); return; }

// Download demo audio and stream in chunks to simulate live audio
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
