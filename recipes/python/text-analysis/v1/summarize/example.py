"""
Recipe: Text Summarization (Text Analysis v1)
===============================================
Demonstrates the `summarize` feature on Deepgram's text analysis API,
which generates a concise summary from plain text input.

Text analysis (Read API) works directly on text — no audio required.
The summarize parameter for the Read API accepts a boolean (unlike the
Listen API which uses "v2" as a string value).
"""

from deepgram import DeepgramClient

TEXT = (
    "Deepgram is an AI speech company that provides automatic speech recognition "
    "and text-to-speech APIs. Their Nova-3 model offers state-of-the-art accuracy "
    "for transcription. The company also provides audio intelligence features like "
    "sentiment analysis, topic detection, and intent recognition. Developers can "
    "integrate Deepgram into their applications using SDKs for Python, JavaScript, "
    "Go, .NET, and other languages."
)


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.read.v1.text.analyze(
        request={"text": TEXT},
        language="en",
        summarize="v2",  # <-- THIS enables text summarization.
    )

    if response.results and response.results.summary:
        print(f"Summary: {response.results.summary.text}")


if __name__ == "__main__":
    main()
