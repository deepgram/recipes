"""
Recipe: Find and Replace (Speech-to-Text v1)
===============================================
Demonstrates the `replace` feature, which searches for specific terms
in the transcript and replaces them with alternative text.

Each replacement is specified as "original:replacement". For example,
"Deepgram:Deep Gram" replaces every occurrence of "Deepgram" with
"Deep Gram" in the final transcript.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        replace=["spacewalk:space walk", "NASA:N.A.S.A."],
            # <-- THIS defines find-and-replace pairs.
            # Format: "term_to_find:replacement_text"
            # Multiple replacements can be provided as a list.
    )

    if response.results and response.results.channels:
        transcript = response.results.channels[0].alternatives[0].transcript
        print(transcript)


if __name__ == "__main__":
    main()
