/**
 * Recipe: Intent Recognition (Audio Intelligence v1)
 * Detects speaker intents from audio context with confidence scores.
 * See also: topics, sentiment, summarize for other intelligence features
 */
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
                .intents(true)  // <-- THIS enables intent recognition
                .smartFormat(true)
                .build());

        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getIntents().ifPresent(i ->
            i.getResults().ifPresent(r ->
                r.getIntents().ifPresent(intentsObj ->
                    intentsObj.getSegments().orElse(Collections.emptyList()).forEach(seg ->
                        seg.getIntents().orElse(Collections.emptyList()).forEach(intent ->
                            System.out.printf("Intent: %s (%.0f%%)%n",
                                intent.getIntent().orElse(""), intent.getConfidenceScore().orElse(0.0f) * 100))))));
    }
}