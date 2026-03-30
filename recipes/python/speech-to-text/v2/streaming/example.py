"""
Recipe: Live Streaming Transcription — v2 API (Speech-to-Text v2)
==================================================================
Demonstrates real-time WebSocket transcription using the v2 API with
the flux-general-en model and contextual turn detection.

The v2 API (`client.listen.v2.connect()`) returns `ListenV2TurnInfo`
events instead of v1's `ListenV1Results`. TurnInfo provides a transcript
along with turn_index and event type for conversational context.
"""

import threading
import time
import urllib.request
from typing import Union

from deepgram import DeepgramClient
from deepgram.core.events import EventType
from deepgram.listen.v2.types import ListenV2CloseStream, ListenV2Connected, ListenV2TurnInfo

AUDIO_URL = "https://dpgr.am/spacewalk.wav"
ListenV2Response = Union[ListenV2Connected, ListenV2TurnInfo]


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment
    audio_data = urllib.request.urlopen(AUDIO_URL).read()

    with client.listen.v2.connect(
        model="flux-general-en",  # <-- v2 English model with turn detection
        encoding="linear16",
        sample_rate="16000",
    ) as connection:

        def on_message(message: ListenV2Response) -> None:
            if isinstance(message, ListenV2TurnInfo):
                print(f"[turn {message.turn_index}] {message.transcript}")

        connection.on(EventType.MESSAGE, on_message)

        def send_audio():
            chunk_size = 4096
            for i in range(0, len(audio_data), chunk_size):
                connection.send_media(audio_data[i : i + chunk_size])
                time.sleep(0.01)
            time.sleep(2)
            connection.send_close_stream(ListenV2CloseStream(type="CloseStream"))

        sender = threading.Thread(target=send_audio, daemon=True)
        sender.start()
        connection.start_listening()


if __name__ == "__main__":
    main()
