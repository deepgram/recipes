"""
Recipe: Speaker Diarization (Speech-to-Text v1)
================================================
Demonstrates the `diarize` feature, which assigns a numeric speaker label
(0, 1, 2, ...) to each word in the transcript.

Without diarize: words have no speaker attribution.
With diarize:    each word object has a `speaker` field (int) indicating
                 which speaker said that word.

Speaker 0 is the first speaker to be detected, Speaker 1 the second, etc.
Labels are consistent within a single request but not across requests.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        diarize=True,      # <-- THIS is the feature this recipe demonstrates.
                           # Adds a `speaker` integer field to every word object.
    )

    if response.results and response.results.channels:
        words = response.results.channels[0].alternatives[0].words
        # words is a list of word objects. With diarize=True, each word has:
        #   word.word        — the spoken word (string)
        #   word.start       — start time in seconds (float)
        #   word.end         — end time in seconds (float)
        #   word.confidence  — confidence score 0-1 (float)
        #   word.speaker     — speaker index (int), only present when diarize=True

        current_speaker = None
        for word in words:
            # getattr guards against audio with a single speaker where the
            # `speaker` field may not be set on every word object
            speaker = getattr(word, "speaker", None)
            if speaker != current_speaker:
                current_speaker = speaker
                print(f"\n[Speaker {current_speaker}]", end=" ")
            print(word.word, end=" ")
        print()


if __name__ == "__main__":
    main()
