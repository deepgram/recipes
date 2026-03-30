"""
Recipe: Live Streaming Transcription (Speech-to-Text v1)
=========================================================
Demonstrates real-time WebSocket-based transcription using the v1 API.

A WebSocket connection is opened with `client.listen.v1.connect()`,
audio bytes are sent via `send_media()`, and partial/final transcripts
arrive as `ListenV1Results` events. This recipe downloads a WAV file
and streams it to simulate live audio input.
"""

import threading
import time
import urllib.request
from typing import Union

from deepgram import DeepgramClient
from deepgram.core.events import EventType
from deepgram.listen.v1.types import ListenV1Metadata, ListenV1Results

AUDIO_URL = "https://dpgr.am/spacewalk.wav"
ListenV1Response = Union[ListenV1Results, ListenV1Metadata]


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment
    audio_data = urllib.request.urlopen(AUDIO_URL).read()

    with client.listen.v1.connect(
        model="nova-3",
        smart_format=True,
        interim_results=True,  # <-- receive partial results as audio is processed
    ) as connection:

        def on_message(message: ListenV1Response) -> None:
            if isinstance(message, ListenV1Results):
                transcript = message.channel.alternatives[0].transcript
                if transcript:
                    is_final = getattr(message, "is_final", False)
                    label = "final" if is_final else "interim"
                    print(f"[{label}] {transcript}")

        connection.on(EventType.MESSAGE, on_message)

        def send_audio():
            chunk_size = 4096
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
