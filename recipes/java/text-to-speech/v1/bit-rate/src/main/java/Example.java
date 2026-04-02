/**
 * Recipe: Bit Rate Control (Text-to-Speech v1)
 * Controls the output audio bit rate for compressed encodings like mp3.
 * Lower bit rates produce smaller files; higher bit rates improve quality.
 * See also: select-encoding for encoding options, generate-audio for basics
 */
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import resources.speak.v1.audio.requests.SpeakV1Request;
import resources.speak.v1.audio.types.AudioGenerateRequestEncoding;
import resources.speak.v1.audio.types.AudioGenerateRequestModel;

public class Example {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("DEEPGRAM_API_KEY");
        if (apiKey == null) throw new RuntimeException("Set DEEPGRAM_API_KEY");

        DeepgramClient client = DeepgramClient.builder().apiKey(apiKey).build();

        InputStream audio = client.speak().v1().audio().generate(
            SpeakV1Request.builder()
                .text("Hello from Deepgram! This audio uses a custom bit rate.")
                .model(AudioGenerateRequestModel.AURA2THALIA_EN)
                .encoding(AudioGenerateRequestEncoding.MP3)
                .bitRate(48000.0)  // <-- THIS sets the output bit rate (48 kbps)
                .build());

        long bytes = Files.copy(audio, Path.of("output.mp3"), StandardCopyOption.REPLACE_EXISTING);
        audio.close();
        System.out.println("Audio saved: output.mp3 (" + bytes + " bytes, bit rate: 48 kbps)");
    }
}