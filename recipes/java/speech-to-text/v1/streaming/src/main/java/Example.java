/**
 * Recipe: Live Streaming Transcription (Speech-to-Text v1)
 * WebSocket-based real-time transcription. Streams a file to simulate live audio.
 * See also: streaming-file, transcribe-url for pre-recorded
 */
import DeepgramClient;
import java.net.URI;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import resources.listen.v1.types.ListenV1CloseStream;
import resources.listen.v1.types.ListenV1CloseStreamType;
import resources.listen.v1.websocket.V1ConnectOptions;
import resources.listen.v1.websocket.V1WebSocketClient;
import types.ListenV1Model;

public class Example {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("DEEPGRAM_API_KEY");
        if (apiKey == null) throw new RuntimeException("Set DEEPGRAM_API_KEY");

        byte[] audio = URI.create("https://dpgr.am/spacewalk.wav").toURL().openStream().readAllBytes();
        CountDownLatch done = new CountDownLatch(1);
        DeepgramClient client = DeepgramClient.builder().apiKey(apiKey).build();
        V1WebSocketClient ws = client.listen().v1().v1WebSocket();

        ws.onResults(r -> {
            if (r.getIsFinal().orElse(false)) {
                String t = r.getChannel().getAlternatives().get(0).getTranscript();
                if (t != null && !t.isEmpty()) System.out.println(t);
            }
        });
        ws.onError(e -> System.err.println("Error: " + e.getMessage()));
        ws.onDisconnected(r -> done.countDown());

        ws.connect(V1ConnectOptions.builder()
            .model(ListenV1Model.NOVA3)  // <-- THIS: Nova-3 model for streaming
            .smartFormat(true).interimResults(true)
            .build()).get(10, TimeUnit.SECONDS);

        for (int i = 0; i < audio.length; i += 4096) {
            ws.sendMedia(java.util.Arrays.copyOfRange(audio, i, Math.min(i + 4096, audio.length)));
        }
        ws.sendCloseStream(ListenV1CloseStream.builder().type(ListenV1CloseStreamType.CLOSE_STREAM).build());
        done.await(30, TimeUnit.SECONDS);
        ws.disconnect();
    }
}