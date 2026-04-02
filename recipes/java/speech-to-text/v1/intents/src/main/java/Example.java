/**
 * Recipe: Intent Recognition (Speech-to-Text v1)
 * Detects speaker intents from the audio content.
 * Each segment gets a list of intents with confidence scores.
 * See also: topics for topic detection, sentiment for sentiment analysis
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
                .intents(true)  // <-- THIS is the feature this recipe demonstrates
                .smartFormat(true)
                // Optional: topics(true), sentiment(true), summarize("v2")
                .build());

        // Print transcript first (always produces output regardless of intent detection)
        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getChannels().get(0)
            .getAlternatives().orElse(Collections.emptyList())
            .get(0).getTranscript().ifPresent(System.out::println);

        // Path: results.intents.results.intents.segments[].intents[] — each has .intent and .confidenceScore
        response.getResults().getIntents().ifPresent(i ->
            i.getResults().ifPresent(r ->
                r.getIntents().ifPresent(intentsObj ->
                    intentsObj.getSegments().orElse(Collections.emptyList()).forEach(seg ->
                        seg.getIntents().orElse(Collections.emptyList()).forEach(intent ->
                            System.out.printf("Intent: %s (%.0f%%)%n",
                                intent.getIntent().orElse(""), intent.getConfidenceScore().orElse(0.0f) * 100))))));
    }
}