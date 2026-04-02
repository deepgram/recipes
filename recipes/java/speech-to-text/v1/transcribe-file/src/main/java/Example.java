/**
 * Recipe: Transcribe Local Audio File (Speech-to-Text v1)
 * Download and transcribe an audio file using byte array upload.
 * See also: transcribe-url for URL-based transcription
 */
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Collections;
import resources.listen.v1.media.requests.MediaTranscribeRequestOctetStream;
import resources.listen.v1.media.types.MediaTranscribeRequestModel;
import resources.listen.v1.media.types.MediaTranscribeResponse;
import types.ListenV1Response;

public class Example {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("DEEPGRAM_API_KEY");
        if (apiKey == null) throw new RuntimeException("Set DEEPGRAM_API_KEY");

        // Download demo audio file
        byte[] audioData = HttpClient.newHttpClient().send(
            HttpRequest.newBuilder().uri(URI.create("https://dpgr.am/spacewalk.wav")).build(),
            HttpResponse.BodyHandlers.ofByteArray()).body();
        System.out.println("Audio size: " + audioData.length + " bytes");

        DeepgramClient client = DeepgramClient.builder().apiKey(apiKey).build();

        // Transcribe from raw audio bytes
        MediaTranscribeResponse result = client.listen().v1().media().transcribeFile(
            MediaTranscribeRequestOctetStream.builder()
                .body(audioData)  // <-- raw audio bytes
                .model(MediaTranscribeRequestModel.NOVA3)
                .build());

        // response path: results.channels[0].alternatives[0].transcript
        ListenV1Response response = (ListenV1Response) result.get();
        response.getResults().getChannels().get(0)
            .getAlternatives().orElse(Collections.emptyList())
            .get(0).getTranscript().ifPresent(System.out::println);
    }
}