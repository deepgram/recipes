"""
Recipe: Paragraphs (Speech-to-Text v1)

Groups transcript output into paragraph blocks based on natural pauses
and topic shifts in speech.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        paragraphs=True,
    )

    if response.results and response.results.channels:
        alt = response.results.channels[0].alternatives[0]
        if alt.paragraphs and alt.paragraphs.paragraphs:
            for i, para in enumerate(alt.paragraphs.paragraphs, 1):
                sentences = [s.text for s in para.sentences]
                print(f"[Paragraph {i}]")
                print(" ".join(sentences))
                print()
        else:
            print("No paragraphs returned")


if __name__ == "__main__":
    main()
