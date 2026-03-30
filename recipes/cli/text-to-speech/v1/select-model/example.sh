#!/usr/bin/env bash
# Recipe: Select Voice Model (Text-to-Speech v1)
#
# Demonstrates choosing a specific aura-2 voice model. Deepgram offers
# multiple voice personalities — swap the model parameter to change
# the voice character while keeping everything else the same.

OUTPUT_FILE="/tmp/deepgram_tts_model.mp3"

curl -s "https://api.deepgram.com/v1/speak?model=aura-2-arcas-en" \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello from Deepgram. This is the arcas voice model, one of many aura-2 voices available."}' \
  -o "$OUTPUT_FILE"

SIZE=$(wc -c < "$OUTPUT_FILE")
echo "Audio generated with aura-2-arcas-en model ($SIZE bytes)"

rm -f "$OUTPUT_FILE"
