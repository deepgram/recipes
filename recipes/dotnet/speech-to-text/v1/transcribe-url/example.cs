// Recipe: Transcribe Audio from URL (Speech-to-Text v1)
// ======================================================
// Demonstrates the most basic pre-recorded transcription: send a URL
// pointing to a hosted audio file, get back a text transcript.
//
// This is the foundation recipe. All other STT recipes build on this
// pattern by adding feature flags (see: paragraphs, diarize, smart-format,
// etc. in sibling directories).

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

// Initialize Deepgram library
Library.Initialize();

// Set "DEEPGRAM_API_KEY" environment variable to your Deepgram API Key
var client = ClientFactory.CreateListenRESTClient();

// Demo audio — a short spacewalk news segment hosted by Deepgram.
// Any publicly accessible audio URL works (mp3, wav, flac, ogg, etc.)
var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",        // nova-3 is the highest-accuracy model
        SmartFormat = true,      // formats numbers, dates, currencies automatically
        // Other useful params: Punctuate, Paragraphs, Diarize, Language
    });

// response.Results.Channels[0].Alternatives[0].Transcript
//   Channels[0]      — first audio channel (use Multichannel for multi-track)
//   Alternatives[0]  — highest-confidence transcript
Console.WriteLine(response.Results.Channels[0].Alternatives[0].Transcript);

Library.Terminate();
