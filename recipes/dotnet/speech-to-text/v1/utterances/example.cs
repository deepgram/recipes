// Recipe: Utterances (Speech-to-Text v1)
// ======================================
// Demonstrates utterance segmentation: splits transcripts into time-stamped
// speech segments with precise start and end timing information.
//
// Without Utterances: single continuous transcript
// With Utterances:    segmented chunks with "[0.5s - 3.2s] Hello there"
//
// Note: When Utterances=true, the response includes utterance data at
// response.Results.Utterances (a list of utterance objects)

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        Utterances = true,  // <-- THIS is the feature this recipe demonstrates
        SmartFormat = true, // Recommended alongside utterances for readability
    });

// Access utterance data when Utterances=true
var utterances = response.Results.Utterances;

Console.WriteLine($"Found {utterances.Count} utterance(s):\n");

foreach (var utterance in utterances)
{
    Console.WriteLine($"[{utterance.Start:F1}s - {utterance.End:F1}s] {utterance.Transcript}");
}

Library.Terminate();