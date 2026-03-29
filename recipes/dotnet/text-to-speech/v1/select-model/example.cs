// Recipe: Select Voice Model (Text-to-Speech v1)
// ================================================
// Demonstrates choosing a specific aura-2 voice model for TTS.
//
// Available aura-2 models include:
//   aura-2-thalia-en (female, warm)       aura-2-luna-en (female, friendly)
//   aura-2-arcas-en (male, conversational) aura-2-zeus-en (male, authoritative)
//
// See also: select-encoding (choose audio format), generate-audio (basic TTS).

using Deepgram;
using Deepgram.Models.Speak.v1.REST;

Library.Initialize();

// Set "DEEPGRAM_API_KEY" environment variable to your Deepgram API Key
var client = ClientFactory.CreateSpeakRESTClient();

var response = await client.ToFile(
    new TextSource("This example demonstrates selecting different voice models."),
    "output.mp3",
    new SpeakSchema()
    {
        Model = "aura-2-arcas-en",  // <-- THIS selects the voice model
        // Try: aura-2-thalia-en, aura-2-luna-en, aura-2-zeus-en
    });

Console.WriteLine(response);
Console.WriteLine($"Model used: aura-2-arcas-en");

if (File.Exists("output.mp3"))
{
    Console.WriteLine($"Audio saved: {new FileInfo("output.mp3").Length} bytes");
    File.Delete("output.mp3");
}

Library.Terminate();
