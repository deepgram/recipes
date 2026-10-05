"""DTMF IVR Voice Agent — routes callers by dial-pad key press via function calling."""
import json, threading, time
from deepgram import DeepgramClient
from deepgram.agent.v1.types import (AgentV1FunctionCallRequest, AgentV1InjectUserMessage,
    AgentV1SendFunctionCallResponse, AgentV1Settings, AgentV1SettingsAgent,
    AgentV1SettingsAgentListen, AgentV1SettingsAgentListenProvider_V1,
    AgentV1SettingsAudio, AgentV1SettingsAudioInput)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi

DTMF_FN = {"name": "handle_dtmf", "description": "Caller pressed a phone key", "parameters":
    {"type": "object", "properties": {"digit": {"type": "string"}}, "required": ["digit"]}}
ROUTES, done, ready = {"1": "sales", "2": "support", "3": "billing"}, threading.Event(), threading.Event()

with DeepgramClient().agent.v1.connect() as agent:
    agent.send_settings(AgentV1Settings(
        audio=AgentV1SettingsAudio(input=AgentV1SettingsAudioInput(encoding="linear16", sample_rate=24000)),
        agent=AgentV1SettingsAgent(
            listen=AgentV1SettingsAgentListen(provider=AgentV1SettingsAgentListenProvider_V1(type="deepgram", model="nova-3")),
            think=ThinkSettingsV1(provider=ThinkSettingsV1Provider_OpenAi(type="open_ai", model="gpt-4o-mini"),
                prompt="You are an IVR. Press 1 for sales, 2 for support. Use handle_dtmf to route.", functions=[DTMF_FN]),
            speak=SpeakSettingsV1(provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en")))))
    def on_msg(m):
        if isinstance(m, bytes): return
        t = getattr(m, "type", "")
        if t == "SettingsApplied": ready.set()
        elif isinstance(m, AgentV1FunctionCallRequest):
            args = json.loads(m.input) if isinstance(m.input, str) else m.input
            dept = ROUTES.get(args.get("digit", ""), "unknown")
            print(f"DTMF '{args.get('digit')}' -> {dept}")
            agent.send_function_call_response(AgentV1SendFunctionCallResponse(
                type="FunctionCallResponse", id=m.id, name=m.name, content=json.dumps({"department": dept})))
        elif t == "ConversationText":
            role, txt = getattr(m, "role", ""), getattr(m, "content", "")
            if txt: print(f"[{role}] {txt}")
            if role == "assistant" and any(w in txt.lower() for w in ROUTES.values()): done.set()
    agent.on(EventType.OPEN, lambda _: print("Connected"))
    agent.on(EventType.MESSAGE, on_msg)
    threading.Thread(target=agent.start_listening, daemon=True).start()
    ready.wait(10)
    print("IVR ready — simulating DTMF '1'")
    agent.send_inject_user_message(AgentV1InjectUserMessage(content="Caller pressed 1"))
    done.wait(30)
    time.sleep(1)
