// Recipe: Numerals (Speech-to-Text v1)
// ======================================
// Demonstrates Deepgram's numerals feature which converts spoken numbers
// from written-out form to numeric digits in the transcript.
//
// Without Numerals: "twenty three percent of the fifty participants"
// With Numerals:    "23% of the 50 participants"
//
// See also: smart-format (includes numerals + more), measurements.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        Numerals = true,  // <-- THIS converts spoken numbers to digits
    });

Console.WriteLine(response.Results.Channels[0].Alternatives[0].Transcript);

Library.Terminate();
