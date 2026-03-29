/**
 * Recipe: Smart Format (Speech-to-Text v1)
 * Automatically formats numbers, dates, currencies, and addresses.
 * Without smart_format: "three hundred dollars"
 * With smart_format:    "$300"
 * smart_format is a superset of punctuate + numerals.
 * See also: punctuate for punctuation-only formatting
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
                .smartFormat(true)  // <-- THIS is the feature this recipe demonstrates
                // Optional: language("en"), punctuate(true) (already included in smartFormat)
                .build());

        // The transcript contains formatted text — "$300" instead of "three hundred dollars"
        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getChannels().get(0)
            .getAlternatives().orElse(Collections.emptyList())
            .get(0).getTranscript().ifPresent(System.out::println);
    }
}