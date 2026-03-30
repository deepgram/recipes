"""
Recipe: Transcribe Audio from URL — v2 API (Speech-to-Text v2)
================================================================
Demonstrates pre-recorded transcription using the flux-general-en model,
Deepgram's English-optimised high-accuracy model.

The Python SDK uses client.listen.v1.media.transcribe_url() with
model="flux-general-en" for v2 pre-recorded transcription. The response
format is the same as v1.

See also: speech-to-text/v1/transcribe-url for the v1 equivalent.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    # flux-general-en is the v2 English-only model with improved accuracy.
    # It uses the same transcribe_url() method as v1 — just change the model name.
    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="flux-general-en",  # <-- v2 English model
        smart_format=True,
    )

    if response.results and response.results.channels:
        transcript = response.results.channels[0].alternatives[0].transcript
        print(transcript)


if __name__ == "__main__":
    main()
