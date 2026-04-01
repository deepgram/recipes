#!/usr/bin/env bash
# Recipe: Configure TTS Voice (Voice Agents v1)
#
# Demonstrates choosing a specific aura-2 voice model for the
# voice agent's speak stage. Prints the configuration payload.

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
      "instructions": "You are a friendly assistant."
    },
    "speak": { "model": "aura-2-arcas-en" }
  }
}
JSON
)

echo "$SETTINGS" | python3 -c "import sys,json; print(json.dumps(json.load(sys.stdin), indent=2))"
echo ""
echo "Voice agent configured with aura-2-arcas-en TTS voice."
