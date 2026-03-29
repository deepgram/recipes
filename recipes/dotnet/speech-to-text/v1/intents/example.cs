// Recipe: Intents (Speech-to-Text v1)
// ==================================
// Demonstrates Deepgram's intent detection feature which identifies
// speaker intents and purposes within transcribed audio content.
//
// The intents feature analyzes the transcript to understand what
// the speakers are trying to accomplish or communicate,
// providing confidence scores for each detected intent.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-2",
        Intents = true,  // <-- THIS is the feature this recipe demonstrates
    });

// Intents are available at response.Results.Intents.Segments
// Each segment contains a list of intents with intent names and confidence scores
if (response.Results.Intents?.Segments != null)
{
    Console.WriteLine("Intents detected:");
    foreach (var segment in response.Results.Intents.Segments)
    {
        if (segment.Intents != null)
        {
            foreach (var intent in segment.Intents)
            {
                Console.WriteLine($"- {intent.Intent} (confidence: {intent.Confidence:F2})");
            }
        }
    }
}

Library.Terminate();