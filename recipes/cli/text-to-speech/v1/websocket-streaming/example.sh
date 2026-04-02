#!/usr/bin/env bash
# Recipe: WebSocket Streaming TTS (TTS v1)
#
# Low-latency TTS via the REST streaming endpoint. This example
# pipes text to dg speak via stdin and saves the output. For true
# WebSocket TTS, the API would be called directly; this demonstrates
# the CLI streaming pattern.

OUTPUT_FILE="/tmp/deepgram_ws_output.mp3"

echo "Hello from Deepgram. This text is piped from stdin for speech synthesis." \
  | dg speak -m aura-2-thalia-en -o "$OUTPUT_FILE"

echo "Audio saved to $OUTPUT_FILE ($(wc -c < "$OUTPUT_FILE") bytes)"
