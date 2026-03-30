"""
Recipe: Configure LLM Provider (Voice Agents v1)
==================================================
Demonstrates using a specific LLM provider for the voice agent's
"think" stage, where it generates responses.

You can use OpenAI or Anthropic as the LLM provider. This recipe
shows how to configure an OpenAI model with custom temperature and
a system prompt.
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
                    provider=ThinkSettingsV1Provider_OpenAi(
                        type="open_ai",
                        model="gpt-4o-mini",  # <-- THIS selects the LLM.
                        temperature=0.7,       # Control response creativity.
                    ),
                    prompt="You are a knowledgeable space exploration expert.",
                ),
                speak=SpeakSettingsV1(
                    provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en")
                ),
            ),
        )

        agent.send_settings(settings)
        print("Agent configured with OpenAI gpt-4o-mini as think provider")

        agent.on(EventType.OPEN, lambda _: print("Connection opened"))
        agent.on(EventType.CLOSE, lambda _: print("Connection closed"))
        agent.start_listening()


if __name__ == "__main__":
    main()
