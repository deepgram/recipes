/**
 * Recipe: Configure TTS Voice (Voice Agents v1)
 * Choose a specific aura-2 voice model for agent speech output.
 * See also: connect for basic setup, custom-llm for LLM selection
 */
import DeepgramClient;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import resources.agent.v1.types.*;
import resources.agent.v1.websocket.V1WebSocketClient;
import types.*;

public class Example {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("DEEPGRAM_API_KEY");
        if (apiKey == null) throw new RuntimeException("Set DEEPGRAM_API_KEY");

        DeepgramClient client = DeepgramClient.builder().apiKey(apiKey).build();
        V1WebSocketClient ws = client.agent().v1().v1WebSocket();
        CountDownLatch done = new CountDownLatch(1);

        ws.onWelcome(w -> {
            System.out.println("Agent connected: " + w.getRequestId());
            ws.sendSettings(AgentV1Settings.builder()
                .audio(AgentV1SettingsAudio.builder().build())
                .agent(AgentV1SettingsAgent.of(AgentV1SettingsAgentContext.builder()
                    .think(AgentV1SettingsAgentContextThink.of(ThinkSettingsV1.builder()
                        .provider(ThinkSettingsV1Provider.openAi(OpenAiThinkProvider.builder()
                            .model(OpenAiThinkProviderModel.GPT4O_MINI).build()))
                        .prompt("You are a helpful assistant.").build()))
                    .speak(AgentV1SettingsAgentContextSpeak.of(SpeakSettingsV1.builder()
                        .provider(SpeakSettingsV1Provider.deepgram(types.Deepgram.builder()
                            .model(DeepgramSpeakProviderModel.AURA2ASTERIA_EN)  // <-- THIS: voice model
                            .build())).build()))
                    .greeting("Hello! I'm using the Asteria voice.").build()))
                .build());
        });
        ws.onSettingsApplied(s -> { System.out.println("Settings applied (Asteria voice)"); done.countDown(); });
        ws.onError(e -> { System.err.println("Error: " + e.getMessage()); done.countDown(); });

        ws.connect().get(10, TimeUnit.SECONDS);
        done.await(15, TimeUnit.SECONDS);
        ws.disconnect();
    }
}