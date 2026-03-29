"""
Recipe: Summarize (Speech-to-Text v1)
======================================
Demonstrates the `summarize` feature, which generates a concise text summary
of the transcribed audio content.

Without summarize: you get only the raw transcript.
With summarize:    response.results.summary contains a short/result summary,
                   plus per-segment summaries in the alternatives.

This is an Audio Intelligence feature that adds a small amount of latency
to the transcription request.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        summarize="v2",  # <-- THIS is the feature this recipe demonstrates.
                         # Generates a summary. Value must be "v2" (string, not bool).
        # Other useful parameters: topics=True, sentiment=True, intents=True
    )

    # Response path: response.results.summary — overall summary object
    #   summary.short   — short summary string
    #   summary.result  — result status string
    # Also: response.results.channels[0].alternatives[0].summaries — per-segment list
    #   item.summary    — segment summary text
    #   item.start_word — start word index
    #   item.end_word   — end word index
    # Summary may be None if the audio is too short to summarize.
    if response.results:
        if response.results.summary:
            print(f"Summary: {response.results.summary.short}")
        alt = response.results.channels[0].alternatives[0]
        if alt.summaries:
            for s in alt.summaries:
                print(f"  Segment: {s.summary}")


if __name__ == "__main__":
    main()
