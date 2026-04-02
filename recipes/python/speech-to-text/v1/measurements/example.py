"""
Recipe: Measurements (Speech-to-Text v1)
==========================================
Demonstrates the `measurements` feature, which converts spoken
measurement phrases into their standard abbreviated forms.

Without measurements: "five feet ten inches" / "twenty degrees celsius"
With measurements:    "5 ft 10 in" / "20°C"
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        measurements=True,  # <-- THIS enables measurement conversion.
                            # Spoken measurements become standard abbreviations.
    )

    if response.results and response.results.channels:
        transcript = response.results.channels[0].alternatives[0].transcript
        print(transcript)


if __name__ == "__main__":
    main()
