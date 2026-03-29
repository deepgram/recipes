/**
 * Recipe: Stream Audio File for Transcription (Speech-to-Text v1)
 * Streams a local audio file over WebSocket for real-time transcription.
 * This downloads a demo file then streams it in chunks.
 * See also: streaming for live mic input, transcribe-file for REST upload
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
        System.out.println("Streaming " + audio.length + " bytes");
        CountDownLatch done = new CountDownLatch(1);
        DeepgramClient client = DeepgramClient.builder().apiKey(apiKey).build();
        V1WebSocketClient ws = client.listen().v1().v1WebSocket();

        ws.onResults(r -> {
            if (r.getIsFinal().orElse(false)) {
                String t = r.getChannel().getAlternatives().get(0).getTranscript();
                if (t != null && !t.isEmpty()) System.out.println(t);
            }
        });
        ws.onDisconnected(r -> done.countDown());

        ws.connect(V1ConnectOptions.builder().model(ListenV1Model.NOVA3)
            .smartFormat(true).build()).get(10, TimeUnit.SECONDS);

        for (int i = 0; i < audio.length; i += 4096) {
            ws.sendMedia(java.util.Arrays.copyOfRange(audio, i, Math.min(i + 4096, audio.length)));
        }
        ws.sendCloseStream(ListenV1CloseStream.builder().type(ListenV1CloseStreamType.CLOSE_STREAM).build());
        done.await(30, TimeUnit.SECONDS);
        ws.disconnect();
    }
}