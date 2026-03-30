"""
Recipe: WebSocket Streaming TTS (Text-to-Speech v1)
=====================================================
Demonstrates low-latency text-to-speech via WebSocket for real-time use.

Unlike the REST-based generate() method, WebSocket TTS lets you send text
incrementally and receive audio as it's synthesised. This is ideal for
conversational UIs where text is produced word-by-word (e.g., from an LLM).

The client sends SpeakV1Text messages, then flush/close. Audio arrives
as binary MESSAGE events.
"""

from deepgram import DeepgramClient
from deepgram.core.events import EventType
from deepgram.speak.v1.types import SpeakV1Text


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment
    audio_size = 0

    with client.speak.v1.connect(
        model="aura-2-thalia-en",
        encoding="linear16",
        sample_rate=24000,
    ) as connection:

        def on_message(message) -> None:
            nonlocal audio_size
            if isinstance(message, bytes):
                audio_size += len(message)

        connection.on(EventType.MESSAGE, on_message)

        connection.send_text(SpeakV1Text(text="Hello! This is WebSocket streaming TTS."))
        connection.send_flush()
        connection.send_close()
        connection.start_listening()

    print(f"Received {audio_size} bytes of audio via WebSocket")


if __name__ == "__main__":
    main()
