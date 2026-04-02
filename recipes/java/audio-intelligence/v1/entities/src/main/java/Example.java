/**
 * Recipe: Entity Detection (Audio Intelligence v1)
 * Identifies named entities: people, organisations, locations in audio.
 * See also: topics, sentiment for other intelligence features
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
                .detectEntities(true)  // <-- THIS enables entity detection
                .smartFormat(true)
                .build());

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