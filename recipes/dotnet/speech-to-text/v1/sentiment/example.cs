// Recipe: Sentiment (Speech-to-Text v1)
// ====================================
// Demonstrates Deepgram's sentiment analysis feature which analyzes
// the emotional tone (positive, negative, neutral) of transcribed audio.
//
// The sentiment analysis feature evaluates the emotional context
// of speech segments, providing sentiment labels and confidence
// scores for understanding the speaker's emotional state.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-2",
        Sentiment = true,  // <-- THIS is the feature this recipe demonstrates
    });

// Sentiments are available at response.Results.Sentiments.Segments
// Each segment contains sentiment, text, and confidence score
if (response.Results.Sentiments?.Segments != null)
{
    Console.WriteLine("Sentiment analysis:");
    foreach (var segment in response.Results.Sentiments.Segments)
    {
        Console.WriteLine($"[{segment.Sentiment}] {segment.Text} (confidence: {segment.Confidence:F2})");
    }
}

Library.Terminate();