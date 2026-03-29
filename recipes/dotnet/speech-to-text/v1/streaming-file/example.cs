// Recipe: Stream Audio File for Transcription (Speech-to-Text v1)
// ===============================================================
// Streams a complete audio file over WebSocket for transcription.
// Use this when you have a file but want progressive results instead
// of waiting for a single batch response (see: transcribe-url, transcribe-file).

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
    SmartFormat = true,
    // Other useful params: Punctuate, Diarize, InterimResults
};

bool connected = await liveClient.Connect(liveSchema);
if (!connected) { Console.WriteLine("Failed to connect"); return; }

// Download and stream the entire audio file in chunks
using var http = new HttpClient();
var audioBytes = await http.GetByteArrayAsync("https://dpgr.am/spacewalk.wav");

for (int i = 0; i < audioBytes.Length; i += 16000)
{
    int len = Math.Min(16000, audioBytes.Length - i);
    var chunk = new byte[len];
    Array.Copy(audioBytes, i, chunk, 0, len);
    liveClient.Send(chunk);
    await Task.Delay(50);
}

await Task.Delay(3000);
await liveClient.Stop();
Library.Terminate();
