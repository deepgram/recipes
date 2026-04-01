#!/usr/bin/env bash
# Recipe: Select Voice Model (TTS v1)
#
# Demonstrates choosing a specific aura-2 voice model.
# Available models include aura-2-thalia-en, aura-2-arcas-en,
# aura-2-luna-en, and others.

OUTPUT_FILE="/tmp/deepgram_model_output.mp3"

dg speak "Hello, this is the Arcas voice model from Deepgram." \
  -m aura-2-arcas-en \
  -o "$OUTPUT_FILE"

echo "Generated audio with aura-2-arcas-en ($(wc -c < "$OUTPUT_FILE") bytes)"
