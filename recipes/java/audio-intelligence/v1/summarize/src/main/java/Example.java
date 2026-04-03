/**
 * Recipe: Audio Summarization (Audio Intelligence v1)
 * Generates a concise text summary of spoken audio content.
 * Uses the speech-to-text API with summarize="v2" to produce a summary.
 * See also: speech-to-text/v1/summarize (same feature via STT)
 */
import resources.listen.v1.media.requests.ListenV1RequestUrl;
import resources.listen.v1.media.types.MediaTranscribeRequestModel;
import resources.listen.v1.media.types.MediaTranscribeRequestSummarize;
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
                .summarize(MediaTranscribeRequestSummarize.V2)  // <-- THIS enables audio summarization
                .smartFormat(true)
                .build());

        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getSummary().ifPresent(s ->
            s.getShort().ifPresent(text -> System.out.println("Summary: " + text)));
    }
}