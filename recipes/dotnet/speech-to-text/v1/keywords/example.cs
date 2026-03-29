// Recipe: Keywords (Speech-to-Text v1)
// ===================================
// Demonstrates Deepgram's keyword boosting feature which improves
// recognition accuracy for specific words by applying boost multipliers.
//
// The keywords feature allows you to specify important terms that
// should receive enhanced recognition accuracy, particularly useful
// for proper nouns, technical terms, and domain-specific vocabulary.

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
        Keywords = new List<string> { "Deepgram:2", "spacewalk:1.5" },  // <-- THIS is the feature this recipe demonstrates
        // Format: "word:boost" where boost is a float multiplier (1.0-3.0)
        // Higher boost values increase recognition confidence for that word
    });

// The transcript benefits from improved accuracy for the specified keywords
// Keywords don't appear in a separate section - they improve overall transcript quality
Console.WriteLine("Enhanced transcript with keyword boosting:");
Console.WriteLine(response.Results.Channels[0].Alternatives[0].Transcript);

Library.Terminate();