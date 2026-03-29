"""
Recipe: Generate audio to file (Text-to-Speech v1)

Converts text to speech using an aura-2 voice model and saves the audio
to a local file. generate() streams chunks as they arrive from the API.
"""

import os
from deepgram import DeepgramClient

TEXT = "Hello! This is a Deepgram text-to-speech example using the aura-2 voice model."
OUTPUT_FILE = "output.mp3"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    audio_chunks = client.speak.v1.audio.generate(
        text=TEXT,
        model="aura-2-thalia-en",
    )

    with open(OUTPUT_FILE, "wb") as f:
        for chunk in audio_chunks:
            f.write(chunk)

    size = os.path.getsize(OUTPUT_FILE)
    print(f"Saved {OUTPUT_FILE}: {size} bytes")


if __name__ == "__main__":
    main()
