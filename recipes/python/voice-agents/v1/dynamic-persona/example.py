"""
Recipe: Dynamic Persona Switching (Voice Agents v1)
=====================================================
Hot-swaps agent persona (prompt + TTS voice) mid-session using
send_update_prompt() and send_update_speak().
"""
import threading, time
from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1InjectUserMessage, AgentV1Settings, AgentV1SettingsAgent,
    AgentV1SettingsAgentListen, AgentV1SettingsAgentListenProvider_V1,
    AgentV1SettingsAudio, AgentV1SettingsAudioInput,
    AgentV1UpdatePrompt, AgentV1UpdateSpeak,
)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi

PERSONAS = {
    "sales":   {"prompt": "You are a friendly sales agent. Highlight benefits.", "voice": "aura-2-thalia-en"},
    "support": {"prompt": "You are precise technical support. Give step-by-step help.", "voice": "aura-2-arcas-en"},
    "billing": {"prompt": "You are a billing specialist. Be clear about charges.", "voice": "aura-2-luna-en"},
}

def switch_persona(agent, name):
    p = PERSONAS[name]
    agent.send_update_prompt(AgentV1UpdatePrompt(prompt=p["prompt"]))
    agent.send_update_speak(AgentV1UpdateSpeak(speak=SpeakSettingsV1(
        provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model=p["voice"]))))
    print(f"Switched to persona: {name} (voice={p['voice']})")

def main():
    client = DeepgramClient()
    ready, done = threading.Event(), threading.Event()
    with client.agent.v1.connect() as agent:
        settings = AgentV1Settings(
            audio=AgentV1SettingsAudio(input=AgentV1SettingsAudioInput(encoding="linear16", sample_rate=24000)),
            agent=AgentV1SettingsAgent(
                listen=AgentV1SettingsAgentListen(provider=AgentV1SettingsAgentListenProvider_V1(type="deepgram", model="nova-3")),
                think=ThinkSettingsV1(provider=ThinkSettingsV1Provider_OpenAi(type="open_ai", model="gpt-4o-mini"), prompt=PERSONAS["sales"]["prompt"]),
                speak=SpeakSettingsV1(provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model=PERSONAS["sales"]["voice"])),
            ))
        def on_msg(msg):
            t = getattr(msg, "type", None)
            if t == "SettingsApplied": ready.set()
            elif t == "ConversationText" and getattr(msg, "role", "") == "assistant":
                print(f"[agent] {getattr(msg, 'content', '')[:80]}")
                done.set()
            elif t in ("PromptUpdated", "SpeakUpdated"): print(f"Confirmed: {t}")
        agent.on(EventType.MESSAGE, on_msg)
        threading.Thread(target=agent.start_listening, daemon=True).start()
        agent.send_settings(settings)
        ready.wait(10)
        print("Agent started with persona: sales")
        switch_persona(agent, "support")
        time.sleep(1)
        agent.send_inject_user_message(AgentV1InjectUserMessage(content="My app keeps crashing on startup."))
        done.wait(30)
        time.sleep(2)

if __name__ == "__main__":
    main()
