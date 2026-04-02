/**
 * Recipe: Speaker Diarization (Speech-to-Text v1)
 * Identifies and labels individual speakers in audio.
 * Each word in the transcript gets a speaker label (speaker 0, 1, 2...).
 * See also: utterances for segment-level timing, paragraphs for grouping
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
                .diarize(true)  // <-- THIS is the feature this recipe demonstrates
                .utterances(true)  // utterances carry speaker labels
                .smartFormat(true)
                // Optional: paragraphs(true)
                .build());

        // Path: results.utterances[] — each utterance has .speaker and .transcript
        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getUtterances().orElse(Collections.emptyList()).forEach(u -> {
            int speaker = u.getSpeaker().orElse(0.0f).intValue();
            System.out.printf("[Speaker %d] %s%n", speaker, u.getTranscript().orElse(""));
        });
    }
}