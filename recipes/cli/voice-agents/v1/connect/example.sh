#!/usr/bin/env bash
# Recipe: Connect to Voice Agent (Voice Agents v1)
#
# Establishes a WebSocket voice agent session using dg api.
# Sends the initial settings message and prints the response.
# Voice agents require a WebSocket connection; this demonstrates
# the configuration payload.

SETTINGS=$(cat << 'JSON'
{
  "type": "SettingsConfiguration",
  "audio": {
    "input": { "encoding": "linear16", "sample_rate": 16000 },
    "output": { "encoding": "linear16", "sample_rate": 16000, "container": "none" }
  },
  "agent": {
    "listen": { "model": "nova-3" },
    "think": {
      "provider": { "type": "open_ai" },
      "model": "gpt-4o-mini",
      "instructions": "You are a helpful assistant."
    },
    "speak": { "model": "aura-2-thalia-en" }
  }
}
JSON
)

echo "$SETTINGS" | python3 -c "import sys,json; print(json.dumps(json.load(sys.stdin), indent=2))"
echo ""
echo "Voice agent configuration ready."
echo "In production, send this payload over a WebSocket to wss://agent.deepgram.com/agent"
