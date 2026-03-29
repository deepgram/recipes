// Recipe: Generate Audio to File (Text-to-Speech v1)
// ===================================================
// Converts text to audio using Deepgram's TTS REST API and saves to a file.
//
// The ToFile method handles the full request-to-file pipeline.
// See also: stream-audio (REST streaming), websocket-streaming (low-latency).

using Deepgram;
using Deepgram.Models.Speak.v1.REST;

Library.Initialize();

// Set "DEEPGRAM_API_KEY" environment variable to your Deepgram API Key
var client = ClientFactory.CreateSpeakRESTClient();

var response = await client.ToFile(
    new TextSource("Hello from Deepgram! This is a text-to-speech example using the aura 2 model."),
    "output.mp3",
    new SpeakSchema()
    {
        Model = "aura-2-thalia-en",  // <-- THIS is the voice model
        // Other models: aura-2-arcas-en, aura-2-luna-en, aura-2-zeus-en
        // Other params: Encoding, SampleRate, Container
    });

Console.WriteLine(response);

if (File.Exists("output.mp3"))
{
    var size = new FileInfo("output.mp3").Length;
    Console.WriteLine($"Audio saved: {size} bytes");
    File.Delete("output.mp3");
}

Library.Terminate();
