#!/usr/bin/env bash
# Recipe: WebSocket Streaming TTS (Text-to-Speech v1)
#
# Uses a WebSocket connection for low-latency text-to-speech. Text is
# sent as JSON messages and audio chunks are received as binary frames.
# This approach is ideal for real-time conversational use cases.

OUTPUT_FILE="/tmp/deepgram_tts_ws.raw"

echo '{"type":"Speak","text":"Hello from Deepgram. This is a WebSocket streaming text to speech example."}
{"type":"Flush"}
{"type":"Close"}' \
  | websocat -n -B 65536 --binary \
    "wss://api.deepgram.com/v1/speak?model=aura-2-thalia-en&encoding=linear16" \
    --header "Authorization: Token $DEEPGRAM_API_KEY" \
  > "$OUTPUT_FILE"

SIZE=$(wc -c < "$OUTPUT_FILE")
echo "WebSocket TTS audio saved to $OUTPUT_FILE ($SIZE bytes)"

rm -f "$OUTPUT_FILE"
