// Recipe: Paragraphs (Speech-to-Text v1)
// ======================================
// Demonstrates paragraph segmentation: intelligently splits long transcripts
// into semantic paragraph blocks based on natural speech patterns.
//
// Without Paragraphs: one continuous string of text
// With Paragraphs:    text organized into logical paragraph units
//
// Note: When Paragraphs=true, the response includes paragraph data at
// response.Results.Channels[0].Alternatives[0].Paragraphs.Paragraphs

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        Paragraphs = true,  // <-- THIS is the feature this recipe demonstrates
        SmartFormat = true, // Recommended alongside paragraphs for readability
    });

// Access paragraph data when Paragraphs=true
var paragraphs = response.Results.Channels[0].Alternatives[0].Paragraphs.Paragraphs;

Console.WriteLine($"Found {paragraphs.Count} paragraph(s):\n");

for (int i = 0; i < paragraphs.Count; i++)
{
    Console.WriteLine($"Paragraph {i + 1}:");
    Console.WriteLine(string.Join(" ", paragraphs[i].Sentences.Select(s => s.Text)));
    Console.WriteLine(); // Empty line between paragraphs
}

Library.Terminate();