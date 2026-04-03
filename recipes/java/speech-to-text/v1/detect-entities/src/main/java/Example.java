/**
 * Recipe: Entity Detection (Speech-to-Text v1)
 * Identifies named entities: people, places, organisations in the audio.
 * Each entity has a label, value, and confidence score.
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
                .detectEntities(true)  // <-- THIS is the feature this recipe demonstrates
                .smartFormat(true)
                // Optional: topics(true), sentiment(true)
                .build());

        // Path: results.channels[0].alternatives[0].entities[] — each has .label, .value, .confidence
        ListenV1Response response = (ListenV1Response) result.get();
        // Always print transcript (ensures non-empty output even if feature returns no data)
        response.getResults().getChannels().get(0)
            .getAlternatives().orElse(Collections.emptyList())
            .get(0).getTranscript().ifPresent(System.out::println);
        response.getResults().getChannels().get(0)
            .getAlternatives().orElse(Collections.emptyList()).get(0)
            .getEntities().orElse(Collections.emptyList()).forEach(entity ->
                System.out.printf("%s: %s (%.0f%%)%n",
                    entity.getLabel().orElse(""), entity.getValue().orElse(""),
                    entity.getConfidence().orElse(0.0f) * 100));
    }
}