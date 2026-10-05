"""
Recipe: Greeting and Persona (Voice Agents v1)
================================================
Configure a voice agent with a custom greeting message and a
system prompt that defines its personality, topic scope, and
behavioral constraints.
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

PERSONA = (
    "You are Nova, a friendly space exploration guide. "
    "Speak in a warm, enthusiastic tone. Only discuss space, astronomy, and NASA missions. "
    "If asked about unrelated topics, politely redirect. Keep responses to two sentences."
)

def main():
    client = DeepgramClient()

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
                    prompt=PERSONA,
                ),
                speak=SpeakSettingsV1(
                    provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en")
                ),
                greeting="Hello! I'm Nova, your space exploration guide. Ask me anything about the cosmos!",
            ),
        )

        agent.send_settings(settings)
        print("Agent configured with custom greeting and persona")
        print(f"Greeting: {settings.agent.greeting}")
        print(f"Persona: {PERSONA[:60]}...")

        agent.on(EventType.OPEN, lambda _: print("Connection opened"))
        agent.on(EventType.CLOSE, lambda _: print("Connection closed"))
        agent.start_listening()


if __name__ == "__main__":
    main()
