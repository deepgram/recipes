/**
 * Recipe: Summarize (Speech-to-Text v1)
 * Generates a concise summary of the transcript content.
 * The summary is returned as a short text string alongside the full transcript.
 * See also: topics for topic detection, intents for intent recognition
 */
import DeepgramClient;
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
                .summarize("v2")  // <-- THIS is the feature this recipe demonstrates
                .smartFormat(true)
                // Optional: topics(true), intents(true), sentiment(true)
                .build());

        // Path: results.summary.short — the summary text
        // Summary may be absent for very short audio clips
        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getSummary().ifPresent(s ->
            s.getShort().ifPresent(text -> System.out.println("Summary: " + text)));
    }
}