// Recipe: Summarize (Speech-to-Text v1)
// ====================================
// Demonstrates Deepgram's summarization feature which generates
// concise summaries of transcribed audio content.
//
// The summarization feature provides a condensed version of the main
// points discussed in the audio, making it easier to understand
// long-form content at a glance.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        Summarize = "v2",  // <-- THIS is the feature this recipe demonstrates
        // Note: Summarize expects string "v2", not boolean true
    });

// The summary is available at response.Results.Summary.Short
// This provides a concise overview of the audio content
Console.WriteLine($"Summary: {response.Results.Summary.Short}");

Library.Terminate();