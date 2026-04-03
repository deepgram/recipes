// Recipe: Profanity Filter (Speech-to-Text v1)
// ==============================================
// Demonstrates Deepgram's profanity filter which masks or removes
// recognized profanity from the transcript output.
//
// Profane words are replaced with the nearest non-profane word
// or removed entirely from the transcript.
//
// See also: redact (PII/PCI redaction), smart-format (formatting).

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        ProfanityFilter = true,  // <-- THIS masks profanity in the output
    });

Console.WriteLine(response.Results.Channels[0].Alternatives[0].Transcript);

Library.Terminate();
