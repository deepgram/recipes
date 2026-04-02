#!/usr/bin/env bash
# Recipe: Configure LLM Provider (Voice Agents v1)
#
# Demonstrates configuring a custom LLM provider (Anthropic)
# for the voice agent's think stage. Prints the configuration
# payload that would be sent over WebSocket.

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
      "provider": { "type": "anthropic" },
      "model": "claude-sonnet-4-20250514",
      "instructions": "You are a helpful customer service agent."
    },
    "speak": { "model": "aura-2-thalia-en" }
  }
}
JSON
)

echo "$SETTINGS" | python3 -c "import sys,json; print(json.dumps(json.load(sys.stdin), indent=2))"
echo ""
echo "Voice agent configured with Anthropic LLM provider."
