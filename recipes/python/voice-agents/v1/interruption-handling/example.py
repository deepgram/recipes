"""
Recipe: Interruption Handling & Silence Detection (Voice Agents v1)
Configures endpointing, utterance_end_ms, and vad_events so the agent
stops speaking when the user starts talking (barge-in).
"""

from typing import Union
from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1Settings, AgentV1SettingsAgent, AgentV1SettingsAgentListen,
    AgentV1SettingsAgentListenProvider_V1, AgentV1SettingsAudio, AgentV1SettingsAudioInput,
)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi

def main():
    client = DeepgramClient()
    with client.agent.v1.connect() as agent:
        settings = AgentV1Settings(
            audio=AgentV1SettingsAudio(
                input=AgentV1SettingsAudioInput(encoding="linear16", sample_rate=24000)),
            agent=AgentV1SettingsAgent(
                listen=AgentV1SettingsAgentListen(provider=AgentV1SettingsAgentListenProvider_V1(
                    type="deepgram", model="nova-3",
                    endpointing=300, utterance_end_ms=1200, vad_events=True)),
                think=ThinkSettingsV1(
                    provider=ThinkSettingsV1Provider_OpenAi(type="open_ai", model="gpt-4o-mini"),
                    prompt="You are a helpful assistant. Keep responses brief."),
                speak=SpeakSettingsV1(
                    provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en"))))
        agent.send_settings(settings)
        print("Agent configured (endpointing=300ms, utterance_end=1200ms, vad_events=on)")

        def on_message(message: Union[str, bytes]) -> None:
            if isinstance(message, bytes):
                return
            msg_type = getattr(message, "type", type(message).__name__)
            if msg_type == "UserStartedSpeaking":
                print(">> Barge-in: user interrupted — agent speech will stop")
            elif msg_type == "ConversationText":
                print(f"[{getattr(message, 'role', '?')}] {getattr(message, 'content', '')}")
            else:
                print(f"Event: {msg_type}")

        agent.on(EventType.OPEN, lambda _: print("Connection opened"))
        agent.on(EventType.MESSAGE, on_message)
        agent.on(EventType.CLOSE, lambda _: print("Connection closed"))
        agent.start_listening()

if __name__ == "__main__":
    main()
