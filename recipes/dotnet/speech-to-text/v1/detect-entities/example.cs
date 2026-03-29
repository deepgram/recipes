// Recipe: Detect Entities (Speech-to-Text v1)
// ============================================
// Demonstrates Deepgram's entity detection feature which identifies
// named entities like people, places, organizations, and other proper nouns.
//
// The entity detection feature automatically recognizes and categorizes
// specific named entities mentioned in the transcript, providing
// entity types, values, and confidence scores.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-2",
        DetectEntities = true,  // <-- THIS is the feature this recipe demonstrates
    });

// Entities are available at response.Results.Entities.Entities
// Each entity contains Label (type), Value (text), and Confidence
if (response.Results.Entities?.Entities != null)
{
    Console.WriteLine("Entities detected:");
    foreach (var entity in response.Results.Entities.Entities)
    {
        Console.WriteLine($"{entity.Label}: {entity.Value} (confidence: {entity.Confidence:F2})");
    }
}

Library.Terminate();