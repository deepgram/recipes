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

// MultiChannel=true transcribes each audio track independently.
// With stereo audio this gives separate transcripts per channel.
var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        SmartFormat = true,
        // MultiChannel = true  // uncomment for stereo/multi-track files
    });

// response.Results.Channels[i] holds each channel's transcript.
// With MultiChannel=true you get one entry per audio track.
Console.WriteLine($"Channels: {response.Results.Channels.Count}");
Console.WriteLine(response.Results.Channels[0].Alternatives[0].Transcript);

Library.Terminate();
