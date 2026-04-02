"""
Recipe: Intent Recognition (Text Analysis v1)
===============================================
Demonstrates the `intents` feature on Deepgram's text analysis API,
which detects speaker intents from plain text input.

Text analysis (Read API) works directly on text — no audio required.
This is different from speech-to-text intent detection, which operates
on transcribed audio.
"""

from deepgram import DeepgramClient

TEXT = (
    "I'd like to return this product and get a refund. "
    "The item arrived damaged and I'm very disappointed with the quality. "
    "Can you also update my shipping address for future orders?"
)


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.read.v1.text.analyze(
        request={"text": TEXT},
        language="en",
        intents=True,  # <-- THIS enables intent recognition on plain text.
    )

    if response.results and response.results.intents:
        for segment in response.results.intents.segments:
            print(f"Text: {segment.text}")
            if segment.intents:
                for intent in segment.intents:
                    print(f"  Intent: {intent.intent} (confidence: {intent.confidence_score:.2f})")


if __name__ == "__main__":
    main()
