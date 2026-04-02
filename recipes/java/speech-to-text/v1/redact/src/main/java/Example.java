/**
 * Recipe: Redaction (Speech-to-Text v1)
 * Redacts sensitive information (PCI, PII, SSNs) from the transcript.
 * Redacted content appears as [REDACTED] in the transcript text.
 * See also: detect-entities for entity identification without redaction
 */
import java.util.Collections;
import java.util.List;
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
                .redact("pci") // SDK v0.1.0 supports one redaction at a time  // <-- THIS is the feature this recipe demonstrates
                .smartFormat(true)
                // Optional: detectEntities(true)
                .build());

        // Transcript will have [REDACTED] in place of sensitive info
        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getChannels().get(0)
            .getAlternatives().orElse(Collections.emptyList())
            .get(0).getTranscript().ifPresent(System.out::println);
    }
}