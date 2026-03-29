/**
 * Recipe: Language Detection (Speech-to-Text v1)
 * Automatically detects the spoken language in the audio.
 * The detected language code appears in the channel metadata.
 * See also: transcribe-url for basic transcription
 */
import DeepgramClient;
import java.util.Collections;
import resources.listen.v1.media.requests.ListenV1RequestUrl;
import resources.listen.v1.media.types.MediaTranscribeRequestModel;
import resources.listen.v1.media.types.MediaTranscribeResponse;
import types.ListenV1Response;

public class Example {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("DEEPGRAM_API_KEY");
        if (apiKey == null) throw new RuntimeException("Set DEEPGRAM_API_KEY");

        DeepgramClient client = DeepgramClient.builder().apiKey(apiKey).build();

        MediaTranscribeResponse result = client.listen().v1().media().transcribeUrl(
            ListenV1RequestUrl.builder()
                .url("https://dpgr.am/spacewalk.wav")
                .model(MediaTranscribeRequestModel.NOVA3)
                .detectLanguage(true)  // <-- THIS is the feature this recipe demonstrates
                .smartFormat(true)
                // Optional: language("en") to force a specific language instead
                .build());

        // Path: results.channels[0].detectedLanguage — the language code (e.g. "en")
        ListenV1Response response = (ListenV1Response) result.get();
        var channel = response.getResults().getChannels().get(0);
        channel.getDetectedLanguage().ifPresent(lang ->
            System.out.println("Detected language: " + lang));
        channel.getAlternatives().orElse(Collections.emptyList())
            .get(0).getTranscript().ifPresent(System.out::println);
    }
}