# Transcribe Audio File (Listen API v1)

**Learning objective**: Transcribe a local audio file using Deepgram's REST API and the Python SDK.

## Prerequisites

- **Python**: 3.10+
- **API key**: Set `DEEPGRAM_API_KEY` in your environment or `.env` file
- **Install SDK**:
```bash
pip install deepgram-sdk
```

## Basic Usage

This example shows how to transcribe an audio file by reading it into memory and sending it to Deepgram's transcription endpoint.

```python
from dotenv import load_dotenv
load_dotenv()

from deepgram import DeepgramClient

client = DeepgramClient()

try:
    # Read audio file
    with open("audio.wav", "rb") as audio_file:
        audio_data = audio_file.read()

    print("Request sent")
    response = client.listen.v1.media.transcribe_file(
        request=audio_data,
        model="nova-3",
    )
    print("Response received")
    print(response)
except Exception as e:
    print(f"Caught: {e}")
```

## Key Concepts

- **Synchronous Call**: The `transcribe_file()` method makes a synchronous HTTP request
- **Binary Data**: Pass the raw audio bytes as the `request` parameter
- **Response Object**: Returns a structured transcription response with metadata

## Additional Options

You can customize the transcription with additional parameters:

```python
response = client.listen.v1.media.transcribe_file(
    request=audio_data,
    model="nova-3",
    language="en-US",
    smart_format=True,
    punctuate=True,
    diarize=True,
    utterances=True,
    paragraphs=True,
)
```

Available parameters include:
- `model`: Speech model (`nova-3`, `nova-2`, `base`, `enhanced`)
- `language`: Language code (e.g., `en-US`, `es`, `fr`)
- `smart_format`: Apply smart formatting to transcripts
- `punctuate`: Add punctuation
- `diarize`: Identify different speakers
- `utterances`: Segment by utterances
- `paragraphs`: Structure output as paragraphs
- `detect_language`: Auto-detect language

## Supported Audio Formats

Deepgram supports many audio formats including:
- WAV
- MP3
- MP4
- FLAC
- OGG
- WebM
- And more

## Accessing Transcription Results

The response contains the transcription and metadata:

```python
response = client.listen.v1.media.transcribe_file(
    request=audio_data,
    model="nova-3",
)

# Access the transcript
transcript = response.results.channels[0].alternatives[0].transcript
print(f"Transcript: {transcript}")

# Access word-level details
for word in response.results.channels[0].alternatives[0].words:
    print(f"{word.word}: {word.start}s - {word.end}s")
```

## Large Files

For very large files, consider:
- Using the async version (see `async.py`)
- Streaming via WebSocket (see `listen/v1/connect/`)
- Using callback URLs for async processing

## Next Steps

- See `async.py` for async/await pattern usage
- See `transcribe_url/` for transcribing remote URLs
- See `with_auth_token.py` for manual token authentication
- See `with_raw_response.py` for accessing raw HTTP responses

