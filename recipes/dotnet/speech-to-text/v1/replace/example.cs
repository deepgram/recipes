// Recipe: Find and Replace (Speech-to-Text v1)
// ==============================================
// Demonstrates Deepgram's find-and-replace feature which substitutes
// specific terms in the transcript output with replacement text.
//
// Format: "original:replacement" — each pair replaces all occurrences.
// Useful for correcting brand names, normalizing terms, or redacting words.
//
// See also: redact (PII redaction), keywords (boost accuracy).

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        Replace = new List<string> { "spacewalk:space walk", "anniversary:milestone" },  // <-- THIS replaces terms in the output
    });

Console.WriteLine(response.Results.Channels[0].Alternatives[0].Transcript);

Library.Terminate();
