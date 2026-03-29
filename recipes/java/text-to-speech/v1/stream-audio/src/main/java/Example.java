/**
 * Recipe: Stream Audio Response (Text-to-Speech v1)
 * Streams TTS audio as it generates via REST, reading chunks incrementally.
 * Useful for low-latency playback where you process audio as it arrives.
 * See also: generate-audio for simple file save, websocket-streaming for WS
 */
import DeepgramClient;
import java.io.InputStream;
import resources.speak.v1.audio.requests.SpeakV1Request;

public class Example {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("DEEPGRAM_API_KEY");
        if (apiKey == null) throw new RuntimeException("Set DEEPGRAM_API_KEY");

        DeepgramClient client = DeepgramClient.builder().apiKey(apiKey).build();

        InputStream audio = client.speak().v1().audio().generate(
            SpeakV1Request.builder()
                .text("Hello from Deepgram! Streaming text-to-speech audio.")
                .model("aura-2-thalia-en")
                .encoding("linear16")  // <-- THIS: linear16 encoding for streaming
                .container("none")
                // Optional: sampleRate(24000), bitRate(128000)
                .build());

        byte[] buf = new byte[4096];
        int totalBytes = 0, chunks = 0, n;
        while ((n = audio.read(buf)) != -1) { totalBytes += n; chunks++; }
        audio.close();
        System.out.printf("Received %d chunks, %d bytes total%n", chunks, totalBytes);
    }
}