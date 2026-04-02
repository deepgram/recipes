"""
Recipe: Topic Detection (Text Analysis v1)
============================================
Demonstrates the `topics` feature on Deepgram's text analysis API,
which identifies topics discussed in plain text input.

Text analysis (Read API) works directly on text — no audio required.
Returns per-segment topic lists with confidence scores.
"""

from deepgram import DeepgramClient

TEXT = (
    "The new electric vehicle from Tesla features a range of 400 miles "
    "and uses a revolutionary battery technology. Meanwhile, SpaceX "
    "successfully launched another batch of Starlink satellites into orbit. "
    "In healthcare news, a new mRNA vaccine shows promising results in "
    "early clinical trials for treating certain types of cancer."
)


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.read.v1.text.analyze(
        request={"text": TEXT},
        language="en",
        topics=True,  # <-- THIS enables topic detection on plain text.
    )

    if response.results and response.results.topics:
        for segment in response.results.topics.segments:
            print(f"Text: {segment.text}")
            if segment.topics:
                for topic in segment.topics:
                    print(f"  Topic: {topic.topic} (confidence: {topic.confidence_score:.2f})")


if __name__ == "__main__":
    main()
