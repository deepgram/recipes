"""
Recipe: Backchanneling — Inject Acknowledgments (Voice Agents v1)
=================================================================
Inject brief agent acknowledgments ("mm-hmm", "I see") during a
conversation without interrupting the user. Uses behavior="queue"
so the backchannel plays after the current turn finishes.
"""

import random
import threading
import time

from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1InjectAgentMessage, AgentV1InjectUserMessage,
    AgentV1Settings, AgentV1SettingsAgent,
    AgentV1SettingsAgentListen, AgentV1SettingsAgentListenProvider_V1,
    AgentV1SettingsAudio, AgentV1SettingsAudioInput,
)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi

BACKCHANNELS = ["mm-hmm", "I see", "right", "got it", "sure"]

def main():
    client = DeepgramClient()
    with client.agent.v1.connect() as agent:
        ready = threading.Event()
        settings = AgentV1Settings(
            audio=AgentV1SettingsAudio(
                input=AgentV1SettingsAudioInput(encoding="linear16", sample_rate=24000)),
            agent=AgentV1SettingsAgent(
                listen=AgentV1SettingsAgentListen(
                    provider=AgentV1SettingsAgentListenProvider_V1(type="deepgram", model="nova-3")),
                think=ThinkSettingsV1(
                    provider=ThinkSettingsV1Provider_OpenAi(type="open_ai", model="gpt-4o-mini"),
                    prompt="You are a helpful assistant. Keep responses brief."),
                speak=SpeakSettingsV1(
                    provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en"))))

        def on_message(message) -> None:
            if isinstance(message, bytes):
                print(f"Received {len(message)} bytes of agent audio")
            elif getattr(message, "type", "") == "SettingsApplied":
                ready.set()
            elif getattr(message, "type", "") == "ConversationText":
                print(f"[{getattr(message, 'role', '?')}] {getattr(message, 'content', '')}")
            else:
                print(f"Event: {getattr(message, 'type', type(message).__name__)}")

        agent.on(EventType.OPEN, lambda _: print("Connection opened"))
        agent.on(EventType.MESSAGE, on_message)
        agent.on(EventType.CLOSE, lambda _: print("Connection closed"))
        listener = threading.Thread(target=agent.start_listening, daemon=True)
        listener.start()
        agent.send_settings(settings)
        ready.wait(10)
        print("Agent configured — injecting backchannels between user messages")
        for line in ["I've been working on a project involving speech recognition.",
                     "The goal is to make voice interfaces feel more human."]:
            ack = random.choice(BACKCHANNELS)
            print(f"Backchannel queued: \"{ack}\"")
            agent.send_inject_agent_message(
                AgentV1InjectAgentMessage(message=ack, behavior="queue"))
            time.sleep(1)
            agent.send_inject_user_message(AgentV1InjectUserMessage(content=line))
            time.sleep(3)
        time.sleep(2)

if __name__ == "__main__":
    main()
