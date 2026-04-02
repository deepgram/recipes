#!/usr/bin/env bash
# Recipe: Stream Audio Response (TTS v1)
#
# Streams TTS audio to stdout as it generates. The audio bytes
# are piped to wc to show the total size. In production you
# would pipe to an audio player like ffplay.

BYTE_COUNT=$(dg speak "Hello from Deepgram. Streaming text to speech." \
  -m aura-2-thalia-en 2>/dev/null | wc -c)

echo "Streamed $BYTE_COUNT bytes of audio to stdout"
