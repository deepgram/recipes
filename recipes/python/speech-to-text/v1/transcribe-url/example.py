"""
Recipe: Transcribe audio from URL (Speech-to-Text v1)
======================================================
Demonstrates the most basic pre-recorded transcription operation:
send a URL pointing to a hosted audio file, get back a text transcript.

This is the foundation recipe. All other speech-to-text recipes
build on this pattern by adding feature flags (see: paragraphs,
diarize, smart-format, etc. in sibling directories).
"""

from deepgram import DeepgramClient

# Demo audio provided by Deepgram — a short spacewalk news segment.
# Any publicly accessible audio URL works here (mp3, wav, flac, ogg, etc.)
AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    # DeepgramClient() with no args reads DEEPGRAM_API_KEY from the environment.
    # Do not pass the key explicitly — keep secrets out of code.
    client = DeepgramClient()

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,         # the audio to transcribe
        model="nova-3",        # nova-3 is the highest-accuracy model for most use cases
        smart_format=True,     # formats numbers, dates, currencies, and addresses automatically
    )

    # The transcript lives at: response.results.channels[0].alternatives[0].transcript
    # channels[0]      — first audio channel (use multichannel=True for multi-track audio)
    # alternatives[0]  — highest-confidence transcript (lower alternatives exist when multiple
    #                    interpretations are possible)
    if response.results and response.results.channels:
        transcript = response.results.channels[0].alternatives[0].transcript
        print(transcript)


if __name__ == "__main__":
    main()
