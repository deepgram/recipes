// Recipe: Transcribe Local Audio File (Speech-to-Text v1)
// ========================================================
// Demonstrates transcribing a local audio file by reading its bytes and
// sending them to Deepgram's pre-recorded endpoint.
//
// Compare with transcribe-url (sibling directory) which sends a URL instead.
// The response structure is identical — only the input method differs.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

// Set "DEEPGRAM_API_KEY" environment variable to your Deepgram API Key
var client = ClientFactory.CreateListenRESTClient();

// Download demo audio to a temp file for demonstration
using var http = new HttpClient();
var audioBytes = await http.GetByteArrayAsync("https://dpgr.am/spacewalk.wav");

var response = await client.TranscribeFile(
    audioBytes,
    new PreRecordedSchema()
    {
        Model = "nova-3",
        SmartFormat = true,
        // Other useful params: Punctuate, Paragraphs, Diarize
    });

// response.Results.Channels[0].Alternatives[0].Transcript
//   Same response path as TranscribeUrl — the API returns identical structures.
Console.WriteLine(response.Results.Channels[0].Alternatives[0].Transcript);

Library.Terminate();
