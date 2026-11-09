"""Configure voice agent end-of-turn detection thresholds on the Flux listen
provider: eot_threshold (0.5-1.0), eager_eot_threshold (0.3-0.9), and
eot_timeout_ms (silence timeout in ms)."""
from typing import Union
from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1Settings, AgentV1SettingsAgent, AgentV1SettingsAgentListen,
    AgentV1SettingsAgentListenProvider_V2,
    AgentV1SettingsAudio, AgentV1SettingsAudioInput,
)
from deepgram.core.events import EventType
from deepgram.types import (
    SpeakSettingsV1, SpeakSettingsV1Provider_Deepgram,
    ThinkSettingsV1, ThinkSettingsV1Provider_OpenAi,
)

AgentResponse = Union[str, bytes]
client = DeepgramClient()

with client.agent.v1.connect() as agent:
    settings = AgentV1Settings(
        audio=AgentV1SettingsAudio(
            input=AgentV1SettingsAudioInput(encoding="linear16", sample_rate=24000)
        ),
        agent=AgentV1SettingsAgent(
            listen=AgentV1SettingsAgentListen(
                provider=AgentV1SettingsAgentListenProvider_V2(
                    type="deepgram", model="flux-general-en",
                    eot_threshold=0.8,
                    eager_eot_threshold=0.5,
                    eot_timeout_ms=3000,
                )
            ),
            think=ThinkSettingsV1(
                provider=ThinkSettingsV1Provider_OpenAi(type="open_ai", model="gpt-4o-mini"),
                prompt="You are a helpful assistant.",
            ),
            speak=SpeakSettingsV1(
                provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en")
            ),
        ),
    )
    agent.send_settings(settings)
    print("Endpointing configured: eot_threshold=0.8, eager_eot=0.5, timeout=3000ms")

    def on_message(message: AgentResponse) -> None:
        if isinstance(message, bytes):
            print(f"Received {len(message)} bytes of agent audio")
        else:
            print(f"Event: {getattr(message, 'type', type(message).__name__)}")

    agent.on(EventType.OPEN, lambda _: print("Connection opened"))
    agent.on(EventType.MESSAGE, on_message)
    agent.on(EventType.CLOSE, lambda _: print("Connection closed"))
    agent.start_listening()
