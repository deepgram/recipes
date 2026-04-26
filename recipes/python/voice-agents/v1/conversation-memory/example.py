"""
Recipe: Conversation Memory (Voice Agents v1)
===============================================
Demonstrates maintaining conversation context across turns using
initial context messages and dynamic prompt updates so the agent
remembers what was said earlier in the session.
"""

from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1ConversationText, AgentV1Settings, AgentV1SettingsAgent,
    AgentV1SettingsAgentContext, AgentV1SettingsAgentContextMessagesItemContent,
    AgentV1SettingsAgentListen, AgentV1SettingsAgentListenProvider_V1,
    AgentV1SettingsAudio, AgentV1SettingsAudioInput, AgentV1UpdatePrompt,
)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi

BASE_PROMPT = "You are a helpful assistant. Remember everything the user tells you."
memory: list[dict] = []


def build_context_prompt() -> str:
    recent = memory[-10:]
    history = "\n".join(f'{m["role"]}: {m["content"]}' for m in recent)
    return f"{BASE_PROMPT}\n\nConversation so far:\n{history}" if recent else BASE_PROMPT


def main():
    client = DeepgramClient()

    with client.agent.v1.connect() as agent:
        prior_context = [
            AgentV1SettingsAgentContextMessagesItemContent(
                type="History", role="user", content="My name is Alice and I like jazz."
            ),
            AgentV1SettingsAgentContextMessagesItemContent(
                type="History", role="assistant", content="Nice to meet you, Alice! Jazz is great."
            ),
        ]

        settings = AgentV1Settings(
            audio=AgentV1SettingsAudio(
                input=AgentV1SettingsAudioInput(encoding="linear16", sample_rate=24000)
            ),
            agent=AgentV1SettingsAgent(
                listen=AgentV1SettingsAgentListen(
                    provider=AgentV1SettingsAgentListenProvider_V1(type="deepgram", model="nova-3")
                ),
                think=ThinkSettingsV1(
                    provider=ThinkSettingsV1Provider_OpenAi(type="open_ai", model="gpt-4o-mini"),
                    prompt=BASE_PROMPT,
                ),
                speak=SpeakSettingsV1(
                    provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en")
                ),
                context=AgentV1SettingsAgentContext(messages=prior_context),
            ),
        )

        agent.send_settings(settings)
        print("Agent configured with conversation memory")
        print(f"Loaded {len(prior_context)} prior context messages")

        def on_message(message) -> None:
            if isinstance(message, AgentV1ConversationText):
                memory.append({"role": message.role, "content": message.content})
                print(f"[{message.role}] {message.content}")
                if len(memory) % 2 == 0:
                    agent.send_update_prompt(AgentV1UpdatePrompt(prompt=build_context_prompt()))
                    print(f"Prompt updated with {len(memory)} turns in memory")
            elif isinstance(message, bytes):
                print(f"Received {len(message)} bytes of audio")
            else:
                print(f"Event: {getattr(message, 'type', type(message).__name__)}")

        agent.on(EventType.OPEN, lambda _: print("Connection opened"))
        agent.on(EventType.MESSAGE, on_message)
        agent.on(EventType.CLOSE, lambda _: print("Connection closed"))
        agent.start_listening()


if __name__ == "__main__":
    main()
