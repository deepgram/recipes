"""
Recipe: Configure TTS Voice (Voice Agents v1)
===============================================
Demonstrates choosing a specific aura-2 voice model for the agent's
"speak" stage.

The speak provider controls how the agent's responses sound. Changing
the model parameter lets you pick from different voice personalities —
e.g., warm and conversational, or deep and authoritative.
"""

from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1Settings, AgentV1SettingsAgent,
    AgentV1SettingsAgentListen, AgentV1SettingsAgentListenProvider_V1,
    AgentV1SettingsAudio, AgentV1SettingsAudioInput,
)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi


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
                    prompt="You are a helpful assistant.",
                ),
                speak=SpeakSettingsV1(
                    provider=SpeakSettingsV1Provider_Deepgram(
                        type="deepgram",
                        model="aura-2-arcas-en",  # <-- THIS selects the agent's voice.
                    )
                ),
            ),
        )

        agent.send_settings(settings)
        print("Agent configured with aura-2-arcas-en voice")

        agent.on(EventType.OPEN, lambda _: print("Connection opened"))
        agent.on(EventType.CLOSE, lambda _: print("Connection closed"))
        agent.start_listening()


if __name__ == "__main__":
    main()
