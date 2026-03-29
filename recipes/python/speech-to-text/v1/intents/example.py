"""
Recipe: Intent Recognition (Speech-to-Text v1)
================================================
Demonstrates the `intents` feature, which detects speaker intents
in the transcript — what the speaker is trying to accomplish.

Without intents: just the transcript text.
With intents:    response.results.intents contains per-segment intent lists,
                 each with an intent label and confidence score.

This is an Audio Intelligence feature. For custom intent detection,
add `custom_intent` and `custom_intent_mode` parameters.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        intents=True,  # <-- THIS is the feature this recipe demonstrates.
                       # Detects speaker intents in the audio.
        # Other useful parameters: custom_intent=["inform","request"],
        #   custom_intent_mode="extended" (detect custom + auto intents)
    )

    # Response path: response.results.intents.results.intents — intent analysis
    #   intents.segments        — list of segment objects
    #     segment.text          — the text segment
    #     segment.start_word    — start word index
    #     segment.end_word      — end word index
    #     segment.intents       — list of intent objects
    #       intent.intent            — intent label (str)
    #       intent.confidence_score  — confidence (float)
    # Intents can be None if audio is too short for analysis.
    if response.results and response.results.intents:
        segments = response.results.intents.results.intents.segments
        if segments:
            for seg in segments[:5]:
                intent_labels = [f"{i.intent} ({i.confidence_score:.2f})"
                                 for i in seg.intents]
                print(f"Intents: {', '.join(intent_labels)}")
                print(f"  Text: {seg.text}\n")


if __name__ == "__main__":
    main()
