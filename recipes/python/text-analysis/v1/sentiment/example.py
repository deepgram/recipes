"""
Recipe: Sentiment Analysis (Text Analysis v1)
===============================================
Demonstrates the `sentiment` feature on Deepgram's text analysis API,
which analyzes sentiment (positive, negative, neutral) on plain text.

Text analysis (Read API) works directly on text — no audio required.
Returns both an overall average sentiment and per-segment breakdowns.
"""

from deepgram import DeepgramClient

TEXT = (
    "I absolutely love this product! It exceeded all my expectations. "
    "However, the shipping was terrible and took three weeks to arrive. "
    "Overall, I'm satisfied with my purchase despite the delivery issues."
)


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.read.v1.text.analyze(
        request={"text": TEXT},
        language="en",
        sentiment=True,  # <-- THIS enables sentiment analysis on plain text.
    )

    if response.results and response.results.sentiments:
        avg = response.results.sentiments.average
        print(f"Average sentiment: {avg.sentiment} (confidence: {avg.sentiment_score:.2f})")
        for segment in response.results.sentiments.segments:
            print(f"  [{segment.sentiment}] {segment.text}")


if __name__ == "__main__":
    main()
