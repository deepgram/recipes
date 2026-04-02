/**
 * Recipe: Topic Detection (Text Analysis v1)
 * Identifies topics discussed in plain text using Deepgram's Read API.
 * Returns per-segment topic lists with confidence scores.
 * See also: text-analysis/v1/intents, text-analysis/v1/sentiment
 */
import java.util.Collections;
import com.deepgram.DeepgramClient;
import com.deepgram.resources.read.v1.text.requests.TextAnalyzeRequest;
import com.deepgram.types.ReadV1Request;
import com.deepgram.types.ReadV1RequestText;
import com.deepgram.types.ReadV1Response;

public class Example {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("DEEPGRAM_API_KEY");
        if (apiKey == null) throw new RuntimeException("Set DEEPGRAM_API_KEY");

        DeepgramClient client = DeepgramClient.builder().apiKey(apiKey).build();

        String text = "The new electric vehicle from Tesla features a range of 400 miles "
            + "and uses a revolutionary battery technology. Meanwhile, SpaceX "
            + "successfully launched another batch of Starlink satellites into orbit. "
            + "In healthcare news, a new mRNA vaccine shows promising results in "
            + "early clinical trials for treating certain types of cancer.";

        System.out.println("Analyzing: " + text.substring(0, Math.min(80, text.length())));
        ReadV1Response response = client.read().v1().text().analyze(
            TextAnalyzeRequest.builder()
                .body(ReadV1Request.of(ReadV1RequestText.builder().text(text).build()))
                .topics(true)  // <-- THIS enables topic detection on plain text
                .language("en")
                .build());

        response.getResults().getTopics().ifPresent(topics ->
            topics.getResults().ifPresent(r ->
                r.getTopics().ifPresent(t ->
                    t.getSegments().orElse(Collections.emptyList()).forEach(seg -> {
                        System.out.println("Text: " + seg.getText().orElse(""));
                        seg.getTopics().orElse(Collections.emptyList()).forEach(topic ->
                            System.out.printf("  Topic: %s (%.0f%%)%n",
                                topic.getTopic().orElse(""),
                                topic.getConfidenceScore().orElse(0f) * 100));
                    }))));
    }
}