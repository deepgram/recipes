"""
Recipe: Sentiment Analysis (Speech-to-Text v1)
================================================
Demonstrates the `sentiment` feature, which analyzes the emotional tone
of the transcript at both the segment level and as an overall average.

Without sentiment: just the transcript text.
With sentiment:    response.results.sentiments contains per-segment sentiment
                   labels (positive/negative/neutral) with confidence scores,
                   plus an overall average.

This is an Audio Intelligence feature.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        sentiment=True,  # <-- THIS is the feature this recipe demonstrates.
                         # Adds sentiment analysis to the response.
        # Other useful parameters: topics=True, intents=True, summarize="v2"
    )

    # Response path: response.results.sentiments — sentiment analysis object
    #   sentiments.average.sentiment       — overall sentiment label (str)
    #   sentiments.average.sentiment_score — overall score (float)
    #   sentiments.segments                — list of segment objects
    #     segment.text            — the text segment
    #     segment.sentiment       — "positive", "negative", or "neutral"
    #     segment.sentiment_score — confidence score (float)
    #     segment.start_word      — start word index
    #     segment.end_word        — end word index
    # Sentiments can be None if audio is too short for analysis.
    if response.results and response.results.sentiments:
        avg = response.results.sentiments.average
        print(f"Overall: {avg.sentiment} ({avg.sentiment_score:.3f})")
        if response.results.sentiments.segments:
            for seg in response.results.sentiments.segments[:5]:
                print(f"  [{seg.sentiment}] {seg.text}")


if __name__ == "__main__":
    main()
