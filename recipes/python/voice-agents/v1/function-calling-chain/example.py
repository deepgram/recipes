"""
Recipe: Multi-Turn Function Calling Chain (Voice Agents v1)
============================================================
Demonstrates chaining sequential, dependent function calls across
conversation turns. Each function result feeds into the next call:
lookup_customer → get_orders → check_return_eligibility → initiate_return.
"""

import json
import threading

from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1FunctionCallRequest, AgentV1InjectUserMessage,
    AgentV1SendFunctionCallResponse, AgentV1Settings, AgentV1SettingsAgent,
    AgentV1SettingsAgentListen, AgentV1SettingsAgentListenProvider_V1,
    AgentV1SettingsAudio, AgentV1SettingsAudioInput,
)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi

FUNCTIONS = [
    {"name": "lookup_customer", "description": "Find a customer by name",
     "parameters": {"type": "object", "properties": {"name": {"type": "string"}}, "required": ["name"]}},
    {"name": "get_orders", "description": "Get order history for a customer ID",
     "parameters": {"type": "object", "properties": {"customer_id": {"type": "string"}}, "required": ["customer_id"]}},
    {"name": "check_return_eligibility", "description": "Check if an order can be returned",
     "parameters": {"type": "object", "properties": {"order_id": {"type": "string"}}, "required": ["order_id"]}},
    {"name": "initiate_return", "description": "Start a return for an order",
     "parameters": {"type": "object", "properties": {"order_id": {"type": "string"}, "reason": {"type": "string"}}, "required": ["order_id", "reason"]}},
]

MOCK_RESPONSES = {
    "lookup_customer": '{"customer_id": "C-1234", "name": "Jane Smith", "email": "jane@example.com"}',
    "get_orders": '{"orders": [{"order_id": "ORD-5678", "item": "Wireless Headphones", "date": "2026-10-15", "total": "$89.99"}]}',
    "check_return_eligibility": '{"eligible": true, "return_window_days": 30, "days_remaining": 16}',
    "initiate_return": '{"return_id": "RET-9012", "status": "approved", "label_url": "https://example.com/label/RET-9012"}',
}

call_count = 0


def main():
    global call_count
    client = DeepgramClient()
    done = threading.Event()

    with client.agent.v1.connect() as agent:
        settings = AgentV1Settings(
            audio=AgentV1SettingsAudio(input=AgentV1SettingsAudioInput(encoding="linear16", sample_rate=24000)),
            agent=AgentV1SettingsAgent(
                listen=AgentV1SettingsAgentListen(
                    provider=AgentV1SettingsAgentListenProvider_V1(type="deepgram", model="nova-3")),
                think=ThinkSettingsV1(
                    provider=ThinkSettingsV1Provider_OpenAi(type="open_ai", model="gpt-4o-mini"),
                    prompt=("You are a customer service agent. When a user wants to return a product, "
                            "call these functions in order: lookup_customer, get_orders, "
                            "check_return_eligibility, then initiate_return. "
                            "Pass results from each step to the next."),
                    functions=FUNCTIONS,
                ),
                speak=SpeakSettingsV1(provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en")),
            ),
        )

        def on_message(message) -> None:
            global call_count
            if isinstance(message, AgentV1FunctionCallRequest):
                for fn in message.functions:
                    call_count += 1
                    print(f"Step {call_count}: {fn.name}({fn.arguments})")
                    content = MOCK_RESPONSES.get(fn.name, '{"error": "unknown function"}')
                    print(f"  → {content}")
                    agent.send_function_call_response(AgentV1SendFunctionCallResponse(
                        type="FunctionCallResponse", id=fn.id, name=fn.name, content=content))
                    if call_count >= 4:
                        done.set()
            elif isinstance(message, bytes):
                pass
            else:
                msg_type = getattr(message, "type", type(message).__name__)
                if msg_type == "SettingsApplied":
                    print("Agent ready — sending return request")
                    agent.send_inject_user_message(AgentV1InjectUserMessage(
                        content="I'm Jane Smith and I want to return the headphones I bought recently."))
                elif msg_type == "ConversationText":
                    role = getattr(message, "role", "")
                    print(f"[{role}] {getattr(message, 'content', '')}")

        agent.on(EventType.OPEN, lambda _: print("Connection opened"))
        agent.on(EventType.MESSAGE, on_message)
        agent.on(EventType.CLOSE, lambda _: print("Connection closed"))

        listener = threading.Thread(target=agent.start_listening, daemon=True)
        listener.start()
        agent.send_settings(settings)
        done.wait(timeout=30)
        print(f"\nChain complete: {call_count} function calls executed")


if __name__ == "__main__":
    main()
