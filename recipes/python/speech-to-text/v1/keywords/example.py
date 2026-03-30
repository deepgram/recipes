"""
Recipe: Keyword Boosting (Speech-to-Text v1)
=============================================
Demonstrates the `keywords` feature, which boosts recognition accuracy
for specific words or phrases.

Keyword boosting is especially useful for proper nouns, brand names,
or domain jargon that the model might not recognise out of the box.

Format: "word:intensifier" where intensifier is a float (-10 to 10).
Positive values boost the keyword; negative values suppress it.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        keywords="Deepgram:2",  # <-- boost "Deepgram" recognition by intensifier 2.
    )

    if response.results and response.results.channels:
        transcript = response.results.channels[0].alternatives[0].transcript
        print(transcript)


if __name__ == "__main__":
    main()
