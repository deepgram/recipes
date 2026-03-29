/**
 * Recipe: Topic Detection (Speech-to-Text v1)
 * Identifies key topics discussed in the audio content.
 * Each segment gets a list of topics with confidence scores.
 * See also: intents for intent recognition, summarize for summaries
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
                .topics(true)  // <-- THIS is the feature this recipe demonstrates
                .smartFormat(true)
                // Optional: intents(true), sentiment(true), summarize("v2")
                .build());

        // Path: results.topics.segments[].topics[] — each has .topic and .confidence
        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getTopics().ifPresent(t ->
            t.getSegments().orElse(Collections.emptyList()).forEach(seg ->
                seg.getTopics().orElse(Collections.emptyList()).forEach(topic ->
                    System.out.printf("Topic: %s (%.0f%%)%n",
                        topic.getTopic().orElse(""), topic.getConfidence().orElse(0.0) * 100))));
    }
}