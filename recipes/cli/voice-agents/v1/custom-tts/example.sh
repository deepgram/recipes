#!/usr/bin/env bash
# Recipe: Configure TTS Voice (Voice Agents v1)
#
# Demonstrates choosing a specific aura-2 voice model for the agent's
# "speak" step. Swap the model parameter to change the voice personality
# while keeping the rest of the agent configuration the same.

CONFIG='{
  "type": "SettingsConfiguration",
  "audio": {"input": {"encoding": "linear16", "sample_rate": 16000}, "output": {"encoding": "linear16", "sample_rate": 16000}},
  "agent": {
    "listen": {"model": "nova-3"},
    "think": {"provider": {"type": "open_ai"}, "model": "gpt-4o-mini"},
    "speak": {"model": "aura-2-arcas-en"}
  }
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

echo "Voice agent with custom TTS voice initiated successfully"
