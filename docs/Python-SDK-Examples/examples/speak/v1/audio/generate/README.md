# Generate Speech from Text (Speak API v1)

**Learning objective**: Convert text to speech using Deepgram's REST API and the Python SDK.

## Prerequisites

- **Python**: 3.10+
- **API key**: Set `DEEPGRAM_API_KEY` in your environment or `.env` file
- **Install SDK**:
```bash
pip install deepgram-sdk
```

## Basic Usage

This example shows how to generate speech from text using the Speak API.

```python
from dotenv import load_dotenv
load_dotenv()

from deepgram import DeepgramClient

client = DeepgramClient()

try:
    print("Request sent")
    response = client.speak.v1.audio.generate(
        text="Hello, this is a sample text to speech conversion.",
    )
    print("Response received")
    print(response)
except Exception as e:
    print(f"Caught: {e}")
```

## Key Concepts

- **Synchronous Call**: The `generate()` method makes a synchronous HTTP request
- **Response Object**: Returns audio data and metadata
- **Simple Interface**: Just pass text and optional parameters

## Additional Options

You can customize the speech output with additional parameters:

```python
response = client.speak.v1.audio.generate(
    text="Hello, world!",
    model="aura-2-asteria-en",  # Choose voice model
    encoding="mp3",              # Output format
    sample_rate=24000,           # Audio sample rate
)
```

Available parameters include:
- `model`: Voice model (e.g., `aura-2-asteria-en`, `aura-2-luna-en`)
- `encoding`: Audio format (`linear16`, `mp3`, `opus`, `flac`)
- `sample_rate`: Sample rate in Hz
- `container`: Audio container format

## Saving Audio to File

To save the generated audio:

```python
response = client.speak.v1.audio.generate(
    text="Hello, world!",
    model="aura-2-asteria-en",
)

# Save audio data
with open("output.mp3", "wb") as f:
    f.write(response.content)
```

## Streaming Response

For large text inputs, consider using streaming:

```python
response = client.speak.v1.audio.generate(
    text="Very long text...",
    stream=True
)

with open("output.mp3", "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
```

## Next Steps

- See `async.py` for async/await pattern usage
- See `with_auth_token.py` for manual token authentication
- See `with_raw_response.py` for accessing raw HTTP responses
- For WebSocket streaming TTS, see `speak/v1/connect/`

