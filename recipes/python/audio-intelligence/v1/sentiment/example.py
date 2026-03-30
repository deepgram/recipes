"""
Recipe: Sentiment Analysis (Audio Intelligence v1)
====================================================
Demonstrates segment-level sentiment analysis on audio content.

When sentiment=True is set, each segment of the transcript is scored as
positive, negative, or neutral with a confidence value. This is useful
for call-centre analytics, customer feedback analysis, or understanding
the emotional tone of conversations.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        sentiment=True,  # <-- THIS enables sentiment analysis.
    )

    if response.results and response.results.channels:
        transcript = response.results.channels[0].alternatives[0].transcript
        print(f"Transcript: {transcript[:150]}...")

    # Sentiment results appear in response.results.sentiments.segments
    if hasattr(response.results, "sentiments") and response.results.sentiments:
        segments = getattr(response.results.sentiments, "segments", [])
        print(f"\nSentiment segments: {len(segments)}")
        for seg in segments[:5]:
            sentiment = getattr(seg, "sentiment", "unknown")
            text = getattr(seg, "text", "")
            print(f"  [{sentiment}] {text[:80]}")


if __name__ == "__main__":
    main()
