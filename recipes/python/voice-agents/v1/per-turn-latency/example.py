"""
Recipe: Per-Turn Latency (Voice Agents v1)
===========================================
Prints the server-side latency breakdown for each agent turn: STT, LLM
(time-to-first-token), TTS, and total end-to-end latency. Deepgram sends
a LatencyReport event after every agent response, so no client-side
instrumentation is needed.
"""

import threading
import time

from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1InjectUserMessage, AgentV1LatencyReport,
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
    client = DeepgramClient()
    latency_event = threading.Event()

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
                    prompt="You are a helpful assistant. Keep responses brief.",
                ),
                speak=SpeakSettingsV1(
                    provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en")
                ),
            ),
        )

        settings_ready = threading.Event()

        def on_message(message) -> None:
            if isinstance(message, bytes):
                return
            msg_type = getattr(message, "type", "")
            if msg_type == "SettingsApplied":
                settings_ready.set()
            elif isinstance(message, AgentV1LatencyReport):
                print(f"STT  latency: {message.stt_latency or 0:.3f}s")
                print(f"LLM  latency: {message.ttt_text_latency or 0:.3f}s")
                print(f"TTS  latency: {message.tts_latency or 0:.3f}s")
                print(f"Total latency: {message.total_latency or 0:.3f}s")
                latency_event.set()

        agent.on(EventType.MESSAGE, on_message)
        listener = threading.Thread(target=agent.start_listening, daemon=True)
        listener.start()
        agent.send_settings(settings)

        if not settings_ready.wait(10):
            raise TimeoutError("Settings not applied")
        agent.send_inject_user_message(
            AgentV1InjectUserMessage(content="Say hello in one sentence.")
        )
        if not latency_event.wait(30):
            raise TimeoutError("No latency report received")
        time.sleep(1)


if __name__ == "__main__":
    main()
