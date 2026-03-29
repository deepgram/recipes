"""
Recipe: Topic Detection (Speech-to-Text v1)
=============================================
Demonstrates the `topics` feature, which identifies the key topics
discussed in the audio.

Without topics: just the transcript text.
With topics:    response.results.topics contains per-segment topic lists,
                each with a topic label and confidence score.

This is an Audio Intelligence feature. For custom topic detection,
add `custom_topic` and `custom_topic_mode` parameters.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        topics=True,  # <-- THIS is the feature this recipe demonstrates.
                      # Detects topics discussed in the audio.
        # Other useful parameters: custom_topic=["space","NASA"],
        #   custom_topic_mode="extended" (detect custom + auto topics)
    )

    # Response path: response.results.topics.results.topics — topic analysis
    #   topics.segments        — list of segment objects
    #     segment.text         — the text segment
    #     segment.start_word   — start word index
    #     segment.end_word     — end word index
    #     segment.topics       — list of topic objects
    #       topic.topic            — topic label (str)
    #       topic.confidence_score — confidence (float)
    # Topics can be None if audio is too short for analysis.
    if response.results and response.results.topics:
        segments = response.results.topics.results.topics.segments
        if segments:
            for seg in segments[:5]:
                topic_labels = [t.topic for t in seg.topics]
                print(f"Topics: {', '.join(topic_labels)}")
                print(f"  Text: {seg.text}\n")


if __name__ == "__main__":
    main()
