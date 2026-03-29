/**
 * Recipe: WebSocket Streaming TTS (Text-to-Speech v1)
 * Low-latency TTS via WebSocket for real-time use cases.
 * Send text chunks, receive audio data in real time.
 * See also: generate-audio for REST, stream-audio for REST streaming
 */
import DeepgramClient;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;
import resources.speak.v1.types.*;
import resources.speak.v1.websocket.V1WebSocketClient;

public class Example {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("DEEPGRAM_API_KEY");
        if (apiKey == null) throw new RuntimeException("Set DEEPGRAM_API_KEY");

        DeepgramClient client = DeepgramClient.builder().apiKey(apiKey).build();
        V1WebSocketClient ws = client.speak().v1().v1WebSocket();
        CountDownLatch done = new CountDownLatch(1);
        AtomicInteger bytes = new AtomicInteger(0);

        ws.onSpeakV1Audio(data -> bytes.addAndGet(data.toByteArray().length));
        ws.onFlushed(f -> System.out.println("Flushed — audio generated"));
        ws.onDisconnected(r -> done.countDown());

        ws.connect().get(10, TimeUnit.SECONDS);  // <-- THIS: WebSocket TTS connection
        ws.sendText(SpeakV1Text.builder().text("Hello from Deepgram! WebSocket TTS.").build());
        ws.sendFlush(SpeakV1Flush.builder().type(SpeakV1FlushType.FLUSH).build());
        Thread.sleep(3000);
        ws.sendClose(SpeakV1Close.builder().type(SpeakV1CloseType.CLOSE).build());
        done.await(10, TimeUnit.SECONDS);
        ws.disconnect();
        System.out.println("Received " + bytes.get() + " bytes of audio");
    }
}