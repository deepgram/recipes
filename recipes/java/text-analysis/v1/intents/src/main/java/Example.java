/**
 * Recipe: Intent Recognition (Text Analysis v1)
 * Detects speaker intents from plain text input using Deepgram's Read API.
 * Text analysis works directly on text — no audio required.
 * See also: text-analysis/v1/topics, text-analysis/v1/sentiment
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

        String text = "I'd like to return this product and get a refund. "
            + "The item arrived damaged and I'm very disappointed with the quality. "
            + "Can you also update my shipping address for future orders?";

        System.out.println("Analyzing: " + text.substring(0, Math.min(80, text.length())));
        ReadV1Response response = client.read().v1().text().analyze(
            TextAnalyzeRequest.builder()
                .body(ReadV1Request.of(ReadV1RequestText.builder().text(text).build()))
                .intents(true)  // <-- THIS enables intent recognition on plain text
                .language("en")
                .build());

        response.getResults().getIntents().ifPresent(intents ->
            intents.getResults().ifPresent(r ->
                r.getIntents().ifPresent(i ->
                    i.getSegments().orElse(Collections.emptyList()).forEach(seg -> {
                        System.out.println("Text: " + seg.getText().orElse(""));
                        seg.getIntents().orElse(Collections.emptyList()).forEach(intent ->
                            System.out.printf("  Intent: %s (%.0f%%)%n",
                                intent.getIntent().orElse(""),
                                intent.getConfidenceScore().orElse(0f) * 100));
                    }))));
    }
}