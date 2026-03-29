"""
Recipe: Language Detection (Speech-to-Text v1)
================================================
Demonstrates the `detect_language` feature, which automatically identifies
the dominant language spoken in the audio.

Without detect_language: you must specify `language` explicitly.
With detect_language:    Deepgram identifies the language and returns it in
                         `channel.detected_language` (BCP-47 code like "en").

Useful when processing audio of unknown language. Cannot be combined with
the `language` parameter — use one or the other.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        detect_language=True,  # <-- THIS is the feature this recipe demonstrates.
                               # Identifies the spoken language automatically.
        # Other useful parameters: language="en" (explicit, mutually exclusive)
    )

    # Response path: response.results.channels[0].detected_language — BCP-47 string
    # Also: response.results.channels[0].alternatives[0].transcript — the text
    # detected_language may be absent if detection confidence is too low.
    if response.results and response.results.channels:
        channel = response.results.channels[0]
        detected = getattr(channel, "detected_language", None)
        transcript = channel.alternatives[0].transcript
        print(f"Detected language: {detected}")
        print(f"Transcript: {transcript}")


if __name__ == "__main__":
    main()
