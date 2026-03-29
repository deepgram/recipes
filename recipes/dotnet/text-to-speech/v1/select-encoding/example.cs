// Recipe: Select Audio Encoding (Text-to-Speech v1)
// ==================================================
// Demonstrates choosing different audio encodings for TTS output.
//
// Available encodings: linear16, mp3, opus, flac, aac, mulaw
// See also: select-model (choose voice), generate-audio (basic TTS).

using Deepgram;
using Deepgram.Models.Speak.v1.REST;

Library.Initialize();

// Set "DEEPGRAM_API_KEY" environment variable to your Deepgram API Key
var client = ClientFactory.CreateSpeakRESTClient();

var response = await client.ToFile(
    new TextSource("This example shows how to select different audio encodings."),
    "output.mp3",
    new SpeakSchema()
    {
        Model = "aura-2-thalia-en",
        Encoding = "mp3",       // <-- THIS selects the audio encoding
        Container = "none",     // container format: "none" or "wav"
        // Other encodings: linear16, opus, flac, aac, mulaw
    });

Console.WriteLine(response);
Console.WriteLine($"Encoding: mp3, Container: none");

if (File.Exists("output.mp3"))
{
    Console.WriteLine($"Audio saved: {new FileInfo("output.mp3").Length} bytes");
    File.Delete("output.mp3");
}

Library.Terminate();
