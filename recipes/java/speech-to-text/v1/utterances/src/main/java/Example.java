/**
 * Recipe: Utterances (Speech-to-Text v1)
 * Splits transcript into per-utterance segments with start/end timing.
 * Each utterance represents a continuous speech segment.
 * See also: paragraphs for paragraph-based grouping, diarize for speaker labels
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
                .utterances(true)  // <-- THIS is the feature this recipe demonstrates
                .smartFormat(true)
                // Optional: diarize(true), punctuate(true)
                .build());

        // Path: results.utterances[] — each has .start, .end, .transcript, .speaker
        // Utterances may be empty for very short audio clips
        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getUtterances().orElse(Collections.emptyList()).forEach(u ->
            System.out.printf("[%.1fs-%.1fs] %s%n",
                u.getStart().orElse(0.0), u.getEnd().orElse(0.0),
                u.getTranscript().orElse("")));
    }
}