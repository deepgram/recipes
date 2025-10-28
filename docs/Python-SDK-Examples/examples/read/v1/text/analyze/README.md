# Analyze Text (Read API v1)

**Learning objective**: Analyze text for sentiment, topics, intents, and generate summaries using Deepgram's Read API and the Python SDK.

## Prerequisites

- **Python**: 3.10+
- **API key**: Set `DEEPGRAM_API_KEY` in your environment or `.env` file
- **Install SDK**:
```bash
pip install deepgram-sdk
```

## Basic Usage

This example shows how to analyze text using Deepgram's Read API for sentiment, topics, intents, and summarization.

```python
from dotenv import load_dotenv
load_dotenv()

from deepgram import DeepgramClient

client = DeepgramClient()

try:
    print("Request sent")
    response = client.read.v1.text.analyze(
        request={"text": "Hello, world!"},
        language="en",
        sentiment=True,
        summarize=True,
        topics=True,
        intents=True,
    )
    print("Response received")
    print(response)
except Exception as e:
    print(f"Caught: {e}")
```

## Key Concepts

- **Synchronous Call**: The `analyze()` method makes a synchronous HTTP request
- **Text Input**: Pass text as a dictionary with a `text` field
- **Multiple Analyses**: Enable multiple analysis types in a single request
- **Response Object**: Returns structured analysis results

## Analysis Options

Enable specific analysis features by setting them to `True`:

### Sentiment Analysis

Analyze the emotional tone of the text:

```python
response = client.read.v1.text.analyze(
    request={"text": "I absolutely love this product! It's amazing."},
    language="en",
    sentiment=True,
)

# Access sentiment results
sentiment = response.results.sentiment
print(f"Overall sentiment: {sentiment.average.sentiment}")
print(f"Confidence: {sentiment.average.sentiment_score}")
```

### Topic Detection

Identify topics discussed in the text:

```python
response = client.read.v1.text.analyze(
    request={"text": "Python is a powerful programming language for AI."},
    language="en",
    topics=True,
)

# Access detected topics
for segment in response.results.topics.segments:
    for topic in segment.topics:
        print(f"Topic: {topic.topic} (confidence: {topic.confidence})")
```

### Intent Detection

Determine the intent behind the text:

```python
response = client.read.v1.text.analyze(
    request={"text": "I would like to schedule a meeting for next Tuesday."},
    language="en",
    intents=True,
)

# Access detected intents
for segment in response.results.intents.segments:
    for intent in segment.intents:
        print(f"Intent: {intent.intent} (confidence: {intent.confidence})")
```

### Text Summarization

Generate a summary of longer text:

```python
response = client.read.v1.text.analyze(
    request={"text": "Very long text content here..."},
    language="en",
    summarize=True,
)

# Access summary
summary = response.results.summary
print(f"Summary: {summary.text}")
```

## Combining Multiple Analyses

Analyze text with all features enabled:

```python
response = client.read.v1.text.analyze(
    request={"text": "Your text content here..."},
    language="en",
    sentiment=True,
    summarize=True,
    topics=True,
    intents=True,
)

# Access all results
print(f"Sentiment: {response.results.sentiment.average.sentiment}")
print(f"Summary: {response.results.summary.text}")
print(f"Topics: {[t.topic for s in response.results.topics.segments for t in s.topics]}")
print(f"Intents: {[i.intent for s in response.results.intents.segments for i in s.intents]}")
```

## Supported Languages

The `language` parameter supports various language codes:
- `en`: English
- `es`: Spanish
- `fr`: French
- `de`: German
- `ja`: Japanese
- `zh`: Chinese
- And more...

## Use Cases

The Read API is ideal for:
- Content moderation and sentiment tracking
- Topic extraction from articles or reviews
- Intent classification for customer support
- Automatic summarization of long documents
- Analyzing transcripts from the Listen API

## Next Steps

- See `async.py` for async/await pattern usage
- See `with_auth_token.py` for manual token authentication
- See `with_raw_response.py` for accessing raw HTTP responses
- Combine with `listen/v1/media/` to analyze transcribed audio

