"""Voice Agent with state machine workflow driven by function calling."""

import threading, time
from enum import Enum
from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1FunctionCallRequest, AgentV1InjectUserMessage,
    AgentV1SendFunctionCallResponse, AgentV1Settings, AgentV1SettingsAgent,
    AgentV1SettingsAgentListen, AgentV1SettingsAgentListenProvider_V1,
    AgentV1SettingsAudio, AgentV1SettingsAudioInput, AgentV1UpdatePrompt,
)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi

class S(Enum):
    GREET = "greet"
    COLLECT = "collect_info"
    CONFIRM = "confirm"
    DONE = "done"

NEXT = {S.GREET: S.COLLECT, S.COLLECT: S.CONFIRM, S.CONFIRM: S.DONE}
PROMPT = {S.GREET: "Greet the user warmly. Call advance_state when greeted.",
    S.COLLECT: "Ask for name and preferred date. Call advance_state once collected.",
    S.CONFIRM: "Repeat details back. Call advance_state when user confirms.",
    S.DONE: "Tell the user their appointment is booked. Do not call any functions."}
FUNC = {"name": "advance_state", "description": "Move to the next workflow state",
    "parameters": {"type": "object", "properties": {"reason": {"type": "string"}}, "required": ["reason"]}}

def main():
    state, done = [S.GREET], threading.Event()
    client = DeepgramClient()
    with client.agent.v1.connect() as agent:
        def on_msg(m):
            if isinstance(m, AgentV1FunctionCallRequest) and m.name == "advance_state":
                nxt = NEXT.get(state[0])
                if nxt:
                    state[0] = nxt
                    agent.send_update_prompt(AgentV1UpdatePrompt(prompt=PROMPT[state[0]]))
                    print(f"State -> {state[0].value}")
                agent.send_function_call_response(AgentV1SendFunctionCallResponse(
                    type="FunctionCallResponse", id=m.id, name=m.name, content=f'{{"state":"{state[0].value}"}}'))
                if state[0] == S.DONE: done.set()
            elif not isinstance(m, bytes) and getattr(m, "type", "") == "ConversationText":
                print(f"[{getattr(m, 'role', '?')}] {getattr(m, 'content', '')}")
        settings = AgentV1Settings(audio=AgentV1SettingsAudio(input=AgentV1SettingsAudioInput(encoding="linear16", sample_rate=24000)),
            agent=AgentV1SettingsAgent(listen=AgentV1SettingsAgentListen(provider=AgentV1SettingsAgentListenProvider_V1(type="deepgram", model="nova-3")),
                think=ThinkSettingsV1(provider=ThinkSettingsV1Provider_OpenAi(type="open_ai", model="gpt-4o-mini"), prompt=PROMPT[S.GREET], functions=[FUNC]),
                speak=SpeakSettingsV1(provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en"))))
        agent.on(EventType.OPEN, lambda _: print("Connection opened"))
        agent.on(EventType.MESSAGE, on_msg)
        t = threading.Thread(target=agent.start_listening, daemon=True)
        t.start()
        agent.send_settings(settings)
        print(f"State -> {state[0].value}")
        time.sleep(3)
        agent.send_inject_user_message(AgentV1InjectUserMessage(content="Hi, book an appointment. Name: Jane Doe, date: October 5th."))
        done.wait(timeout=30)
        time.sleep(2)
        print(f"Final state: {state[0].value}")

if __name__ == "__main__":
    main()
