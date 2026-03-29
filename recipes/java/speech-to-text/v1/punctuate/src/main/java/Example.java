/**
 * Recipe: Punctuation (Speech-to-Text v1)
 * Adds punctuation (periods, commas, question marks) to the transcript.
 * Without punctuate: "hello how are you doing today"
 * With punctuate:    "Hello, how are you doing today?"
 * See also: smart-format which includes punctuation plus number formatting
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
                .punctuate(true)  // <-- THIS is the feature this recipe demonstrates
                // Optional: smartFormat(true), language("en")
                .build());

        // Transcript will include periods, commas, question marks
        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getChannels().get(0)
            .getAlternatives().orElse(Collections.emptyList())
            .get(0).getTranscript().ifPresent(System.out::println);
    }
}