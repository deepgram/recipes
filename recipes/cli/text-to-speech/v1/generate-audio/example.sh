#!/usr/bin/env bash
# Recipe: Generate Audio to File (TTS v1)
#
# Converts text to speech and saves the audio as an MP3 file
# using the aura-2-thalia-en voice model.

OUTPUT_FILE="/tmp/deepgram_output.mp3"

dg speak "Hello from Deepgram. This is a text to speech example." \
  -m aura-2-thalia-en \
  -o "$OUTPUT_FILE"

echo "Audio saved to $OUTPUT_FILE ($(wc -c < "$OUTPUT_FILE") bytes)"
