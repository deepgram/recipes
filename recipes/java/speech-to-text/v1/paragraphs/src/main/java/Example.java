/**
 * Recipe: Paragraphs (Speech-to-Text v1)
 * Groups transcript into paragraph blocks based on speech pauses.
 * Without paragraphs: flat transcript string.
 * With paragraphs: structured paragraph objects with sentences and timing.
 * Paragraphs may be absent if audio is too short.
 * See also: utterances for speaker-turn-based segmentation
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
                .paragraphs(true)  // <-- THIS is the feature this recipe demonstrates
                .smartFormat(true)
                // Optional: punctuate(true), utterances(true)
                .build());

        // Path: results.channels[0].alternatives[0].paragraphs.paragraphs[].sentences[].text
        ListenV1Response response = (ListenV1Response) result.get();
        var alt = response.getResults().getChannels().get(0)
            .getAlternatives().orElse(Collections.emptyList()).get(0);
        alt.getParagraphs().ifPresent(p -> p.getParagraphs().orElse(Collections.emptyList())
            .forEach(para -> {
                para.getSentences().orElse(Collections.emptyList())
                    .forEach(s -> s.getText().ifPresent(t -> System.out.print(t + " ")));
                System.out.println("\n");
            }));
    }
}