// Recipe: Smart Format (Speech-to-Text v1)
// ==========================================
// Demonstrates Deepgram's smart formatting feature which automatically
// formats numbers, dates, currencies, addresses, and other entities.
//
// Without SmartFormat: "i owe you twenty three dollars and fifty cents"
// With SmartFormat:    "I owe you $23.50"
//
// See also: punctuate (sibling directory) for basic punctuation only.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        SmartFormat = true,  // <-- THIS is the feature this recipe demonstrates
        // SmartFormat includes punctuation, so Punctuate is not needed separately.
        // Other formatting params: Numerals, MeasurementUnits
    });

// The transcript is auto-formatted with proper casing, punctuation,
// numerals, dates, and currency symbols.
Console.WriteLine(response.Results.Channels[0].Alternatives[0].Transcript);

Library.Terminate();
