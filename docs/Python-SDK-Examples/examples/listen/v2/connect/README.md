# Live Transcription via WebSocket (Listen API v2)

**Learning objective**: Establish a WebSocket connection using Listen API v2 to stream audio and receive real-time transcription with enhanced features.

## Prerequisites

- **Python**: 3.10+
- **API key**: Set `DEEPGRAM_API_KEY` in your environment or `.env` file
- **Install SDK**:
```bash
pip install deepgram-sdk
```

## Basic Usage

This example shows how to connect to Deepgram's Listen API v2 WebSocket endpoint with explicit audio configuration.

```python
import threading
import time

from dotenv import load_dotenv
load_dotenv()

from deepgram import DeepgramClient
from deepgram.core.events import EventType
from deepgram.extensions.types.sockets import ListenV2SocketClientResponse

client = DeepgramClient()

try:
    with client.listen.v2.connect(
        model="flux-general-en",
        encoding="linear16",
        sample_rate="16000"
    ) as connection:
        def on_message(message: ListenV2SocketClientResponse) -> None:
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

- **Listen API v2**: Enhanced version with improved features and configuration
- **Context Manager**: The `with` statement ensures proper connection cleanup
- **Explicit Audio Format**: Requires `encoding` and `sample_rate` parameters
- **Event Handlers**: Register callbacks for connection lifecycle events using `EventType`
- **Message Types**: The `ListenV2SocketClientResponse` provides typed responses

## v2 vs v1 Differences

Listen API v2 introduces several improvements:

1. **Required Audio Configuration**: Must specify `encoding` and `sample_rate` upfront
2. **Enhanced Models**: Access to newer models like `flux-general-en`
3. **Improved Performance**: Better latency and accuracy
4. **New Features**: Additional transcription features and options

## Audio Configuration

v2 requires explicit audio format specification:

```python
with client.listen.v2.connect(
    model="flux-general-en",
    encoding="linear16",       # Required: audio encoding
    sample_rate="16000",       # Required: sample rate in Hz
) as connection:
    # ... setup handlers and start listening
```

Supported encodings:
- `linear16`: 16-bit PCM
- `mulaw`: μ-law encoding
- `alaw`: A-law encoding
- `opus`: Opus codec
- `flac`: FLAC codec

## Additional Options

You can pass additional parameters when connecting:

```python
with client.listen.v2.connect(
    model="flux-general-en",
    encoding="linear16",
    sample_rate="16000",
    language="en-US",
    smart_format=True,
    punctuate=True,
    diarize=True,
    interim_results=True,
) as connection:
    # ... setup handlers and start listening
```

Available parameters include:
- `model`: Speech model (e.g., `flux-general-en`)
- `encoding`: Audio encoding format
- `sample_rate`: Sample rate in Hz
- `language`: Language code
- `smart_format`: Apply smart formatting
- `punctuate`: Add punctuation
- `diarize`: Speaker diarization
- `interim_results`: Get interim transcription results
- `utterance_end_ms`: Utterance end detection threshold

## Sending Audio

Once connected, send audio data to the connection:

```python
# Example: Send audio chunks
audio_data = b"..."  # Your audio bytes in specified format
connection.send(audio_data)
```

Ensure your audio matches the `encoding` and `sample_rate` you specified.

## Next Steps

- See `async.py` for async/await pattern usage
- See `with_auth_token.py` for manual token authentication
- See `with_raw_response.py` for accessing raw WebSocket messages
- Compare with `listen/v1/connect/` to understand differences from v1

