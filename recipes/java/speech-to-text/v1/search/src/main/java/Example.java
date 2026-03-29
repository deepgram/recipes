/**
 * Recipe: Search (Speech-to-Text v1)
 * Finds specific words or phrases in audio with confidence and timing.
 * Search results include hit positions with start/end times.
 * See also: keywords for boosting accuracy of specific terms
 */
import DeepgramClient;
import java.util.Collections;
import java.util.List;
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
                .search(List.of("NASA", "spacewalk"))  // <-- THIS is the feature
                .smartFormat(true)
                // Optional: keywords(List.of("NASA:2"))
                .build());

        // Path: results.channels[0].search[] — each has .query and .hits[]
        // Each hit has .confidence, .start, .end, .snippet
        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getChannels().get(0).getSearch()
            .orElse(Collections.emptyList()).forEach(s -> {
                System.out.println("Search: \"" + s.getQuery().orElse("") + "\"");
                s.getHits().orElse(Collections.emptyList()).forEach(h ->
                    System.out.printf("  Hit: %.0f%% at %.1fs%n",
                        h.getConfidence().orElse(0.0) * 100, h.getStart().orElse(0.0)));
            });
    }
}