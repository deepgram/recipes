"""
Recipe: Bit Rate Control (Text-to-Speech v1)
==============================================
Demonstrates the `bit_rate` parameter, which controls the output audio
bit rate for compressed encodings like mp3.

Lower bit rates produce smaller files at the cost of audio quality.
Higher bit rates preserve more audio detail. Common mp3 bit rates:
  32000  — low quality, small files (voice-only, bandwidth-constrained)
  48000  — medium quality
  128000 — high quality (default for mp3)
  192000 — very high quality
"""

import os
from deepgram import DeepgramClient

TEXT = "Hello! This audio demonstrates bit rate control with Deepgram text-to-speech."
OUTPUT_FILE = "output.mp3"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    audio_chunks = client.speak.v1.audio.generate(
        text=TEXT,
        model="aura-2-thalia-en",
        encoding="mp3",
        bit_rate=48000,  # <-- THIS controls the output bit rate.
                         # 48 kbps mp3 — smaller file, suitable for voice content.
    )

    with open(OUTPUT_FILE, "wb") as f:
        for chunk in audio_chunks:
            f.write(chunk)

    size = os.path.getsize(OUTPUT_FILE)
    print(f"Saved {OUTPUT_FILE} ({size} bytes) — encoding: mp3, bit_rate: 48000")


if __name__ == "__main__":
    main()
