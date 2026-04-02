#!/usr/bin/env bash
# Recipe: Bit Rate Control (TTS v1)
#
# Controls the output audio bit rate for compressed encodings like MP3.
# Lower bit rates produce smaller files; higher bit rates improve quality.
# Uses dg api since the CLI does not expose --bit-rate directly.

OUTPUT_FILE="/tmp/deepgram_bitrate.mp3"

dg api -X POST \
  "/v1/speak?model=aura-2-thalia-en&encoding=mp3&bit_rate=48000" \
  -H "Content-Type: application/json" \
  --input <(printf '{"text":"Hello from Deepgram. This demonstrates bit rate control for text to speech output."}') \
  --raw > "$OUTPUT_FILE"

echo "Audio saved to $OUTPUT_FILE ($(wc -c < "$OUTPUT_FILE") bytes, 48kbps MP3)"
