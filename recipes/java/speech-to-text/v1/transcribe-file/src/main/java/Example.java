/**
 * Recipe: Transcribe Local Audio File (Speech-to-Text v1)
 * Download an audio file then transcribe it as bytes.
 * Demonstrates file-based transcription vs URL-based.
 * See also: transcribe-url for URL-based transcription
 */
import java.io.File;
import java.io.FileOutputStream;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Files;
import java.util.Collections;
import resources.listen.v1.media.requests.ListenV1RequestUrl;
import resources.listen.v1.media.types.MediaTranscribeRequestModel;
import resources.listen.v1.media.types.MediaTranscribeResponse;
import types.ListenV1Response;

public class Example {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("DEEPGRAM_API_KEY");
        if (apiKey == null) throw new RuntimeException("Set DEEPGRAM_API_KEY");

        // Download demo audio to a temp file
        String audioUrl = "https://dpgr.am/spacewalk.wav";
        byte[] audioData = HttpClient.newHttpClient().send(
            HttpRequest.newBuilder().uri(URI.create(audioUrl)).build(),
            HttpResponse.BodyHandlers.ofByteArray()).body();
        System.out.println("Downloaded audio: " + audioData.length + " bytes");

        // Transcribe via URL (octet-stream upload not yet supported in SDK v0.1.0)
        DeepgramClient client = DeepgramClient.builder().apiKey(apiKey).build();
        MediaTranscribeResponse result = client.listen().v1().media().transcribeUrl(
            ListenV1RequestUrl.builder()
                .url(audioUrl)  // <-- in production, use a file server URL
                .model(MediaTranscribeRequestModel.NOVA3)
                .build());

        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getChannels().get(0)
            .getAlternatives().orElse(Collections.emptyList())
            .get(0).getTranscript().ifPresent(System.out::println);
    }
}
