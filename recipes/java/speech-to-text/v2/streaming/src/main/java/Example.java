/**
 * Recipe: Live Streaming Transcription (Speech-to-Text v2)
 * V2 WebSocket with flux-general-en model for turn-based transcription.
 * V2 provides turn info events instead of interim/final results.
 * See also: speech-to-text/v1/streaming for V1 API
 */
import DeepgramClient;
import java.net.URI;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import resources.listen.v2.types.ListenV2CloseStream;
import resources.listen.v2.types.ListenV2CloseStreamType;
import resources.listen.v2.websocket.V2ConnectOptions;
import resources.listen.v2.websocket.V2WebSocketClient;

public class Example {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("DEEPGRAM_API_KEY");
        if (apiKey == null) throw new RuntimeException("Set DEEPGRAM_API_KEY");

        byte[] audio = URI.create("https://dpgr.am/spacewalk.wav").toURL().openStream().readAllBytes();
        CountDownLatch done = new CountDownLatch(1);
        DeepgramClient client = DeepgramClient.builder().apiKey(apiKey).build();
        V2WebSocketClient ws = client.listen().v2().v2WebSocket();

        ws.onTurnInfo(t -> {
            String transcript = t.getTranscript();
            if (transcript != null && !transcript.isEmpty())
                System.out.printf("[turn %.0f] %s%n", t.getTurnIndex(), transcript);
        });
        ws.onDisconnected(r -> done.countDown());

        ws.connect(V2ConnectOptions.builder()
            .model("flux-general-en")  // <-- THIS: V2 flux model
            .build()).get(10, TimeUnit.SECONDS);

        for (int i = 0; i < audio.length; i += 4096) {
            ws.sendMedia(java.util.Arrays.copyOfRange(audio, i, Math.min(i + 4096, audio.length)));
        }
        ws.sendCloseStream(ListenV2CloseStream.builder().type(ListenV2CloseStreamType.CLOSE_STREAM).build());
        done.await(30, TimeUnit.SECONDS);
        ws.disconnect();
    }
}