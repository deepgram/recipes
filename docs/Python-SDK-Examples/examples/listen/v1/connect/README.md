# Live Transcription via WebSocket (Listen API v1)

**Learning objective**: Establish a WebSocket connection to stream audio and receive real-time transcription results using the Python SDK.

## Prerequisites

- **Python**: 3.10+
- **API key**: Set `DEEPGRAM_API_KEY` in your environment or `.env` file
- **Install SDK**:
```bash
pip install deepgram-sdk
```

## Basic Usage

This example shows how to connect to Deepgram's live transcription WebSocket endpoint using a context manager pattern.

```python
import threading
import time

from dotenv import load_dotenv
load_dotenv()

from deepgram import DeepgramClient
from deepgram.core.events import EventType
from deepgram.extensions.types.sockets import ListenV1SocketClientResponse

client = DeepgramClient()

try:
    with client.listen.v1.connect(model="nova-3") as connection:
        def on_message(message: ListenV1SocketClientResponse) -> None:
            msg_type = getattr(message, "type", "Unknown")
            print(f"Received {msg_type} event")
        
        connection.on(EventType.OPEN, lambda _: print("Connection opened"))
        connection.on(EventType.MESSAGE, on_message)
        connection.on(EventType.CLOSE, lambda _: print("Connection closed"))
        connection.on(EventType.ERROR, lambda error: print(f"Caught: {error}"))

        # Start listening - blocks until connection closes
        connection.start_listening()
except Exception as e:
    print(f"Caught: {e}")
```

## Key Concepts

- **Context Manager**: The `with` statement ensures proper connection cleanup
- **Event Handlers**: Register callbacks for connection lifecycle events using `EventType`
- **Message Types**: The `ListenV1SocketClientResponse` provides typed responses
- **Blocking Call**: `start_listening()` blocks the thread until the connection closes

## Additional Options

You can pass additional parameters when connecting:

```python
with client.listen.v1.connect(
    model="nova-3",
    language="en-US",
    smart_format=True,
    punctuate=True,
    diarize=True
) as connection:
    # ... setup handlers and start listening
```

Refer to the Deepgram API documentation for all available transcription parameters.

## Sending Audio

Once connected, send audio data to the connection:

```python
# Example: Send audio chunks
audio_data = b"..."  # Your audio bytes
connection.send(audio_data)
```

## Next Steps

- See `async.py` for async/await pattern usage
- See `with_auth_token.py` for manual token authentication
- See `with_raw_response.py` for accessing raw WebSocket messages

