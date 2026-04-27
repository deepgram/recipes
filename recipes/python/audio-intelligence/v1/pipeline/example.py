"""
Recipe: Audio Intelligence Pipeline (Audio Intelligence v1)
Combines sentiment, entity detection, topics, summarization, and PII
redaction in a single API call — one request, full audio analysis.
"""
from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment
    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        sentiment=True,
        detect_entities=True,
        topics=True,
        summarize="v2",
        redact="pci",
    )

    transcript = response.results.channels[0].alternatives[0].transcript
    print(f"Transcript: {transcript[:120]}...")

    if hasattr(response.results, "summary") and response.results.summary:
        print(f"\nSummary: {getattr(response.results.summary, 'short', '')}")

    if hasattr(response.results, "sentiments") and response.results.sentiments:
        segs = getattr(response.results.sentiments, "segments", [])
        print(f"\nSentiment segments: {len(segs)}")
        for s in segs[:3]:
            print(f"  [{getattr(s, 'sentiment', '')}] {getattr(s, 'text', '')[:60]}")

    if hasattr(response.results, "topics") and response.results.topics:
        segs = getattr(response.results.topics, "segments", [])
        print(f"\nTopic segments: {len(segs)}")
        for s in segs[:3]:
            names = [getattr(t, "topic", "") for t in getattr(s, "topics", [])]
            print(f"  {', '.join(names)}")

    if hasattr(response.results, "entities") and response.results.entities:
        print(f"\nEntities: {len(response.results.entities)}")
        for e in response.results.entities[:5]:
            print(f"  [{getattr(e, 'label', '')}] {getattr(e, 'value', '')}")


if __name__ == "__main__":
    main()
