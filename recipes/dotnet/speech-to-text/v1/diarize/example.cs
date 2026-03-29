// Recipe: Diarize (Speech-to-Text v1)
// ===================================
// Demonstrates speaker diarization: identifies and labels different speakers
// in multi-speaker audio, assigning each word/segment to a speaker ID.
//
// Without Diarize: "hello there how are you doing today"
// With Diarize:    "Speaker 0: hello there" "Speaker 1: how are you doing today"
//
// Note: Combines with Utterances for best results - each utterance gets a speaker ID

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        Diarize = true,    // <-- THIS is the feature this recipe demonstrates
        Utterances = true, // Recommended alongside diarize for speaker-per-utterance
        SmartFormat = true,
    });

// When using both Diarize and Utterances, each utterance has a speaker ID
var utterances = response.Results.Utterances;

Console.WriteLine($"Found {utterances.Count} utterance(s) with speaker labels:\n");

foreach (var utterance in utterances)
{
    Console.WriteLine($"Speaker {utterance.Speaker}: {utterance.Transcript}");
}

Library.Terminate();