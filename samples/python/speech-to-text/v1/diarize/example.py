"""
Recipe: Speaker Diarization (Speech-to-Text v1)

Identifies and labels individual speakers in a multi-speaker recording.
Speaker labels appear as a `speaker` field on each word in the transcript.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        diarize=True,
    )

    if response.results and response.results.channels:
        words = response.results.channels[0].alternatives[0].words
        current_speaker = None
        for word in words:
            speaker = getattr(word, "speaker", None)
            if speaker != current_speaker:
                current_speaker = speaker
                print(f"\n[Speaker {current_speaker}]", end=" ")
            print(word.word, end=" ")
        print()


if __name__ == "__main__":
    main()
