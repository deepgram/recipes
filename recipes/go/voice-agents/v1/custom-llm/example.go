// Recipe: Configure LLM Provider (Voice Agents v1)
// Use OpenAI or Anthropic as the think model for your agent. The think provider
// determines which LLM processes the conversation and generates responses.
// Related recipes: connect, custom-tts, function-calling
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

	// <-- THIS is the feature: configuring a custom LLM provider
	tOptions.Agent.Think.Provider["type"] = "open_ai" // or "anthropic"
	tOptions.Agent.Think.Provider["model"] = "gpt-4o-mini"
	tOptions.Agent.Think.Prompt = "You are a friendly assistant who speaks concisely."
	// Also try: type="anthropic", model="claude-3-haiku-20240307"

	tOptions.Agent.Speak.Provider["type"] = "deepgram"
	tOptions.Agent.Speak.Provider["model"] = "aura-2-thalia-en"
	tOptions.Agent.Language = "en"
	tOptions.Agent.Greeting = "Hi there! I'm using a custom LLM."

	dgClient, err := agentClient.NewWSUsingChanForDemo(ctx, tOptions)
	if err != nil {
		fmt.Printf("Agent connection error: %v\n", err)
		os.Exit(1)
	}

	if !dgClient.Connect() {
		fmt.Println("Connection failed")
		os.Exit(1)
	}
	fmt.Println("Voice agent with custom LLM connected")

	time.Sleep(3 * time.Second)
	dgClient.Stop()
	fmt.Println("Session ended")
}
