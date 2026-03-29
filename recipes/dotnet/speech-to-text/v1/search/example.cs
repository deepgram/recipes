// Recipe: Search (Speech-to-Text v1)
// =================================
// Demonstrates Deepgram's search feature which finds specific
// words or phrases within audio with timestamps and confidence scores.
//
// The search feature allows you to locate exact instances of
// specified terms in the transcript, providing precise timing
// and confidence information for each match.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;
using System.Collections.Generic;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-2",
        Search = new List<string> { "spacewalk", "NASA" },  // <-- THIS is the feature this recipe demonstrates
    });

// Search results are available at response.Results.Channels[0].Search
// Each search result group contains hits for the specified search terms
if (response.Results.Channels[0].Search != null)
{
    Console.WriteLine("Search results:");
    foreach (var searchGroup in response.Results.Channels[0].Search)
    {
        foreach (var hit in searchGroup.Hits)
        {
            Console.WriteLine($"Found '{hit.Word}' at {hit.Start:F2}s-{hit.End:F2}s (confidence: {hit.Confidence:F2})");
        }
    }
}

Library.Terminate();