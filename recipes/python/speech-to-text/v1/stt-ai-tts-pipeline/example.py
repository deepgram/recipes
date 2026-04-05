"""
Recipe: STT → Audio Intelligence → TTS Pipeline
End-to-end: transcribe, analyse (sentiment/topics/summary), speak the summary.
"""
import os
from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"
OUTPUT_FILE = "output.mp3"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    print("=== Stage 1: Speech-to-Text + Audio Intelligence ===")
    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL, model="nova-3", smart_format=True,
        summarize="v2", sentiment=True, topics=True,
    )
    transcript = response.results.channels[0].alternatives[0].transcript
    print(f"Transcript: {transcript[:120]}...")

    if hasattr(response.results, "sentiments") and response.results.sentiments:
        segs = getattr(response.results.sentiments, "segments", [])
        print(f"Sentiment segments: {len(segs)}")
        for s in segs[:3]:
            print(f"  [{getattr(s, 'sentiment', '?')}] {getattr(s, 'text', '')[:60]}")

    if hasattr(response.results, "topics") and response.results.topics:
        for seg in getattr(response.results.topics, "segments", [])[:3]:
            names = [getattr(t, "topic", "") for t in getattr(seg, "topics", [])]
            print(f"  Topics: {', '.join(names)}")

    summary = ""
    if hasattr(response.results, "summary") and response.results.summary:
        summary = getattr(response.results.summary, "short", "")
        print(f"\nSummary: {summary}")

    print("\n=== Stage 2: Text-to-Speech ===")
    audio_chunks = client.speak.v1.audio.generate(
        text=summary or transcript[:200], model="aura-2-thalia-en",
    )
    with open(OUTPUT_FILE, "wb") as f:
        for chunk in audio_chunks:
            f.write(chunk)
    print(f"Saved spoken summary: {OUTPUT_FILE} ({os.path.getsize(OUTPUT_FILE)} bytes)")


if __name__ == "__main__":
    main()
