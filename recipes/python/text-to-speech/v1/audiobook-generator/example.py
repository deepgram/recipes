"""
Recipe: Audiobook generator with chapter pauses (Flux TTS)
==========================================================
Splits text into paragraphs, inserts pause markers using TextBuilder,
and generates a single concatenated audio file via Flux batch REST.
"""
import os
from deepgram import DeepgramClient
from deepgram.helpers import TextBuilder

SAMPLE_TEXT = """Chapter 1: The Launch

The crew prepared for departure as mission control counted down.
Every instrument was checked twice. The engines roared to life.

The spacecraft lifted off smoothly. Within minutes they had cleared
the atmosphere and entered the silent vastness of space.

Chapter 2: The Spacewalk

Commander Williams opened the airlock. Floating free above the Earth,
she marveled at the thin blue line of the atmosphere below."""

OUTPUT_FILE = "output.mp3"


def main():
    client = DeepgramClient()
    paragraphs = [p.strip() for p in SAMPLE_TEXT.strip().split("\n\n") if p.strip()]
    audio_data = bytearray()

    for i, para in enumerate(paragraphs):
        builder = TextBuilder()
        if i > 0:
            builder.pause(1000)
        builder.text(para)
        for chunk in client.speak.v2.audio.generate(
            text=builder.build(), model="flux-alexis-en"
        ):
            audio_data.extend(chunk)

    with open(OUTPUT_FILE, "wb") as f:
        f.write(audio_data)

    size = os.path.getsize(OUTPUT_FILE)
    print(f"Generated {len(paragraphs)} paragraphs -> {OUTPUT_FILE}: {size} bytes")


if __name__ == "__main__":
    main()
