/**
 * Recipe: Speaker Diarization (Speech-to-Text v1)
 * Identifies and labels individual speakers in audio.
 * Each word in the transcript gets a speaker label (speaker 0, 1, 2...).
 * See also: utterances for segment-level timing, paragraphs for grouping
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
                .diarize(true)  // <-- THIS is the feature this recipe demonstrates
                .smartFormat(true)
                // Optional: utterances(true), paragraphs(true)
                .build());

        // Path: results.channels[0].alternatives[0].words[] — each word has .speaker
        ListenV1Response response = (ListenV1Response) result.get();
        var words = response.getResults().getChannels().get(0)
            .getAlternatives().orElse(Collections.emptyList()).get(0)
            .getWords().orElse(Collections.emptyList());
        int lastSpeaker = -1;
        for (var w : words) {
            int speaker = w.getSpeaker().orElse(0.0).intValue();
            if (speaker != lastSpeaker) {
                if (lastSpeaker >= 0) System.out.println();
                System.out.print("[Speaker " + speaker + "] ");
                lastSpeaker = speaker;
            }
            System.out.print(w.getWord().orElse("") + " ");
        }
        System.out.println();
    }
}