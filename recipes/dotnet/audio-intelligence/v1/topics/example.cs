// Recipe: Topic Detection (Audio Intelligence v1)
// ===============================================
// Identifies and extracts key topics discussed in the audio content.
// Uses AI to recognize themes, subjects, and discussion points throughout
// the conversation, ideal for meeting analysis, content categorization, or research.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

// Initialize Deepgram library
Library.Initialize();

// Set "DEEPGRAM_API_KEY" environment variable to your Deepgram API Key
var client = ClientFactory.CreateListenRESTClient();

// Demo audio — a short spacewalk news segment hosted by Deepgram.
// Topic detection works best with substantial content containing clear themes
var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",        // nova-3 required for topic detection
        Topics = true,           // Enable topic detection
        SmartFormat = true,      // Clean formatting for better topic analysis
    });

// Print detected topics for each segment
Console.WriteLine("Detected Topics:");
if (response.Results.Topics?.Segments != null)
{
    foreach (var segment in response.Results.Topics.Segments)
    {
        if (segment.Topics != null)
        {
            foreach (var topic in segment.Topics)
            {
                Console.WriteLine($"Topic: {topic.Topic}");
                Console.WriteLine($"  Confidence: {topic.Confidence:F2}");
                Console.WriteLine($"  Context: {segment.Text}");
                Console.WriteLine();
            }
        }
    }
}
else
{
    Console.WriteLine("No topics detected");
}

Library.Terminate();