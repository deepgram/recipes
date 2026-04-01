#!/usr/bin/env bash
# Recipe: Select Audio Encoding (TTS v1)
#
# Demonstrates choosing an output audio encoding format.
# Supported encodings: mp3, linear16, flac, mulaw, alaw, opus, aac.

OUTPUT_FILE="/tmp/deepgram_encoded.wav"

dg speak "Hello from Deepgram with linear16 encoding." \
  -m aura-2-thalia-en \
  --encoding linear16 \
  --container wav \
  -o "$OUTPUT_FILE"

echo "Generated linear16/wav audio ($(wc -c < "$OUTPUT_FILE") bytes)"
