# Transcribe Audio from URL (Listen API v1)

**Learning objective**: Transcribe audio from a remote URL using Deepgram's REST API and the Python SDK.

## Prerequisites

- **Python**: 3.10+
- **API key**: Set `DEEPGRAM_API_KEY` in your environment or `.env` file
- **Install SDK**:
```bash
pip install deepgram-sdk
```

## Basic Usage

This example shows how to transcribe audio from a publicly accessible URL without downloading the file first.

```python
from dotenv import load_dotenv
load_dotenv()

from deepgram import DeepgramClient

client = DeepgramClient()

try:
    print("Request sent")
    response = client.listen.v1.media.transcribe_url(
        model="nova-3",
        url="https://dpgr.am/spacewalk.wav",
    )
    print("Response received")
    print(response)
except Exception as e:
    print(f"Caught: {e}")
```

## Key Concepts

- **Synchronous Call**: The `transcribe_url()` method makes a synchronous HTTP request
- **Remote Processing**: Deepgram fetches the audio directly from the URL
- **Efficiency**: No need to download and upload the file yourself
- **Response Object**: Returns a structured transcription response with metadata

## Additional Options

You can customize the transcription with additional parameters:

```python
response = client.listen.v1.media.transcribe_url(
    model="nova-3",
    url="https://example.com/audio.mp3",
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
- `sentiment`: Analyze sentiment
- `summarize`: Generate summary
- `topics`: Extract topics
- `intents`: Detect intents

## URL Requirements

The audio URL must be:
- Publicly accessible (or use authenticated URLs if supported by your host)
- A direct link to an audio file (not a webpage)
- In a supported audio format (WAV, MP3, MP4, FLAC, etc.)

## Accessing Transcription Results

The response contains the transcription and metadata:

```python
response = client.listen.v1.media.transcribe_url(
    model="nova-3",
    url="https://example.com/audio.mp3",
)

# Access the transcript
transcript = response.results.channels[0].alternatives[0].transcript
print(f"Transcript: {transcript}")

# Access word-level details
for word in response.results.channels[0].alternatives[0].words:
    print(f"{word.word}: {word.start}s - {word.end}s")
```

## Use Cases

URL transcription is ideal for:
- Processing files from cloud storage (S3, GCS, Azure Blob)
- Transcribing podcast episodes or video URLs
- Building integrations with other services
- Avoiding file upload bandwidth

## Next Steps

- See `async.py` for async/await pattern usage
- See `transcribe_file/` for transcribing local files
- See `with_auth_token.py` for manual token authentication
- See `with_raw_response.py` for accessing raw HTTP responses

