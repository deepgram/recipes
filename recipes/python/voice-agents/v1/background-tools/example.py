"""
Recipe: Background Tool Execution with Filler Speech (Voice Agents v1)
Sends filler speech while tools run in a background thread, eliminating silence.
"""

import json, threading, time
from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1FunctionCallRequest, AgentV1InjectAgentMessage,
    AgentV1SendFunctionCallResponse, AgentV1Settings, AgentV1SettingsAgent,
    AgentV1SettingsAgentListen, AgentV1SettingsAgentListenProvider_V1,
    AgentV1SettingsAudio, AgentV1SettingsAudioInput,
)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi

TOOLS = [
    {"name": "get_weather", "description": "Get current weather",
     "parameters": {"type": "object", "properties": {"location": {"type": "string"}}, "required": ["location"]}},
    {"name": "search_db", "description": "Search customer database (slow)",
     "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}},
]
FILLER = {"get_weather": "Let me check the weather...", "search_db": "One moment while I look that up..."}

def run_tool(name, args):
    if name == "get_weather":
        time.sleep(0.3)
        return json.dumps({"temp": "72°F", "condition": "sunny", "city": args.get("location", "")})
    time.sleep(1.5)
    return json.dumps({"results": [{"name": "Jane Doe", "id": "C-1042"}], "query": args.get("query", "")})

def main():
    client = DeepgramClient()
    with client.agent.v1.connect() as agent:
        agent.send_settings(AgentV1Settings(
            audio=AgentV1SettingsAudio(input=AgentV1SettingsAudioInput(encoding="linear16", sample_rate=24000)),
            agent=AgentV1SettingsAgent(
                listen=AgentV1SettingsAgentListen(provider=AgentV1SettingsAgentListenProvider_V1(type="deepgram", model="nova-3")),
                think=ThinkSettingsV1(provider=ThinkSettingsV1Provider_OpenAi(type="open_ai", model="gpt-4o-mini"),
                    prompt="You are a helpful assistant. Use get_weather for weather and search_db for customer lookups.",
                    functions=TOOLS),
                speak=SpeakSettingsV1(provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en")))))
        print("Agent configured with background tool execution")

        def handle_function_call(fc):
            for fn in fc.functions:
                print(f"Tool called: {fn.name} — sending filler speech")
                agent.send_inject_agent_message(AgentV1InjectAgentMessage(type="InjectAgentMessage", message=FILLER.get(fn.name, "Working on it...")))
                args = json.loads(fn.arguments) if fn.arguments else {}
                def _bg(f=fn, a=args):
                    result = run_tool(f.name, a)
                    print(f"Tool {f.name} done — sending result")
                    agent.send_function_call_response(AgentV1SendFunctionCallResponse(type="FunctionCallResponse", id=f.id, name=f.name, content=result))
                threading.Thread(target=_bg, daemon=True).start()

        def on_message(m):
            if isinstance(m, AgentV1FunctionCallRequest): handle_function_call(m)
            elif isinstance(m, bytes): print(f"Audio: {len(m)} bytes")
            else: print(f"Event: {getattr(m, 'type', type(m).__name__)}")

        agent.on(EventType.OPEN, lambda _: print("Connection opened"))
        agent.on(EventType.MESSAGE, on_message)
        agent.on(EventType.CLOSE, lambda _: print("Connection closed"))
        agent.start_listening()

if __name__ == "__main__":
    main()
