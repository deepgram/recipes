"""
Recipe: Utterances (Speech-to-Text v1)
=======================================
Demonstrates the `utterances` feature, which splits the transcript into
per-utterance segments — meaningful speech units separated by pauses.

Without utterances: a single transcript string with no timing segments.
With utterances:    a list of utterance objects, each with its own transcript,
                    start/end times, confidence, and optional speaker label.

Related recipes: paragraphs (groups by topic), diarize (labels speakers).
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        utterances=True,  # <-- THIS is the feature this recipe demonstrates.
                          # Splits transcript into utterance segments with timing.
        # Other useful parameters: utt_split=0.8 (seconds of silence to split on)
    )

    # Response path: response.results.utterances — list of utterance objects
    #   utterance.transcript  — text of this utterance
    #   utterance.start       — start time in seconds
    #   utterance.end         — end time in seconds
    #   utterance.confidence  — confidence score 0-1
    #   utterance.speaker     — speaker index (if diarize=True)
    #   utterance.channel     — audio channel index
    # Utterances can be empty if audio is very short or has no detectable pauses.
    if response.results and response.results.utterances:
        for utt in response.results.utterances:
            print(f"[{utt.start:.2f}s - {utt.end:.2f}s] {utt.transcript}")
    else:
        print("No utterances returned")


if __name__ == "__main__":
    main()
