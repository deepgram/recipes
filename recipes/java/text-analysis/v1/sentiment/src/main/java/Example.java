/**
 * Recipe: Sentiment Analysis (Text Analysis v1)
 * Analyzes sentiment (positive/negative/neutral) on plain text using Deepgram's Read API.
 * Returns both per-segment sentiment and an overall average.
 * See also: text-analysis/v1/topics, text-analysis/v1/intents
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

        String text = "I absolutely love this product! It exceeded all my expectations. "
            + "However, the shipping was terrible and took three weeks to arrive. "
            + "Overall, I'm satisfied with my purchase despite the delivery issues.";

        System.out.println("Analyzing: " + text.substring(0, Math.min(80, text.length())));
        ReadV1Response response = client.read().v1().text().analyze(
            TextAnalyzeRequest.builder()
                .body(ReadV1Request.of(ReadV1RequestText.builder().text(text).build()))
                .sentiment(true)  // <-- THIS enables sentiment analysis on plain text
                .language("en")
                .build());

        response.getResults().getSentiments().ifPresent(sentiments -> {
            sentiments.getAverage().ifPresent(avg ->
                System.out.printf("Average: %s (%.2f)%n",
                    avg.getSentiment().orElse(""), avg.getSentimentScore().orElse(0.0)));
            sentiments.getSegments().orElse(Collections.emptyList()).forEach(seg ->
                System.out.printf("[%s] %s%n",
                    seg.getSentiment().orElse(""), seg.getText().orElse("")));
        });
    }
}