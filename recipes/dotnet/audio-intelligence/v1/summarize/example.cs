// Recipe: Text Summarization (Audio Intelligence v1)
// ====================================================
// Generates a concise summary of spoken content using AI analysis.
// The summary feature extracts key points and themes from the transcript,
// making it ideal for meeting notes, lecture summaries, or content analysis.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

// Initialize Deepgram library
Library.Initialize();

// Set "DEEPGRAM_API_KEY" environment variable to your Deepgram API Key
var client = ClientFactory.CreateListenRESTClient();

// Demo audio — a short spacewalk news segment hosted by Deepgram.
// Summarization works best with longer content (2+ minutes)
var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",        // nova-3 required for summarization
        Summarize = "v2",        // Enable v2 summarization (string, not bool)
        SmartFormat = true,      // Clean formatting for better summary output
    });

// Print the generated summary
// Note: summary may be empty for very short audio files
if (response.Results.Summary?.Short != null)
{
    Console.WriteLine("Summary:");
    Console.WriteLine(response.Results.Summary.Short);
}
else
{
    Console.WriteLine("No summary generated (audio may be too short)");
}

Library.Terminate();