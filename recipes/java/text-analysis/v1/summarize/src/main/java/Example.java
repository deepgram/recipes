/**
 * Recipe: Text Summarization (Text Analysis v1)
 * Generates a concise summary from plain text using Deepgram's Read API.
 * Text analysis works directly on text — no audio required.
 * See also: text-analysis/v1/topics, text-analysis/v1/sentiment
 */
import com.deepgram.DeepgramClient;
import com.deepgram.resources.read.v1.text.requests.TextAnalyzeRequest;
import com.deepgram.resources.read.v1.text.types.TextAnalyzeRequestSummarize;
import com.deepgram.types.ReadV1Request;
import com.deepgram.types.ReadV1RequestText;
import com.deepgram.types.ReadV1Response;

public class Example {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("DEEPGRAM_API_KEY");
        if (apiKey == null) throw new RuntimeException("Set DEEPGRAM_API_KEY");

        DeepgramClient client = DeepgramClient.builder().apiKey(apiKey).build();

        String text = "Deepgram is an AI speech company that provides automatic speech recognition "
            + "and text-to-speech APIs. Their Nova-3 model offers state-of-the-art accuracy "
            + "for transcription. The company also provides audio intelligence features like "
            + "sentiment analysis, topic detection, and intent recognition. Developers can "
            + "integrate Deepgram into their applications using SDKs for Python, JavaScript, "
            + "Go, .NET, and other languages.";

        System.out.println("Analyzing: " + text.substring(0, Math.min(80, text.length())));
        ReadV1Response response = client.read().v1().text().analyze(
            TextAnalyzeRequest.builder()
                .body(ReadV1Request.of(ReadV1RequestText.builder().text(text).build()))
                .summarize(TextAnalyzeRequestSummarize.V2)  // <-- THIS enables summarization
                .language("en")
                .build());

        response.getResults().getSummary().ifPresent(s ->
            s.getResults().ifPresent(r ->
                r.getSummary().ifPresent(sum ->
                    sum.getText().ifPresent(t -> System.out.println("Summary: " + t)))));
    }
}