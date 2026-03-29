# Configure TTS Voice (Voice Agents v1)

Configures your voice agent to use a specific Aura-2 voice model for speech synthesis. This allows you to customize the voice characteristics of your agent, choosing from different voice personalities and speaking styles to match your application's needs.

## Key Parameters

- **Speak provider**: `SpeakSettingsV1Provider.deepgram()` sets Deepgram as the TTS provider
- **Voice model**: `DeepgramSpeakProviderModel.AURA2ASTERIA_EN` specifies the Asteria voice
- **Agent context**: Configured with both think (LLM) and speak (TTS) settings

## Prerequisites

- Java 11 or higher
- Maven 3.9 or higher
- `DEEPGRAM_API_KEY` environment variable set

## Run

```bash
cd recipes/java/voice-agents/v1/custom-tts
mvn exec:java -Dexec.mainClass="Example"
```

## Expected Output

```
Agent connected: req_12345678-abcd-1234-abcd-123456789abc
Settings applied (Asteria voice)
```

The agent successfully connects and configures itself to use the Asteria voice model for generating speech output, providing a specific vocal personality for your voice agent.