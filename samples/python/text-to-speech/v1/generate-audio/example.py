"""
Recipe: Generate audio to file (Text-to-Speech v1)
====================================================
Demonstrates the basic TTS operation: convert text to speech and save
the audio to a local file.

generate() returns an Iterator[bytes] that streams audio chunks as they
arrive from the API — so writing begins immediately without waiting for
the full audio to download. This is the simplest TTS recipe; see also:
- text-to-speech/v1/stream-audio     — stream chunks without saving to file
- text-to-speech/v1/websocket-streaming — low-latency WebSocket TTS
"""

import os
from deepgram import DeepgramClient

TEXT = "Hello! This is a Deepgram text-to-speech example using the aura-2 voice model."

# Output file — the encoding below (default: mp3) determines the extension.
# Change to "output.wav" if you switch encoding to linear16.
OUTPUT_FILE = "output.mp3"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    # client.speak.v1.audio.generate() streams audio chunks as an iterator.
    # Parameters:
    #   text  — the text to synthesise (string, required)
    #   model — the aura-2 voice model to use (see README for all options)
    # Optional parameters you can add here:
    #   encoding="linear16"  — raw PCM instead of mp3
    #   sample_rate=24000    — output sample rate in Hz
    audio_chunks = client.speak.v1.audio.generate(
        text=TEXT,
        model="aura-2-thalia-en",  # <-- THIS selects the voice. Change this to hear
                                   # different voices (aura-2-arcas-en, aura-2-luna-en, etc.)
    )

    # Write chunks to file as they arrive — no need to buffer the full response
    with open(OUTPUT_FILE, "wb") as f:
        for chunk in audio_chunks:
            f.write(chunk)

    size = os.path.getsize(OUTPUT_FILE)
    print(f"Saved {OUTPUT_FILE}: {size} bytes")


if __name__ == "__main__":
    main()
