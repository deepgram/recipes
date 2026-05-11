"""Latency Profiling — measure per-component TTFB in a voice agent turn."""
import threading, time
from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1InjectUserMessage, AgentV1Settings, AgentV1SettingsAgent,
    AgentV1SettingsAgentListen, AgentV1SettingsAgentListenProvider_V1,
    AgentV1SettingsAudio, AgentV1SettingsAudioInput)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi

client = DeepgramClient()
ts, done = {}, threading.Event()
with client.agent.v1.connect() as agent:
    settings = AgentV1Settings(
        audio=AgentV1SettingsAudio(
            input=AgentV1SettingsAudioInput(encoding="linear16", sample_rate=24000)),
        agent=AgentV1SettingsAgent(
            listen=AgentV1SettingsAgentListen(provider=AgentV1SettingsAgentListenProvider_V1(
                type="deepgram", model="nova-3")),
            think=ThinkSettingsV1(provider=ThinkSettingsV1Provider_OpenAi(
                type="open_ai", model="gpt-4o-mini"), prompt="Reply in one short sentence."),
            speak=SpeakSettingsV1(provider=SpeakSettingsV1Provider_Deepgram(
                type="deepgram", model="aura-2-thalia-en"))))
    def on_message(msg):
        now = time.perf_counter()
        if isinstance(msg, bytes):
            ts.setdefault("tts_fb", now); return
        t = getattr(msg, "type", "")
        if t == "SettingsApplied":
            ts["inject"] = now
            agent.send_inject_user_message(AgentV1InjectUserMessage(
                content="What is the deepest ocean trench?"))
        elif t == "AgentThinking":
            ts["think"] = now
        elif t == "AgentStartedSpeaking":
            ts["speak"] = now
        elif t == "AgentAudioDone":
            i, th, sp = ts.get("inject", now), ts.get("think", now), ts.get("speak", now)
            print(f"Think TTFB:     {(th - i)*1000:7.0f} ms")
            print(f"TTS TTFB:       {(ts.get('tts_fb', now) - th)*1000:7.0f} ms")
            print(f"Speak duration: {(now - sp)*1000:7.0f} ms")
            print(f"Total turn:     {(now - i)*1000:7.0f} ms")
            done.set()
    agent.on(EventType.MESSAGE, on_message)
    threading.Thread(target=agent.start_listening, daemon=True).start()
    agent.send_settings(settings)
    done.wait(timeout=30)
