"""
Recipe: Function Calling (Voice Agents v1)
============================================
Demonstrates injecting tool/function definitions for the LLM to call
during a voice agent conversation.

Functions are defined in the think settings and, when the LLM invokes
one, a FunctionCallRequest event arrives. You respond with
send_function_call_response() so the LLM can incorporate the result
into its next spoken response.
"""

from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1FunctionCallRequest, AgentV1SendFunctionCallResponse,
    AgentV1Settings, AgentV1SettingsAgent,
    AgentV1SettingsAgentListen, AgentV1SettingsAgentListenProvider_V1,
    AgentV1SettingsAudio, AgentV1SettingsAudioInput,
)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi

WEATHER_FUNCTION = {
    "name": "get_weather",
    "description": "Get the current weather for a location",
    "parameters": {
        "type": "object",
        "properties": {"location": {"type": "string", "description": "City name"}},
        "required": ["location"],
    },
}


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    with client.agent.v1.connect() as agent:
        settings = AgentV1Settings(
            audio=AgentV1SettingsAudio(
                input=AgentV1SettingsAudioInput(encoding="linear16", sample_rate=24000)
            ),
            agent=AgentV1SettingsAgent(
                listen=AgentV1SettingsAgentListen(
                    provider=AgentV1SettingsAgentListenProvider_V1(type="deepgram", model="nova-3")
                ),
                think=ThinkSettingsV1(
                    provider=ThinkSettingsV1Provider_OpenAi(type="open_ai", model="gpt-4o-mini"),
                    prompt="You are a helpful assistant. Use get_weather when asked about weather.",
                    functions=[WEATHER_FUNCTION],  # <-- function definitions for the LLM
                ),
                speak=SpeakSettingsV1(
                    provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en")
                ),
            ),
        )

        agent.send_settings(settings)
        print("Agent configured with function calling (get_weather)")

        def on_message(message) -> None:
            if isinstance(message, AgentV1FunctionCallRequest):
                print(f"Function call: {message.name}")
                agent.send_function_call_response(
                    AgentV1SendFunctionCallResponse(
                        type="FunctionCallResponse", id=message.id,
                        name=message.name, content='{"temp": "72°F", "condition": "sunny"}',
                    )
                )
            elif isinstance(message, bytes):
                print(f"Received {len(message)} bytes of audio")
            else:
                print(f"Event: {getattr(message, 'type', type(message).__name__)}")

        agent.on(EventType.OPEN, lambda _: print("Connection opened"))
        agent.on(EventType.MESSAGE, on_message)
        agent.on(EventType.CLOSE, lambda _: print("Connection closed"))
        agent.start_listening()


if __name__ == "__main__":
    main()
