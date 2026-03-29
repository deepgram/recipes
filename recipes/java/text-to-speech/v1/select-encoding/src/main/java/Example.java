/**
 * Recipe: Select Audio Encoding (Text-to-Speech v1)
 * Choose output audio encoding: linear16, mp3, opus, flac, aac, mulaw.
 * Different encodings suit different use cases (streaming, file storage, telephony).
 * See also: select-model for voice options, generate-audio for basics
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
                .text("This audio uses linear16 encoding in a WAV container.")
                .model("aura-2-thalia-en")
                .encoding("linear16")  // <-- THIS: selecting audio encoding
                .container("wav")      // Container format: wav, none
                // Available encodings: linear16, mp3, opus, flac, aac, mulaw
                .build());

        long bytes = Files.copy(audio, Path.of("output.wav"), StandardCopyOption.REPLACE_EXISTING);
        audio.close();
        System.out.println("Audio saved: output.wav (" + bytes + " bytes, encoding: linear16)");
    }
}