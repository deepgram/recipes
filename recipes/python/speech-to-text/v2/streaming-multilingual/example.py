"""
Recipe: Flux Multilingual Streaming (Speech-to-Text v2)
========================================================
Streams audio to the Flux Multilingual model (`flux-general-multi`) via
the v2 WebSocket API, displaying per-turn language detection alongside
the transcript. The `languages` field on each TurnInfo event reports
which languages were detected, sorted by word count.
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
        model="flux-general-multi",
        encoding="linear16",
        sample_rate="16000",
    ) as connection:

        def on_message(message: ListenV2Response) -> None:
            if isinstance(message, ListenV2TurnInfo):
                langs = getattr(message, "languages", None) or []
                lang_str = ", ".join(langs) if langs else "detecting..."
                print(f"[turn {message.turn_index}] ({lang_str}) {message.transcript}")

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
