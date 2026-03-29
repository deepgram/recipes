// Recipe: Sentiment Analysis (Audio Intelligence v1)
// =================================================
// Analyzes sentiment (positive, negative, neutral) for each segment of speech.
// Provides confidence scores and identifies emotional tone throughout the audio,
// useful for customer service analysis, meeting insights, or content moderation.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

// Initialize Deepgram library
Library.Initialize();

// Set "DEEPGRAM_API_KEY" environment variable to your Deepgram API Key
var client = ClientFactory.CreateListenRESTClient();

// Demo audio — a short spacewalk news segment hosted by Deepgram.
// Sentiment analysis works on any spoken content with emotional context
var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",        // nova-3 required for sentiment analysis
        Sentiment = true,        // Enable sentiment analysis
        SmartFormat = true,      // Clean formatting for better analysis
    });

// Print sentiment analysis for each segment
Console.WriteLine("Sentiment Analysis:");
if (response.Results.Sentiments?.Segments != null)
{
    foreach (var segment in response.Results.Sentiments.Segments)
    {
        Console.WriteLine($"[{segment.Sentiment}] {segment.Text}");
        Console.WriteLine($"  Confidence: {segment.Confidence:F2}");
        Console.WriteLine();
    }
}
else
{
    Console.WriteLine("No sentiment data available");
}

Library.Terminate();