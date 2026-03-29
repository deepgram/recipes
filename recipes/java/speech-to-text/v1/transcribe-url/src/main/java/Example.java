/**
 * Recipe: Transcribe Audio from URL (Speech-to-Text v1)
 * Send a URL pointing to a hosted audio file for transcription.
 * This is the foundation recipe — all other STT recipes build on this pattern.
 * See also: transcribe-file, smart-format, paragraphs, diarize
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

        // Transcribe audio from a public URL
        MediaTranscribeResponse result = client.listen().v1().media().transcribeUrl(
            ListenV1RequestUrl.builder()
                .url("https://dpgr.am/spacewalk.wav")
                .model(MediaTranscribeRequestModel.NOVA3) // <-- highest-accuracy model
                .smartFormat(true)
                // Optional: language("en"), punctuate(true), diarize(true)
                .build());

        // result.get() returns ListenV1Response for synchronous requests
        // response.getResults().getChannels() -> list of channels
        //   channel.getAlternatives() -> Optional list of alternatives
        //     alternative.getTranscript() -> Optional<String>
        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getChannels().get(0)
            .getAlternatives().orElse(Collections.emptyList())
            .get(0).getTranscript().ifPresent(System.out::println);
    }
}