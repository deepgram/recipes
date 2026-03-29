// Recipe: Multichannel (Speech-to-Text v1)
// ========================================
// Demonstrates multichannel transcription: processes each audio channel
// independently, useful for stereo recordings or multi-track audio.
//
// Without Multichannel: all channels mixed together in one transcript
// With Multichannel:    separate transcript for each channel
//
// Note: Single-channel audio still works but will only have one channel in results.
// The demo audio is mono, so this example shows the structure with one channel.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        Multichannel = true,  // <-- THIS is the feature this recipe demonstrates
        SmartFormat = true,
    });

// When Multichannel=true, response.Results.Channels is an array
var channels = response.Results.Channels;

Console.WriteLine($"Found {channels.Count} audio channel(s):\n");

for (int i = 0; i < channels.Count; i++)
{
    var transcript = channels[i].Alternatives[0].Transcript;
    Console.WriteLine($"Channel {i}: {transcript}");
}

Library.Terminate();