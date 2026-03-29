// Recipe: Transcribe URL with v2 Model (Speech-to-Text v2)
// ========================================================
// Demonstrates using Deepgram's v2 API model (flux-general-en) for
// English-optimized transcription. This uses the same REST client
// as v1 but with the new flux-general-en model.
//
// v2 model benefits:
// - Optimized specifically for English language
// - Improved accuracy for conversational speech
// - Better performance on noisy audio

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

// Use the v2 model through the v1 REST client
var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "flux-general-en",  // <-- v2 model for English
        SmartFormat = true,
        Punctuate = true,
        // The flux-general-en model is optimized for English only
        // For other languages, use v1 models like nova-3
    });

// Extract and print the transcript
var transcript = response.Results.Channels[0].Alternatives[0].Transcript;
Console.WriteLine($"Transcript: {transcript}");

// Print confidence score (v2 models provide enhanced confidence metrics)
var confidence = response.Results.Channels[0].Alternatives[0].Confidence;
Console.WriteLine($"Confidence: {confidence:F2}");

Library.Terminate();