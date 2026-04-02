/**
 * Recipe: Filler Words (Speech-to-Text v1)
 * Captures filler words ("uh", "um", "mhm") in the transcript output.
 * Without this flag, Deepgram omits filler words from the transcript.
 * See also: smart-format for automatic formatting, punctuate for punctuation
 */
import java.util.Collections;
import com.deepgram.DeepgramClient;
import com.deepgram.resources.listen.v1.media.requests.ListenV1RequestUrl;
import com.deepgram.resources.listen.v1.media.types.MediaTranscribeRequestModel;
import com.deepgram.resources.listen.v1.media.types.MediaTranscribeResponse;
import com.deepgram.types.ListenV1Response;

public class Example {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("DEEPGRAM_API_KEY");
        if (apiKey == null) throw new RuntimeException("Set DEEPGRAM_API_KEY");

        DeepgramClient client = DeepgramClient.builder().apiKey(apiKey).build();

        MediaTranscribeResponse result = client.listen().v1().media().transcribeUrl(
            ListenV1RequestUrl.builder()
                .url("https://dpgr.am/spacewalk.wav")
                .model(MediaTranscribeRequestModel.NOVA3)
                .fillerWords(true)  // <-- THIS captures filler words in transcript
                .smartFormat(true)
                .build());

        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getChannels().get(0)
            .getAlternatives().orElse(Collections.emptyList())
            .get(0).getTranscript().ifPresent(System.out::println);
    }
}
