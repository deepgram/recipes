"""Voice agent with an IVR system prompt that classifies caller intent
(billing, support, sales) and responds with department-specific guidance."""

from deepgram import DeepgramClient
from deepgram.agent.v1.types import (
    AgentV1Settings, AgentV1SettingsAgent,
    AgentV1SettingsAgentListen, AgentV1SettingsAgentListenProvider_V1,
    AgentV1SettingsAudio, AgentV1SettingsAudioInput,
)
from deepgram.core.events import EventType
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi

IVR_PROMPT = (
    "You are an IVR agent for Acme Corp. Greet the caller, classify their intent "
    "as billing, support, or sales. Billing: invoices and payments. Support: "
    "troubleshoot issues. Sales: pricing and plans. Confirm the department first."
)

def main():
    client = DeepgramClient()
    with client.agent.v1.connect() as agent:
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
                    prompt=IVR_PROMPT,
                ),
                speak=SpeakSettingsV1(
                    provider=SpeakSettingsV1Provider_Deepgram(type="deepgram", model="aura-2-thalia-en")
                ),
            ),
        )
        agent.send_settings(settings)
        print("Voice agent configured with intent-routing IVR prompt")
        agent.on(EventType.OPEN, lambda _: print("Connection opened"))
        agent.on(EventType.CLOSE, lambda _: print("Connection closed"))
        agent.start_listening()

if __name__ == "__main__":
    main()
