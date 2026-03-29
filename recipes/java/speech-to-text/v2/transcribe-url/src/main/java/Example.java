/**
 * Recipe: Transcribe Audio from URL (Speech-to-Text v2)
 * Uses the flux-general-en model for high-accuracy English transcription.
 * The v2 model is accessed via the v1 REST endpoint with model="flux-general-en".
 * See also: speech-to-text/v1/transcribe-url for Nova-3, v2/streaming for WebSocket
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
                .model(MediaTranscribeRequestModel.of("flux-general-en"))  // <-- THIS: v2 flux model
                .smartFormat(true)
                // Optional: punctuate(true), paragraphs(true)
                .build());

        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getChannels().get(0)
            .getAlternatives().orElse(Collections.emptyList())
            .get(0).getTranscript().ifPresent(System.out::println);
    }
}
