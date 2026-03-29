/**
 * Recipe: Function Calling (Voice Agents v1)
 * Configures the voice agent with a tool definition for function calling.
 * The LLM can invoke defined functions during conversation.
 * See also: connect for basic setup, custom-llm for provider selection
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
                        .prompt("You can look up weather using the get_weather function.").build()))
                    .greeting("Hello! I can check the weather for you.").build()))
                .build());
        });
        ws.onSettingsApplied(s -> { System.out.println("Settings applied with function calling"); done.countDown(); });
        ws.onFunctionCallRequest(f -> System.out.println("Function call: " + f));  // <-- THIS: handle function calls
        ws.onError(e -> { System.err.println("Error: " + e.getMessage()); done.countDown(); });

        ws.connect().get(10, TimeUnit.SECONDS);
        done.await(15, TimeUnit.SECONDS);
        ws.disconnect();
    }
}