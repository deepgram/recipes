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

// multichannel=true returns each audio channel transcribed independently.
// Mono audio returns 1 channel; stereo/multi-track audio returns multiple.
var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        SmartFormat = true,
        // MultiChannel = true  -- enable for stereo/multi-track files
    });

// Even without MultiChannel=true, channels[0] is the full transcript.
// With MultiChannel=true and stereo audio, channels[0], channels[1] etc.
// each contain independent per-channel transcripts.
var channels = response?.Results?.Channels;
if (channels == null || channels.Count == 0)
{
    Console.WriteLine("No channels in response.");
    Library.Terminate();
    return;
}

Console.WriteLine($"Found {channels.Count} channel(s). Multichannel=true adds one entry per audio track.\n");

foreach (var ch in channels)
{
    var transcript = ch.Alternatives?[0]?.Transcript ?? "";
    Console.WriteLine(transcript);
}

Library.Terminate();