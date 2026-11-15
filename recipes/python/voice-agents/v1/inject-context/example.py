"""Inject live context (e.g. screen description) into a voice agent's prompt mid-conversation."""

import threading, time
from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1InjectUserMessage, AgentV1Settings, AgentV1SettingsAgent,
    AgentV1SettingsAgentListen, AgentV1SettingsAgentListenProvider_V1,
    AgentV1SettingsAudio, AgentV1SettingsAudioInput, AgentV1UpdatePrompt,
)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi

SCREEN_CONTEXT = "The user's screen shows an error dialog: 'Connection timed out on port 443'."
BASE_PROMPT = "You are a helpful support assistant. Keep responses brief."
client = DeepgramClient()
ready, done = threading.Event(), threading.Event()

with client.agent.v1.connect() as agent:
    def on_message(msg):
        if isinstance(msg, bytes):
            return
        t = getattr(msg, "type", "")
        if t == "SettingsApplied":
            ready.set()
        elif t == "ConversationText":
            print(f"[{getattr(msg, 'role', '')}] {getattr(msg, 'content', '')}")
            if getattr(msg, "role", "") == "assistant":
                done.set()

    agent.on(EventType.MESSAGE, on_message)
    threading.Thread(target=agent.start_listening, daemon=True).start()
    agent.send_settings(AgentV1Settings(
        audio=AgentV1SettingsAudio(input=AgentV1SettingsAudioInput(encoding="linear16", sample_rate=24000)),
        agent=AgentV1SettingsAgent(
            listen=AgentV1SettingsAgentListen(provider=AgentV1SettingsAgentListenProvider_V1(type="deepgram", model="nova-3")),
            think=ThinkSettingsV1(provider=ThinkSettingsV1Provider_OpenAi(type="open_ai", model="gpt-4o-mini"), prompt=BASE_PROMPT),
            speak=SpeakSettingsV1(provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en")),
        ),
    ))
    ready.wait(10)
    print(f"Injecting screen context: {SCREEN_CONTEXT}")
    agent.send_update_prompt(AgentV1UpdatePrompt(prompt=f"{BASE_PROMPT}\n\nCurrent screen context: {SCREEN_CONTEXT}"))
    agent.send_inject_user_message(AgentV1InjectUserMessage(content="What's on my screen right now?"))
    done.wait(30)
    time.sleep(1)
