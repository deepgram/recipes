"""
Recipe: Entity Detection (Speech-to-Text v1)
=============================================
Demonstrates the `detect_entities` feature, which identifies named entities
— people, places, organisations, dates, etc. — in the transcript.

Without detect_entities: no entity metadata.
With detect_entities:    the response includes a `entities` object containing
                         categorised entity mentions with their positions.
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
        print(transcript[:200])

    # Entities are returned in response.results.entities.
    # Each entity has: label (category), value (text), confidence, start/end times.
    if hasattr(response.results, "entities") and response.results.entities:
        print("\nDetected entities:")
        for entity in response.results.entities:
            label = getattr(entity, "label", "unknown")
            value = getattr(entity, "value", "")
            confidence = getattr(entity, "confidence", 0)
            print(f"  [{label}] {value} (confidence: {confidence:.2f})")


if __name__ == "__main__":
    main()
