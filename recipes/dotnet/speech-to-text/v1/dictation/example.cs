// Recipe: Dictation Mode (Speech-to-Text v1)
// ===========================================
// Demonstrates dictation mode, which interprets spoken punctuation commands
// literally. For example, saying "period" inserts "." and "comma" inserts ",".
//
// Useful for hands-free document creation where the speaker explicitly
// dictates punctuation instead of relying on automatic punctuation.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

// Set "DEEPGRAM_API_KEY" environment variable to your Deepgram API Key
var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        Dictation = true,       // <-- THIS enables dictation mode
        SmartFormat = true,     // Recommended alongside dictation for clean output
    });

// With Dictation=true, spoken punctuation commands like "period", "comma",
// "question mark" are converted to their punctuation equivalents.
Console.WriteLine(response.Results.Channels[0].Alternatives[0].Transcript);

Library.Terminate();
