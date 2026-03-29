// Recipe: Detect Language (Speech-to-Text v1)
// ============================================
// Demonstrates automatic language detection: identifies the spoken language
// in the audio without requiring you to specify it in advance.
//
// Without DetectLanguage: must specify language parameter manually
// With DetectLanguage:    automatically identifies "en", "es", "fr", etc.
//
// The detected language is available at response.Results.Channels[0].DetectedLanguage

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        DetectLanguage = true,  // <-- THIS is the feature this recipe demonstrates
        SmartFormat = true,
    });

// Access detected language when DetectLanguage=true
var detectedLanguage = response.Results.Channels[0].DetectedLanguage;
var transcript = response.Results.Channels[0].Alternatives[0].Transcript;

Console.WriteLine($"Detected Language: {detectedLanguage}");
Console.WriteLine($"Transcript: {transcript}");

Library.Terminate();