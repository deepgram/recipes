"""
Recipe: Entity Detection (Audio Intelligence v1)
==================================================
Demonstrates identifying named entities in audio content — people,
organisations, locations, dates, and other structured information.

This is the audio-intelligence version of entity detection. It uses the
same `detect_entities` parameter as the speech-to-text feature recipe,
but focuses on the entity extraction use case for content analysis.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        detect_entities=True,  # <-- THIS enables entity detection.
    )

    if response.results and response.results.channels:
        transcript = response.results.channels[0].alternatives[0].transcript
        print(f"Transcript: {transcript[:150]}...")

    if hasattr(response.results, "entities") and response.results.entities:
        print(f"\nDetected entities:")
        for entity in response.results.entities:
            label = getattr(entity, "label", "unknown")
            value = getattr(entity, "value", "")
            confidence = getattr(entity, "confidence", 0)
            print(f"  [{label}] {value} (confidence: {confidence:.2f})")
    else:
        print("\nNo entities detected in this audio sample.")


if __name__ == "__main__":
    main()
