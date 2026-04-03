// Recipe: Bit Rate Control (Text-to-Speech v1)
// ==============================================
// Demonstrates controlling the output audio bit rate for TTS.
//
// Lower bit rates reduce file size (good for bandwidth-constrained use cases).
// Higher bit rates improve audio quality. Only applies to compressed encodings
// like mp3 — has no effect on linear16 or other uncompressed formats.
//
// See also: select-encoding (encoding format), select-model (voice choice).

using Deepgram;
using Deepgram.Models.Speak.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateSpeakRESTClient();

var response = await client.ToFile(
    new TextSource("Hello from Deepgram! This example demonstrates bit rate control for compressed audio output."),
    "output.mp3",
    new SpeakSchema()
    {
        Model = "aura-2-thalia-en",
        Encoding = "mp3",
        BitRate = "48000",  // <-- THIS controls the output bit rate (in bps)
    });

Console.WriteLine(response);

if (File.Exists("output.mp3"))
{
    Console.WriteLine($"Audio saved: {new FileInfo("output.mp3").Length} bytes (48kbps mp3)");
    File.Delete("output.mp3");
}

Library.Terminate();
