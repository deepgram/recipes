"""
Recipe: Transcribe local audio file — v2 API (Speech-to-Text v2)
=================================================================
Demonstrates local-file transcription using the flux-general-en model,
Deepgram's highest-accuracy English model. The file bytes are sent via
transcribe_file() with model="flux-general-en".

See also: speech-to-text/v1/transcribe-file for the v1 equivalent.
"""

import urllib.request
from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    # Download a sample audio file to demonstrate local-file transcription.
    # In production you would open an existing local file instead.
    audio_data = urllib.request.urlopen(AUDIO_URL).read()
    print(f"Downloaded {len(audio_data)} bytes")

    # flux-general-en is the v2 English-only model with improved accuracy.
    # transcribe_file() accepts raw bytes — just set model to "flux-general-en".
    response = client.listen.v1.media.transcribe_file(
        request=audio_data,
        model="flux-general-en",
        smart_format=True,
    )

    if response.results and response.results.channels:
        alt = response.results.channels[0].alternatives[0]
        print(alt.transcript)

        # Print word-level timestamps and confidence scores
        for w in alt.words[:10]:
            print(f"  {w.word:15s}  {w.start:.2f}s - {w.end:.2f}s  (conf: {w.confidence:.3f})")


if __name__ == "__main__":
    main()
