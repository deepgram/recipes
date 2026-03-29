# Function Calling (Voice Agents v1)

Configures the voice agent with function calling capabilities, enabling the LLM to invoke defined functions during conversation. This allows your agent to perform actions, retrieve data, or interact with external systems based on user requests.

## Key Parameters

- **Function call handler**: `ws.onFunctionCallRequest()` registers a callback to handle function invocations
- **Enhanced prompt**: System prompt that informs the LLM about available functions
- **Tool definitions**: Functions that the agent can call (defined in agent configuration)

## Prerequisites

- Java 11 or higher
- Maven 3.9 or higher
- `DEEPGRAM_API_KEY` environment variable set

## Run

```bash
cd recipes/java/voice-agents/v1/function-calling
mvn exec:java -Dexec.mainClass="Example"
```

## Expected Output

```
Agent connected: req_12345678-abcd-1234-abcd-123456789abc
Settings applied with function calling
```

When the user makes a request that triggers a function call, you'll also see:

```
Function call: {function_name: "get_weather", parameters: {"location": "San Francisco"}}
```

The agent is now ready to handle function calls, enabling it to perform actions beyond just conversation.