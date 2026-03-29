/**
 * Recipe: Generate Audio to File (Text-to-Speech v1)
 * Converts text to speech audio and saves to a file.
 * generate() returns an InputStream of audio bytes.
 * See also: stream-audio, websocket-streaming, select-model, select-encoding
 */
import DeepgramClient;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import resources.speak.v1.audio.requests.SpeakV1Request;

public class Example {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("DEEPGRAM_API_KEY");
        if (apiKey == null) throw new RuntimeException("Set DEEPGRAM_API_KEY");

        DeepgramClient client = DeepgramClient.builder().apiKey(apiKey).build();

        InputStream audio = client.speak().v1().audio().generate(
            SpeakV1Request.builder()
                .text("Hello from Deepgram! This is a text-to-speech example.")
                .model("aura-2-thalia-en")  // <-- THIS: aura-2 voice model
                // Optional: encoding("linear16"), container("wav"), sampleRate(24000)
                .build());

        long bytes = Files.copy(audio, Path.of("output.mp3"), StandardCopyOption.REPLACE_EXISTING);
        audio.close();
        System.out.println("Audio saved: output.mp3 (" + bytes + " bytes)");
    }
}