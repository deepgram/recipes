# Function Calling Setup

Demonstrates how to set up function calling capabilities for voice agents, allowing the AI to trigger external functions during conversations.

## What this demonstrates

Function calling enables voice agents to interact with external APIs, databases, or custom business logic during conversations. When the agent determines that a function should be called based on user input, it triggers a `FunctionCallRequestResponse` event that your application can handle to execute the function and return results.

## Key parameters

- Subscribe to `FunctionCallRequestResponse` events to handle function calls
- Configure agent greeting to mention available functions
- Function definitions are typically configured through the LLM provider settings
- `FunctionCallRequestResponse.Name` contains the function name to execute
- `FunctionCallRequestResponse.Arguments` contains the function parameters

## Example output

```
Configuring voice agent with function calling:
- Function calling events subscribed
- Agent configured to mention available functions
- Ready to handle FunctionCallRequestResponse events
Connection result: True
Connected with function calling! Welcome: Hello! I'm your AI assistant with function calling capabilities. I can help you with weather information and calculations.
Function calling setup successful!
Agent is ready to receive and handle function calls
No function calls triggered yet (would happen during conversation)
Agent session completed
```

## Function call workflow

1. User speaks a request that requires external data (e.g., "What's the weather?")
2. Agent analyzes the request and determines a function should be called
3. `FunctionCallRequestResponse` event is triggered with function name and arguments
4. Your application executes the function and can send results back to continue the conversation

## Prerequisites

- Set `DEEPGRAM_API_KEY` environment variable
- Set `OPENAI_API_KEY` for LLM provider (or configure different provider)
- Function definitions must be configured with your LLM provider

## Run the example

```bash
dotnet run
```