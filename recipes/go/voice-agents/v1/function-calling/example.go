// Recipe: Function Calling (Voice Agents v1)
// Inject tool calls for the LLM to use during a conversation. Function calling
// allows the agent to execute actions like lookups, calculations, or API calls.
// FunctionCallRequestResponse events arrive when the LLM wants to invoke a tool.
// Related recipes: connect, custom-llm, custom-tts
package main

import (
	"context"
	"fmt"
	"os"
	"time"

	agentClient "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/agent"
)

func main() {
	agentClient.InitWithDefault()
	ctx := context.Background()

	tOptions := agentClient.NewSettingsConfigurationOptions()
	tOptions.Agent.Listen.Provider["type"] = "deepgram"
	tOptions.Agent.Listen.Provider["model"] = "nova-3"
	tOptions.Agent.Think.Provider["type"] = "open_ai"
	tOptions.Agent.Think.Provider["model"] = "gpt-4o-mini"
	tOptions.Agent.Think.Prompt = "You are a helpful assistant that can look up the weather."
	tOptions.Agent.Speak.Provider["type"] = "deepgram"
	tOptions.Agent.Speak.Provider["model"] = "aura-2-thalia-en"
	tOptions.Agent.Language = "en"
	tOptions.Agent.Greeting = "Hello! Ask me about the weather."

	// <-- THIS is the feature: function calling via FunctionCallRequestResponse events
	// The demo handler prints function call requests to stdout

	dgClient, err := agentClient.NewWSUsingChanForDemo(ctx, tOptions)
	if err != nil {
		fmt.Printf("Agent connection error: %v\n", err)
		os.Exit(1)
	}

	if !dgClient.Connect() {
		fmt.Println("Connection failed")
		os.Exit(1)
	}
	fmt.Println("Voice agent with function calling connected")

	time.Sleep(3 * time.Second)
	dgClient.Stop()
	fmt.Println("Session ended")
}
