"""
Recipe: Smart Format (Speech-to-Text v1)
=========================================
Demonstrates the `smart_format` feature, which automatically applies formatting
to transcripts: numbers become digits, dates are standardized, currencies get
symbols, and addresses are formatted conventionally.

Without smart_format: "three hundred dollars on january first twenty twenty five"
With smart_format:    "$300 on January 1st, 2025"

Related recipes: punctuate (adds punctuation only, without number/date formatting).
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,  # <-- THIS is the feature this recipe demonstrates.
                            # Formats numbers, dates, currencies, addresses, etc.
                            # Also implies punctuate=True behavior.
        # Other useful parameters: punctuate=True, numerals=True, measurements=True
    )

    # Response path: response.results.channels[0].alternatives[0].transcript
    # The transcript string itself contains the formatted text — no separate
    # structured field. Compare this output against the transcribe-url recipe
    # (which also uses smart_format) to see formatting in action.
    if response.results and response.results.channels:
        transcript = response.results.channels[0].alternatives[0].transcript
        print(transcript)


if __name__ == "__main__":
    main()
