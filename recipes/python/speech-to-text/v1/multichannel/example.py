"""
Recipe: Multichannel Transcription (Speech-to-Text v1)
======================================================
Demonstrates the `multichannel` feature, which transcribes each audio
channel independently.

Without multichannel: all audio is mixed into a single channel[0].
With multichannel:    each channel gets its own transcript in
                      response.results.channels[i].

This is useful for stereo recordings where each speaker is on a
separate channel (e.g., call-centre audio with agent on left and
caller on right).
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        multichannel=True,  # <-- THIS transcribes each channel separately.
    )

    if response.results and response.results.channels:
        for i, channel in enumerate(response.results.channels):
            transcript = channel.alternatives[0].transcript
            print(f"Channel {i}: {transcript[:150]}")


if __name__ == "__main__":
    main()
