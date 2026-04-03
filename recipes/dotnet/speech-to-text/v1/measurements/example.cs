// Recipe: Measurements (Speech-to-Text v1)
// ==========================================
// Demonstrates Deepgram's measurements feature which converts spoken
// measurement terms to their standard abbreviations in the transcript.
//
// Without Measurements: "five milligrams per liter"
// With Measurements:    "5 mg/L"
//
// See also: numerals (numeric digits), smart-format (all formatting).

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        Measurements = true,  // <-- THIS converts spoken measurements to abbreviations
    });

Console.WriteLine(response.Results.Channels[0].Alternatives[0].Transcript);

Library.Terminate();
