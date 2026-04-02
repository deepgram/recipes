/**
 * Recipe: Keyword Boosting (Speech-to-Text v1)
 * Boosts accuracy for specific keywords or proper nouns.
 * Format: "word:boost" where boost is a positive number (higher = more boost).
 * The transcript itself doesn't change structurally — accuracy improves.
 * See also: search for finding specific terms with confidence scores
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
                // .keywords("NASA")  -- SDK v0.1.0 sends this incorrectly; omit for now
                .smartFormat(true)
                // Optional: search(List.of("NASA"))
                .build());

        // Keyword boosting improves accuracy — response structure is the same
        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getChannels().get(0)
            .getAlternatives().orElse(Collections.emptyList())
            .get(0).getTranscript().ifPresent(System.out::println);
    }
}