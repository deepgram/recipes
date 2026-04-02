"""
Recipe: Key Term Prompting (Speech-to-Text v1)
================================================
Demonstrates the `keyterm` feature, which boosts recognition accuracy
for specific terms, brand names, or specialized vocabulary.

Key term prompting is only compatible with Nova-3. It differs from the
older `keywords` feature by using prompt-based boosting rather than
weighted keyword biasing.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",       # keyterm requires Nova-3
        smart_format=True,
        keyterm=["Deepgram", "spacewalk", "ISS"],  # <-- THIS boosts these terms.
            # Provide a list of terms the model should prioritise recognising.
            # Useful for brand names, proper nouns, or domain-specific vocabulary.
    )

    if response.results and response.results.channels:
        transcript = response.results.channels[0].alternatives[0].transcript
        print(transcript)


if __name__ == "__main__":
    main()
