"""
Recipe: Redaction (Speech-to-Text v1)
=====================================
Demonstrates the `redact` feature, which removes sensitive information
from the transcript.

Supported redaction types:
  - pci     — payment card numbers (credit/debit cards)
  - ssn     — Social Security Numbers
  - numbers — all numeric sequences

When enabled, matched content is replaced with redaction markers in the
transcript text (e.g., "[REDACTED]").
"""

from deepgram import DeepgramClient

AUDIO_URL = "https://dpgr.am/spacewalk.wav"


def main():
    client = DeepgramClient()  # reads DEEPGRAM_API_KEY from environment

    response = client.listen.v1.media.transcribe_url(
        url=AUDIO_URL,
        model="nova-3",
        smart_format=True,
        redact="pci",  # <-- THIS enables PCI redaction (credit card numbers).
    )

    if response.results and response.results.channels:
        transcript = response.results.channels[0].alternatives[0].transcript
        print(transcript)


if __name__ == "__main__":
    main()
