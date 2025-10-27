# Streaming Text-to-Speech via WebSocket (Speak API v1)

**Learning objective**: Establish a WebSocket connection to stream text-to-speech synthesis in real-time using the Python SDK.

## Prerequisites

- **Python**: 3.10+
- **API key**: Set `DEEPGRAM_API_KEY` in your environment or `.env` file
- **Install SDK**:
```bash
pip install deepgram-sdk
```

## Basic Usage

This example shows how to connect to Deepgram's Speak API via WebSocket for streaming text-to-speech synthesis.

```python
import threading
import time

from dotenv import load_dotenv
load_dotenv()

from deepgram import DeepgramClient
from deepgram.core.events import EventType
from deepgram.extensions.types.sockets import SpeakV1SocketClientResponse, SpeakV1ControlMessage

client = DeepgramClient()

try:
    with client.speak.v1.connect(
        model="aura-2-asteria-en",
        encoding="linear16",
        sample_rate=24000
    ) as connection:
        def on_message(message: SpeakV1SocketClientResponse) -> None:
            if isinstance(message, bytes):
                print("Received audio event")
                # Handle audio bytes - play or save
            else:
                msg_type = getattr(message, "type", "Unknown")
                print(f"Received {msg_type} event")

        connection.on(EventType.OPEN, lambda _: print("Connection opened"))
        connection.on(EventType.MESSAGE, on_message)
        connection.on(EventType.CLOSE, lambda _: print("Connection closed"))
        connection.on(EventType.ERROR, lambda error: print(f"Caught: {error}"))

        # Start listening - blocks until connection closes
        threading.Thread(target=connection.start_listening, daemon=True).start()

        # Send text to be converted to speech
        connection.send_text("Hello, this is streaming text to speech!")

        # Send control messages
        print("Send Flush message")
        connection.send_control(SpeakV1ControlMessage(type="Flush"))
        print("Send Close message")
        connection.send_control(SpeakV1ControlMessage(type="Close"))

        time.sleep(3)  # Wait for audio processing
except Exception as e:
    print(f"Caught: {e}")
```

## Key Concepts

- **Context Manager**: The `with` statement ensures proper connection cleanup
- **Audio Configuration**: Specify `model`, `encoding`, and `sample_rate` when connecting
- **Event Handlers**: Register callbacks for connection lifecycle and audio events
- **Binary Audio**: Receive synthesized audio as binary data in the message callback
- **Control Messages**: Send `Flush` and `Close` control messages to manage synthesis

## Audio Configuration

Configure the audio output format:

```python
with client.speak.v1.connect(
    model="aura-2-asteria-en",    # Voice model
    encoding="linear16",           # Audio encoding
    sample_rate=24000,             # Sample rate in Hz
    container="none",              # Audio container format
) as connection:
    # ... setup handlers
```

### Voice Models

Choose from various Aura voice models:
- `aura-2-asteria-en`: Female, conversational
- `aura-2-luna-en`: Female, warm
- `aura-2-stella-en`: Female, expressive
- `aura-2-athena-en`: Female, professional
- `aura-2-hera-en`: Female, clear
- `aura-2-orion-en`: Male, conversational
- `aura-2-arcas-en`: Male, deep
- `aura-2-perseus-en`: Male, professional
- `aura-2-angus-en`: Male, narrative
- `aura-2-orpheus-en`: Male, smooth
- `aura-2-helios-en`: Male, energetic
- `aura-2-zeus-en`: Male, authoritative

### Encoding Options

- `linear16`: 16-bit PCM (uncompressed)
- `opus`: Opus codec (compressed)
- `aac`: AAC codec (compressed)
- `mp3`: MP3 codec (compressed)

## Sending Text

Send text to be synthesized:

```python
# Send plain text
connection.send_text("Hello, world!")

# Send longer text
connection.send_text("This is a longer passage that will be converted to speech.")
```

## Control Messages

Use control messages to manage synthesis flow:

### Flush

Forces immediate synthesis of buffered text:

```python
from deepgram.extensions.types.sockets import SpeakV1ControlMessage
connection.send_control(SpeakV1ControlMessage(type="Flush"))
```

### Close

Signals end of text input and closes the connection gracefully:

```python
connection.send_control(SpeakV1ControlMessage(type="Close"))
```

## Handling Audio

Process audio bytes in the message callback:

```python
def on_message(message: SpeakV1SocketClientResponse) -> None:
    if isinstance(message, bytes):
        # Save to file
        with open("output.raw", "ab") as f:
            f.write(message)

        # Or play directly
        # audio_player.play(message)
    else:
        print(f"Event: {message.type}")
```

## WebSocket vs REST

**Use WebSocket Speak when:**
- You need real-time streaming synthesis
- Processing long-form text progressively
- Building interactive voice applications
- Low latency is critical

**Use REST Speak when:**
- Synthesizing short text snippets
- Generating audio files for download
- Simpler implementation is preferred
- See `speak/v1/audio/generate/` for REST examples

## Next Steps

- See `async.py` for async/await pattern usage
- See `with_auth_token.py` for manual token authentication
- See `with_raw_response.py` for accessing raw WebSocket messages
- See `speak/v1/audio/generate/` for REST-based TTS

