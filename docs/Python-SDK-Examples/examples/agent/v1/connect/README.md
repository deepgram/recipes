# Voice Agent WebSocket Connection (Agent API v1)

**Learning objective**: Establish a WebSocket connection to Deepgram's Voice Agent API for conversational AI experiences.

## Prerequisites

- **Python**: 3.10+
- **API key**: Set `DEEPGRAM_API_KEY` in your environment or `.env` file
- **OpenAI API key**: Required for the think provider
- **Install SDK**:
```bash
pip install deepgram-sdk
```

## Basic Usage

This example shows how to connect to the Agent API and configure it with listen, think, and speak capabilities.

```python
import threading
import time

from dotenv import load_dotenv
load_dotenv()

from deepgram import DeepgramClient
from deepgram.core.events import EventType
from deepgram.extensions.types.sockets import (
    AgentV1Agent,
    AgentV1AudioConfig,
    AgentV1AudioInput,
    AgentV1DeepgramSpeakProvider,
    AgentV1Listen,
    AgentV1ListenProvider,
    AgentV1OpenAiThinkProvider,
    AgentV1SettingsMessage,
    AgentV1SocketClientResponse,
    AgentV1SpeakProviderConfig,
    AgentV1Think,
)

client = DeepgramClient()

try:
    with client.agent.v1.connect() as agent:
        # Configure agent settings
        settings = AgentV1SettingsMessage(
            audio=AgentV1AudioConfig(
                input=AgentV1AudioInput(
                    encoding="linear16",
                    sample_rate=44100,
                )
            ),
            agent=AgentV1Agent(
                listen=AgentV1Listen(
                    provider=AgentV1ListenProvider(
                        type="deepgram",
                        model="nova-3",
                        smart_format=True,
                    )
                ),
                think=AgentV1Think(
                    provider=AgentV1OpenAiThinkProvider(
                        type="open_ai",
                        model="gpt-4o-mini",
                        temperature=0.7,
                    ),
                    prompt='Reply only and explicitly with "OK".',
                ),
                speak=AgentV1SpeakProviderConfig(
                    provider=AgentV1DeepgramSpeakProvider(
                        type="deepgram",
                        model="aura-2-asteria-en",
                    )
                ),
            ),
        )

        print("Send SettingsConfiguration message")
        agent.send_settings(settings)

        def on_message(message: AgentV1SocketClientResponse) -> None:
            if isinstance(message, bytes):
                print("Received audio event")
            else:
                msg_type = getattr(message, "type", "Unknown")
                print(f"Received {msg_type} event")
        
        agent.on(EventType.OPEN, lambda _: print("Connection opened"))
        agent.on(EventType.MESSAGE, on_message)
        agent.on(EventType.CLOSE, lambda _: print("Connection closed"))
        agent.on(EventType.ERROR, lambda error: print(f"Caught: {error}"))

        # Start listening - blocks until connection closes
        agent.start_listening()
except Exception as e:
    print(f"Caught: {e}")
```

## Key Concepts

- **Context Manager**: The `with` statement ensures proper connection cleanup
- **Settings Configuration**: Use structured types to configure the agent's behavior
- **Three Components**:
  - **Listen**: Speech-to-text transcription (Deepgram Nova models)
  - **Think**: LLM processing (OpenAI, Anthropic, or other providers)
  - **Speak**: Text-to-speech synthesis (Deepgram Aura models)
- **Event Handlers**: Register callbacks for connection lifecycle and messages
- **Audio Handling**: Receive both text events and audio bytes

## Agent Configuration

### Audio Input Configuration

Configure the audio input format:

```python
audio=AgentV1AudioConfig(
    input=AgentV1AudioInput(
        encoding="linear16",  # or "mulaw", "alaw"
        sample_rate=44100,    # Hz
    )
)
```

### Listen Provider Options

Configure the speech recognition:

```python
listen=AgentV1Listen(
    provider=AgentV1ListenProvider(
        type="deepgram",
        model="nova-3",           # or "nova-2"
        smart_format=True,        # Enable smart formatting
        language="en-US",         # Language code
        punctuate=True,           # Add punctuation
    )
)
```

### Think Provider Options

Configure the LLM provider:

```python
think=AgentV1Think(
    provider=AgentV1OpenAiThinkProvider(
        type="open_ai",
        model="gpt-4o-mini",      # or "gpt-4", "gpt-3.5-turbo"
        temperature=0.7,          # Response creativity
    ),
    prompt="Your system prompt here",  # Agent behavior instructions
)
```

### Speak Provider Options

Configure the voice output:

```python
speak=AgentV1SpeakProviderConfig(
    provider=AgentV1DeepgramSpeakProvider(
        type="deepgram",
        model="aura-2-asteria-en",  # Choose voice model
    )
)
```

## Sending Audio

Send audio data to the agent:

```python
audio_data = b"..."  # Your audio bytes
agent.send(audio_data)
```

## Receiving Responses

The agent sends various event types:
- **Text events**: Transcriptions, LLM responses, agent state changes
- **Audio events**: Synthesized speech as binary data

Handle them in your message callback:

```python
def on_message(message: AgentV1SocketClientResponse) -> None:
    if isinstance(message, bytes):
        # Play or save audio
        play_audio(message)
    else:
        # Handle text events
        print(f"Event: {message.type}")
```

## Next Steps

- See `async.py` for async/await pattern usage
- See `with_auth_token.py` for manual token authentication
- See `with_raw_response.py` for accessing raw WebSocket messages

