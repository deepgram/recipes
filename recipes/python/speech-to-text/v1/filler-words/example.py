"""
Recipe: Filler Words (Speech-to-Text v1)
=========================================
Demonstrates the `filler_words` feature, which captures spoken filler
words like "uh", "um", "mhm", and "uh-huh" in the transcript.

Without filler_words: fillers are silently dropped from the transcript.
With filler_words:    fillers appear inline, reflecting natural speech.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        filler_words=True,  # <-- THIS enables filler word capture.
                            # "uh", "um", "mhm" etc. appear in the transcript.
    )

    if response.results and response.results.channels:
        transcript = response.results.channels[0].alternatives[0].transcript
        print(transcript)


if __name__ == "__main__":
    main()
