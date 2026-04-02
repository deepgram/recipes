"""
Recipe: Dictation Mode (Speech-to-Text v1)
============================================
Demonstrates the `dictation` feature, which interprets dictation-style
spoken punctuation commands such as "period", "comma", "new paragraph"
and converts them into their written equivalents in the transcript.

Without dictation: "Hello period How are you question mark"
With dictation:    "Hello. How are you?"
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        dictation=True,  # <-- THIS enables dictation mode.
                         # Spoken punctuation commands become actual punctuation.
    )

    if response.results and response.results.channels:
        transcript = response.results.channels[0].alternatives[0].transcript
        print(transcript)


if __name__ == "__main__":
    main()
