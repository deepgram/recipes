"""
Recipe: Stream Audio File for Transcription (Speech-to-Text v1)
================================================================
Demonstrates streaming a local audio file over WebSocket for transcription.

This is the same WebSocket API as the live-streaming recipe, but instead
of microphone input, a local file is read and sent in chunks. Useful for
processing large files where you want incremental results rather than
waiting for the entire file to upload.
"""

import threading
import time
import urllib.request

from deepgram import DeepgramClient
from deepgram.core.events import EventType
from deepgram.listen.v1.types import ListenV1Results

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment
    audio_data = urllib.request.urlopen(AUDIO_URL).read()
    print(f"Streaming {len(audio_data)} bytes over WebSocket")

    with client.listen.v1.connect(
        model="nova-3",
        smart_format=True,
    ) as connection:

        def on_message(message) -> None:
            if isinstance(message, ListenV1Results):
                transcript = message.channel.alternatives[0].transcript
                if transcript:
                    print(transcript)

        connection.on(EventType.MESSAGE, on_message)

        def send_audio():
            chunk_size = 8192
            for i in range(0, len(audio_data), chunk_size):
                connection.send_media(audio_data[i : i + chunk_size])
                time.sleep(0.01)
            time.sleep(2)
            connection.send_close_stream()

        sender = threading.Thread(target=send_audio, daemon=True)
        sender.start()
        connection.start_listening()


if __name__ == "__main__":
    main()
