"""Multichannel contact center analytics: per-channel transcription with
sentiment, topic detection, and summarization for call analysis."""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        multichannel=True,
        sentiment=True,
        topics=True,
        summarize="v2",
    )

    channels = response.results.channels or []
    for i, ch in enumerate(channels):
        label = "Agent" if i == 0 else "Customer"
        transcript = ch.alternatives[0].transcript
        words = ch.alternatives[0].words or []
        duration = sum(getattr(w, "end", 0) - getattr(w, "start", 0) for w in words)
        print(f"[{label} ch{i}] {transcript[:120]}...")
        print(f"  Talk time: {duration:.1f}s | Words: {len(words)}")

    if hasattr(response.results, "sentiments") and response.results.sentiments:
        segments = getattr(response.results.sentiments, "segments", [])
        print(f"\nSentiment segments: {len(segments)}")
        for seg in segments[:5]:
            print(f"  [{getattr(seg, 'sentiment', '?')}] {getattr(seg, 'text', '')[:70]}")

    if hasattr(response.results, "topics") and response.results.topics:
        segments = getattr(response.results.topics, "segments", [])
        all_topics = {getattr(t, "topic", "") for s in segments for t in getattr(s, "topics", [])}
        print(f"\nTopics detected: {', '.join(sorted(all_topics)[:8])}")

    if hasattr(response.results, "summary") and response.results.summary:
        print(f"\nSummary: {getattr(response.results.summary, 'short', '')}")


if __name__ == "__main__":
    main()
