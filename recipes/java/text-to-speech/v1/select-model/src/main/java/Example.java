/**
 * Recipe: Select Voice Model (Text-to-Speech v1)
 * Choose from available aura-2 voice models for different voice characteristics.
 * Default: aura-2-thalia-en. Other options: aura-2-arcas-en, aura-2-asteria-en, etc.
 * See also: select-encoding for audio format options, generate-audio for basics
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
                .text("Hello! This is the Arcas voice model speaking.")
                .model("aura-2-arcas-en")  // <-- THIS: selecting a specific voice model
                // Available: aura-2-thalia-en, aura-2-arcas-en, aura-2-asteria-en, etc.
                .build());

        long bytes = Files.copy(audio, Path.of("output.mp3"), StandardCopyOption.REPLACE_EXISTING);
        audio.close();
        System.out.println("Audio saved: output.mp3 (" + bytes + " bytes, model: aura-2-arcas-en)");
    }
}