// Recipe: Intent Recognition (Audio Intelligence v1)
// =================================================
// Detects caller or speaker intents from conversational context.
// Identifies what the speaker is trying to accomplish or communicate,
// useful for customer service analysis, call routing, or conversation insights.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

// Initialize Deepgram library
Library.Initialize();

// Set "DEEPGRAM_API_KEY" environment variable to your Deepgram API Key
var client = ClientFactory.CreateListenRESTClient();

// Demo audio — a short spacewalk news segment hosted by Deepgram.
// Intent recognition works best with conversational or instructional content
var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",        // nova-3 required for intent recognition
        Intents = true,          // Enable intent detection
        SmartFormat = true,      // Clean formatting for better intent analysis
    });

// Print detected intents for each segment
Console.WriteLine("Detected Intents:");
if (response.Results.Intents?.Segments != null)
{
    foreach (var segment in response.Results.Intents.Segments)
    {
        if (segment.Intents != null)
        {
            foreach (var intent in segment.Intents)
            {
                Console.WriteLine($"Intent: {intent.Intent}");
                Console.WriteLine($"  Confidence: {intent.Confidence:F2}");
                Console.WriteLine($"  Context: {segment.Text}");
                Console.WriteLine();
            }
        }
    }
}
else
{
    Console.WriteLine("No intents detected");
}

Library.Terminate();