import json, threading, time
from pathlib import Path
from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1InjectAgentMessage, AgentV1InjectUserMessage, AgentV1Settings,
    AgentV1SettingsAgent, AgentV1SettingsAgentListen,
    AgentV1SettingsAgentListenProvider_V1, AgentV1SettingsAudio,
    AgentV1SettingsAudioInput,
)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi

THREAD = Path("thread_history.json")
SEED = [{"role": "user", "content": "What was the first all-female spacewalk?"},
        {"role": "assistant", "content": "Christina Koch and Jessica Meir performed it on Oct 18 2019."}]

history = json.loads(THREAD.read_text()) if THREAD.exists() else SEED
THREAD.write_text(json.dumps(history, indent=2))
print(f"Loaded {len(history)} prior turns from thread")

client = DeepgramClient()
with client.agent.v1.connect() as agent:
    ready, done = threading.Event(), threading.Event()
    def on_msg(m):
        if isinstance(m, bytes): return
        t = getattr(m, "type", "")
        if t == "SettingsApplied": ready.set()
        elif t == "ConversationText" and getattr(m, "role", "") == "assistant":
            print(f"Agent: {getattr(m, 'content', '')}"); done.set()
    agent.on(EventType.MESSAGE, on_msg)
    threading.Thread(target=agent.start_listening, daemon=True).start()
    agent.send_settings(AgentV1Settings(
        audio=AgentV1SettingsAudio(input=AgentV1SettingsAudioInput(encoding="linear16", sample_rate=24000)),
        agent=AgentV1SettingsAgent(
            listen=AgentV1SettingsAgentListen(provider=AgentV1SettingsAgentListenProvider_V1(type="deepgram", model="nova-3")),
            think=ThinkSettingsV1(provider=ThinkSettingsV1Provider_OpenAi(type="open_ai", model="gpt-4o-mini"),
                prompt="You are a helpful assistant. Continue the conversation using the injected context."),
            speak=SpeakSettingsV1(provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en")))))
    ready.wait(10)
    for turn in history:
        if turn["role"] == "user":
            agent.send_inject_user_message(AgentV1InjectUserMessage(content=turn["content"]))
        else:
            agent.send_inject_agent_message(AgentV1InjectAgentMessage(message=turn["content"]))
    print("Prior context injected — asking follow-up")
    agent.send_inject_user_message(AgentV1InjectUserMessage(content="How long did that spacewalk last?"))
    done.wait(30); time.sleep(2)
