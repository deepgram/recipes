// Recipe: Topics (Speech-to-Text v1)
// =================================
// Demonstrates Deepgram's topic detection feature which identifies
// topics discussed in the transcribed audio content.
//
// The topics feature analyzes the transcript and automatically
// categorizes different subjects and themes mentioned,
// providing confidence scores for each identified topic.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-2",
        Topics = true,  // <-- THIS is the feature this recipe demonstrates
    });

// Topics are available at response.Results.Topics.Segments
// Each segment contains a list of topics with topic names and confidence scores
if (response.Results.Topics?.Segments != null)
{
    Console.WriteLine("Topics detected:");
    foreach (var segment in response.Results.Topics.Segments)
    {
        if (segment.Topics != null)
        {
            foreach (var topic in segment.Topics)
            {
                Console.WriteLine($"- {topic.Topic} (confidence: {topic.Confidence:F2})");
            }
        }
    }
}

Library.Terminate();