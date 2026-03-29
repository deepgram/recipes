/**
 * Recipe: Sentiment Analysis (Speech-to-Text v1)
 * Analyzes sentiment (positive/negative/neutral) per transcript segment.
 * Each segment has a sentiment value and confidence score plus the text.
 * See also: topics for topic detection, intents for intent recognition
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
                .sentiment(true)  // <-- THIS is the feature this recipe demonstrates
                .smartFormat(true)
                // Optional: topics(true), intents(true), summarize("v2")
                .build());

        // Path: results.sentiments.segments[] — each has .sentiment.value, .text
        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getSentiments().ifPresent(s ->
            s.getSegments().orElse(Collections.emptyList()).forEach(seg ->
                System.out.printf("[%s] %s%n",
                    seg.getSentiment().map(sent -> sent.toString()).orElse("unknown"),
                    seg.getText().orElse(""))));
    }
}