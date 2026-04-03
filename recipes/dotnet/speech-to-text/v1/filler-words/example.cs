// Recipe: Filler Words (Speech-to-Text v1)
// =========================================
// Demonstrates Deepgram's filler words feature which captures words
// like "uh", "um", "mhm" in the transcript instead of removing them.
//
// Without FillerWords: "I think we should move forward"
// With FillerWords:    "Um I think uh we should move forward"
//
// See also: smart-format (automatic formatting), punctuate (punctuation).

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        FillerWords = true,  // <-- THIS captures filler words ("uh", "um") in output
    });

Console.WriteLine(response.Results.Channels[0].Alternatives[0].Transcript);

Library.Terminate();
