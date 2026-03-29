"""
Recipe: Punctuation (Speech-to-Text v1)
========================================
Demonstrates the `punctuate` feature, which adds punctuation and capitalization
to the transcript output.

Without punctuate: "yeah as much as its worth celebrating"
With punctuate:    "Yeah, as much as it's worth celebrating"

For broader formatting (numbers, dates, currencies), see: smart-format.
smart_format=True implies punctuation, but punctuate=True alone is lighter.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        punctuate=True,  # <-- THIS is the feature this recipe demonstrates.
                         # Adds punctuation marks and capitalization to the transcript.
        # Other useful parameters: smart_format=True, dictation=True
    )

    # Response path: response.results.channels[0].alternatives[0].transcript
    # Punctuation appears inline in the transcript string itself.
    # No separate structured field — just compare the output with and without.
    if response.results and response.results.channels:
        transcript = response.results.channels[0].alternatives[0].transcript
        print(transcript)


if __name__ == "__main__":
    main()
