"""STT v2 streaming with interim result assembly and final transcript reconstruction."""

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
    client = DeepgramClient()
    audio_data = urllib.request.urlopen(AUDIO_URL).read()
    final_turns: dict[int, str] = {}

    with client.listen.v2.connect(
        model="flux-general-en",
        encoding="linear16",
        sample_rate="16000",
    ) as connection:

        def on_message(message: ListenV2Response) -> None:
            if not isinstance(message, ListenV2TurnInfo):
                return
            idx = message.turn_index
            if message.event in ("Update", "StartOfTurn", "EagerEndOfTurn", "TurnResumed"):
                print(f"[interim turn {idx}] {message.transcript}")
            elif message.event == "EndOfTurn":
                final_turns[idx] = message.transcript
                print(f"[final  turn {idx}] {message.transcript}")

        connection.on(EventType.MESSAGE, on_message)

        def send_audio():
            for i in range(0, len(audio_data), 4096):
                connection.send_media(audio_data[i : i + 4096])
                time.sleep(0.01)
            time.sleep(2)
            connection.send_close_stream(ListenV2CloseStream(type="CloseStream"))

        sender = threading.Thread(target=send_audio, daemon=True)
        sender.start()
        connection.start_listening()

    transcript = " ".join(final_turns[k] for k in sorted(final_turns))
    print(f"\n--- Assembled transcript ---\n{transcript}")


if __name__ == "__main__":
    main()
