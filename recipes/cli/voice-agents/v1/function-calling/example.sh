#!/usr/bin/env bash
# Recipe: Function Calling (Voice Agents v1)
#
# Voice agents support function calling where the LLM can invoke
# tool calls during a conversation. This recipe shows the JSON
# configuration payload for injecting function definitions.

echo "Checking Deepgram API access..."
dg api "/v1/models" --jq '.stt | length | tostring + " STT models available"'

echo ""
echo "Voice Agent function calling configuration (send via WebSocket Settings message):"
echo '  "think": {'
echo '    "functions": [{'
echo '      "name": "get_weather",'
echo '      "description": "Get current weather for a location",'
echo '      "parameters": {'
echo '        "type": "object",'
echo '        "properties": {'
echo '          "location": { "type": "string", "description": "City name" }'
echo '        },'
echo '        "required": ["location"]'
echo '      }'
echo '    }]'
echo '  }'
echo ""
echo "Use a Deepgram SDK to establish a session with function calling."
