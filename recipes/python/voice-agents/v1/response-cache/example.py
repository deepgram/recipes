"""Voice Agent with in-memory TTL response cache — cache repeated questions to skip LLM round-trips."""
import hashlib, threading, time
from deepgram import DeepgramClient
from deepgram.agent.v1.types import (AgentV1InjectUserMessage, AgentV1Settings,
    AgentV1SettingsAgent, AgentV1SettingsAgentListen,
    AgentV1SettingsAgentListenProvider_V1, AgentV1SettingsAudio, AgentV1SettingsAudioInput)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi

CACHE, TTL, stats = {}, 300, {"hits": 0, "misses": 0}
Q = "What does the first all-female spacewalk symbolize?"
def _key(t): return hashlib.sha256(" ".join(t.lower().split()).encode()).hexdigest()
def _get(k):
    e = CACHE.get(k)
    return e["r"] if e and time.time() - e["t"] < TTL else None
def main():
    client, done = DeepgramClient(), threading.Event()
    with client.agent.v1.connect() as agent:
        s = AgentV1Settings(audio=AgentV1SettingsAudio(input=AgentV1SettingsAudioInput(
            encoding="linear16", sample_rate=24000)), agent=AgentV1SettingsAgent(
            listen=AgentV1SettingsAgentListen(provider=AgentV1SettingsAgentListenProvider_V1(type="deepgram", model="nova-3")),
            think=ThinkSettingsV1(provider=ThinkSettingsV1Provider_OpenAi(type="open_ai", model="gpt-4o-mini"),
                prompt="You are a helpful assistant. Keep answers brief."),
            speak=SpeakSettingsV1(provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en"))))
        def on_msg(msg):
            if isinstance(msg, bytes): return
            mt = getattr(msg, "type", "")
            if mt == "SettingsApplied":
                cached = _get(_key(Q))
                if cached:
                    stats["hits"] += 1
                    print(f"[HIT] {cached[:80]}  (hits={stats['hits']})")
                    done.set()
                else:
                    agent.send_inject_user_message(AgentV1InjectUserMessage(content=Q))
            elif mt == "ConversationText" and getattr(msg, "role", "") == "assistant":
                r = getattr(msg, "content", "")
                CACHE[_key(Q)] = {"r": r, "t": time.time()}
                stats["misses"] += 1
                print(f"[MISS] {r[:80]}  (misses={stats['misses']})")
                done.set()
        agent.on(EventType.OPEN, lambda _: print("Connection opened"))
        agent.on(EventType.MESSAGE, on_msg)
        t = threading.Thread(target=agent.start_listening, daemon=True)
        t.start(); agent.send_settings(s); done.wait(30)
        print(f"Cache: {len(CACHE)} entries, hits={stats['hits']}, misses={stats['misses']}, ttl={TTL}s")
if __name__ == "__main__": main()
