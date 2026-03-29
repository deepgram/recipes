// Recipe: Named Entity Recognition (Audio Intelligence v1)
// ======================================================
// Identifies and extracts named entities like people, organizations, locations,
// and other important references from the audio transcript. Useful for contact
// extraction, content indexing, or understanding key participants and places.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

// Initialize Deepgram library
Library.Initialize();

// Set "DEEPGRAM_API_KEY" environment variable to your Deepgram API Key
var client = ClientFactory.CreateListenRESTClient();

// Demo audio — a short spacewalk news segment hosted by Deepgram.
// Entity detection works best with content mentioning specific names, places, or organizations
var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",        // nova-3 required for entity detection
        DetectEntities = true,   // Enable named entity recognition
        SmartFormat = true,      // Clean formatting for better entity extraction
    });

// Print detected named entities
Console.WriteLine("Detected Entities:");
if (response.Results.Entities?.Entities != null)
{
    foreach (var entity in response.Results.Entities.Entities)
    {
        Console.WriteLine($"{entity.Label}: {entity.Value} ({entity.Confidence:F2})");
    }
}
else
{
    Console.WriteLine("No entities detected");
}

Library.Terminate();