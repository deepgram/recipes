// Recipe: Stream Audio Response (Text-to-Speech v1)
// ==================================================
// Streams TTS audio as it generates using the REST streaming endpoint.
// The audio data arrives progressively, allowing playback to begin before
// the full response is ready.
//
// See also: generate-audio (save to file), websocket-streaming (lowest latency).

using Deepgram;
using Deepgram.Models.Speak.v1.REST;

Library.Initialize();

// Set "DEEPGRAM_API_KEY" environment variable to your Deepgram API Key
var client = ClientFactory.CreateSpeakRESTClient();

var response = await client.Stream(
    new TextSource("This is a streaming text-to-speech example with linear16 encoding."),
    new SpeakSchema()
    {
        Model = "aura-2-thalia-en",
        Encoding = "linear16",  // <-- THIS controls the audio encoding
        // Other encodings: mp3, opus, flac, aac, mulaw
    });

Console.WriteLine(response);

if (response.Stream != null)
{
    using var ms = new MemoryStream();
    await response.Stream.CopyToAsync(ms);
    Console.WriteLine($"Streamed audio size: {ms.Length} bytes");
}

Library.Terminate();
