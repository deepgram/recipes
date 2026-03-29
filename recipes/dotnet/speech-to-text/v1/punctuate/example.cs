// Recipe: Punctuate (Speech-to-Text v1)
// ======================================
// Demonstrates punctuation-only formatting: adds periods, commas, question marks,
// and basic capitalization to the transcript.
//
// Without Punctuate: "yeah as much as its worth i mean you know from a scientific standpoint"
// With Punctuate:    "Yeah, as much as it's worth, I mean, you know, from a scientific standpoint."
//
// See also: smart-format (sibling directory) for full formatting including numbers.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        Punctuate = true,  // <-- THIS is the feature this recipe demonstrates
        // Adds basic punctuation and capitalization without number formatting
    });

// The transcript includes proper punctuation and capitalization
Console.WriteLine(response.Results.Channels[0].Alternatives[0].Transcript);

Library.Terminate();