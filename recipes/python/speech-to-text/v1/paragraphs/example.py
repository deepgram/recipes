"""
Recipe: Paragraphs (Speech-to-Text v1)
=======================================
Demonstrates the `paragraphs` feature, which groups transcript output
into paragraph blocks based on natural pauses and topic shifts in speech.

Without paragraphs: the transcript is a single flat string.
With paragraphs:    the transcript is broken into structured blocks,
                    each containing one or more sentences with timing.

Compare the output of this recipe against speech-to-text/v1/transcribe-url
to see the structural difference paragraphs adds.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        paragraphs=True,   # <-- THIS is the feature this recipe demonstrates.
                           # Enables paragraph segmentation in the response.
                           # Works best alongside smart_format=True.
    )

    if response.results and response.results.channels:
        alt = response.results.channels[0].alternatives[0]

        # When paragraphs=True, the structured output lives at:
        # alt.paragraphs.paragraphs  — list of paragraph objects
        #   para.sentences           — list of sentence objects within each paragraph
        #     sentence.text          — the sentence text
        #     sentence.start         — start time in seconds
        #     sentence.end           — end time in seconds
        if alt.paragraphs and alt.paragraphs.paragraphs:
            for i, para in enumerate(alt.paragraphs.paragraphs, 1):
                sentences = [s.text for s in para.sentences]
                print(f"[Paragraph {i}]")
                print(" ".join(sentences))
                print()
        else:
            # paragraphs can be absent if the audio is too short or has no
            # detectable natural breaks
            print("No paragraphs returned")


if __name__ == "__main__":
    main()
