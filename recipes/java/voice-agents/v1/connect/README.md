# Connect to Voice Agent (Voice Agents v1)

Establishes a WebSocket connection to a Deepgram voice agent with default settings. The agent creates a conversational AI that can understand speech input and respond with synthesized voice output, enabling natural voice-based interactions.

## Key Parameters

- **WebSocket connection**: `client.agent().v1().v1WebSocket()` creates the agent client
- **Settings configuration**: Agent context with think (LLM) and greeting settings
- **Event handlers**: Welcome, settings applied, conversation text, and error callbacks

## Prerequisites

- Java 11 or higher
- Maven 3.9 or higher
- `DEEPGRAM_API_KEY` environment variable set

## Run

```bash
cd recipes/java/voice-agents/v1/connect
mvn exec:java -Dexec.mainClass="Example"
```

## Expected Output

```
Agent connected: req_12345678-abcd-1234-abcd-123456789abc
Settings applied
[assistant] Hello! How can I help?
```

The agent establishes a WebSocket connection, applies the configuration settings, and provides a greeting message, ready to engage in voice conversations.