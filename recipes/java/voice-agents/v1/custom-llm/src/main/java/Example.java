/**
 * Recipe: Configure LLM Provider (Voice Agents v1)
 * Use Anthropic Claude as the think model for your voice agent.
 * See also: connect for basic setup, custom-tts for voice selection
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
                        .provider(ThinkSettingsV1Provider.anthropic(Anthropic.builder()
                            .model(AnthropicThinkProviderModel.CLAUDE_SONNET420250514)  // <-- THIS: Anthropic LLM
                            .build()))
                        .prompt("You are a helpful voice assistant. Keep responses brief.").build()))
                    .greeting("Hello! I'm powered by Claude.").build()))
                .build());
        });
        ws.onSettingsApplied(s -> { System.out.println("Settings applied (Anthropic Claude)"); done.countDown(); });
        ws.onError(e -> { System.err.println("Error: " + e.getMessage()); done.countDown(); });

        ws.connect().get(10, TimeUnit.SECONDS);
        done.await(15, TimeUnit.SECONDS);
        ws.disconnect();
    }
}