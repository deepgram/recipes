"""Wake Word Activation — detect a phrase via STT, then start a voice agent."""
import threading, time
from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1InjectUserMessage, AgentV1Settings, AgentV1SettingsAgent,
    AgentV1SettingsAgentListen, AgentV1SettingsAgentListenProvider_V1,
    AgentV1SettingsAudio, AgentV1SettingsAudioInput,
)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi

AUDIO_URL = "https://dpgr.am/spacewalk.wav"
WAKE_PHRASE = "spacewalk"

client = DeepgramClient()
print("STATE: IDLE — listening for wake phrase…")
resp = client.listen.v1.media.transcribe_url(url=AUDIO_URL, model="nova-3", smart_format=True)
transcript = resp.results.channels[0].alternatives[0].transcript.lower()
if WAKE_PHRASE not in transcript:
    print(f"Wake phrase '{WAKE_PHRASE}' not detected. Staying idle.")
    raise SystemExit(0)
print(f"STATE: WAKE_WORD_DETECTED — '{WAKE_PHRASE}' found in audio")
print("STATE: AGENT_ACTIVE — opening voice agent session")
ready, done = threading.Event(), threading.Event()
with client.agent.v1.connect() as agent:
    settings = AgentV1Settings(
        audio=AgentV1SettingsAudio(input=AgentV1SettingsAudioInput(encoding="linear16", sample_rate=24000)),
        agent=AgentV1SettingsAgent(
            listen=AgentV1SettingsAgentListen(provider=AgentV1SettingsAgentListenProvider_V1(type="deepgram", model="nova-3")),
            think=ThinkSettingsV1(provider=ThinkSettingsV1Provider_OpenAi(type="open_ai", model="gpt-4o-mini"), prompt="You are a helpful assistant. Be brief."),
            speak=SpeakSettingsV1(provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en")),
        ),
    )
    def on_msg(msg):
        if not isinstance(msg, bytes) and getattr(msg, "type", "") == "SettingsApplied":
            ready.set()
        elif not isinstance(msg, bytes) and getattr(msg, "type", "") == "ConversationText" and getattr(msg, "role", "") == "assistant":
            print(f"Agent: {getattr(msg, 'content', '')}")
            done.set()
    agent.on(EventType.MESSAGE, on_msg)
    threading.Thread(target=agent.start_listening, daemon=True).start()
    agent.send_settings(settings)
    ready.wait(10)
    agent.send_inject_user_message(AgentV1InjectUserMessage(content="Tell me about the first all-female spacewalk."))
    done.wait(30)
    time.sleep(1)
print("STATE: IDLE — agent session ended")
