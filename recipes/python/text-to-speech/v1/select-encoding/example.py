"""
Recipe: Select Audio Encoding (Text-to-Speech v1)
===================================================
Demonstrates how to choose the output audio encoding for TTS.

By default, generate() returns mp3 audio. You can request different
encodings: linear16 (raw PCM), mp3, opus, flac, aac, or mulaw.
The `container` parameter controls whether a container format (e.g., WAV
header) wraps the raw audio. Set container="none" for headerless output.
"""

import os
from deepgram import DeepgramClient

TEXT = "This audio was generated in linear16 encoding at 24000 Hz sample rate."
OUTPUT_FILE = "output.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    # encoding="linear16" produces raw PCM audio.
    # container="wav" wraps it in a WAV header so media players can open it.
    audio_chunks = client.speak.v1.audio.generate(
        text=TEXT,
        model="aura-2-thalia-en",
        encoding="linear16",   # <-- THIS selects the output encoding.
        container="wav",       # Wrap PCM in a WAV container.
        sample_rate=24000,     # Output sample rate in Hz.
    )

    with open(OUTPUT_FILE, "wb") as f:
        for chunk in audio_chunks:
            f.write(chunk)

    size = os.path.getsize(OUTPUT_FILE)
    print(f"Saved {OUTPUT_FILE} ({size} bytes) — encoding: linear16, container: wav")


if __name__ == "__main__":
    main()
