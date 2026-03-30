#!/usr/bin/env bash
# Recipe: Connect to Voice Agent (Voice Agents v1)
#
# Establishes a WebSocket connection to Deepgram's voice agent API with
# default settings. Sends a configuration message to initialise the
# agent session, then prints the welcome message and closes.

CONFIG='{
  "type": "SettingsConfiguration",
  "audio": {"input": {"encoding": "linear16", "sample_rate": 16000}, "output": {"encoding": "linear16", "sample_rate": 16000}},
  "agent": {"listen": {"model": "nova-3"}, "think": {"provider": {"type": "open_ai"}, "model": "gpt-4o-mini"}, "speak": {"model": "aura-2-thalia-en"}}
}'

echo "$CONFIG" \
  | websocat -n1 \
    "wss://agent.deepgram.com/agent" \
    --header "Authorization: Token $DEEPGRAM_API_KEY" \
  | python3 -c "
import sys, json
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        msg = json.loads(line)
        print(f'{msg[\"type\"]}: {json.dumps(msg, indent=2)[:200]}')
    except (json.JSONDecodeError, KeyError):
        pass
" | head -5

echo "Voice agent session initiated successfully"
