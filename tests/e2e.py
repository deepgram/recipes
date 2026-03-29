"""
E2E test — required check on every PR before auto-merge.

Verifies:
  1. DEEPGRAM_API_KEY is valid and accepted
  2. The STT pre-recorded API returns a non-empty transcript
  3. The TTS API returns audio bytes

This is intentionally minimal — one call per product, fast, no exotic options.
It is NOT a recipe test. Recipe tests live in recipes/{language}/.
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"
TTS_TEXT  = "Deepgram end-to-end test."


def test_stt_prerecorded():
    """STT: transcribe a known audio URL, assert non-empty transcript."""
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
    )

    assert response.results and response.results.channels, \
        "No channels in STT response"
    transcript = response.results.channels[0].alternatives[0].transcript
    assert transcript.strip(), \
        "STT returned an empty transcript"

    print(f"STT ✓  {len(transcript)} chars")


def test_tts():
    """TTS: synthesise a short phrase, assert audio bytes received."""
    client = DeepgramClient()

    chunks = list(client.speak.v1.audio.generate(
        text=TTS_TEXT,
        model="aura-2-thalia-en",
    ))

    audio = b"".join(chunks)
    assert len(audio) > 1000, \
        f"TTS returned suspiciously small audio ({len(audio)} bytes)"

    print(f"TTS ✓  {len(audio)} bytes")
