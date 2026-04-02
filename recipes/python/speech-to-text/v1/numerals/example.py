"""
Recipe: Numerals (Speech-to-Text v1)
======================================
Demonstrates the `numerals` feature, which converts spoken numbers
from their written-out form into numeric digits.

Without numerals: "fifty" / "three hundred and twenty one"
With numerals:    "50" / "321"

Note: `smart_format` includes numeral conversion among its formatting
rules. Use `numerals` alone when you want digit conversion without
the other smart_format transformations.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        numerals=True,  # <-- THIS enables numeral conversion.
                        # Spoken numbers become digits: "fifty" → "50".
    )

    if response.results and response.results.channels:
        transcript = response.results.channels[0].alternatives[0].transcript
        print(transcript)


if __name__ == "__main__":
    main()
