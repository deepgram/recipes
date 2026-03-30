"""
Recipe: Select Voice Model (Text-to-Speech v1)
================================================
Demonstrates how to choose a specific aura-2 voice model for TTS output.

Deepgram offers multiple voice models, each with a distinct voice
personality. The `model` parameter selects which voice is used.

Available aura-2 voices include:
  aura-2-thalia-en, aura-2-arcas-en, aura-2-luna-en,
  aura-2-asteria-en, aura-2-helios-en, and more.
"""

import os
from deepgram import DeepgramClient

TEXT = "Each Deepgram voice has its own personality. This is the Arcas voice."
OUTPUT_FILE = "output.mp3"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    # Change the model parameter to hear different voices.
    # aura-2-arcas-en is a deep, authoritative male voice.
    audio_chunks = client.speak.v1.audio.generate(
        text=TEXT,
        model="aura-2-arcas-en",  # <-- THIS selects a different voice model.
    )

    with open(OUTPUT_FILE, "wb") as f:
        for chunk in audio_chunks:
            f.write(chunk)

    size = os.path.getsize(OUTPUT_FILE)
    print(f"Saved {OUTPUT_FILE} ({size} bytes) using model aura-2-arcas-en")


if __name__ == "__main__":
    main()
