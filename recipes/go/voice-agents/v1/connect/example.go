// Recipe: Connect to Voice Agent (Voice Agents v1)
// Establishes a WebSocket voice agent session with default settings.
// The agent uses listen-think-speak pipeline: listen (STT) → think (LLM) → speak (TTS).
// Related recipes: custom-llm, custom-tts, function-calling
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

	// Configure agent with listen-think-speak pipeline
	tOptions := agentClient.NewSettingsConfigurationOptions()
	tOptions.Agent.Listen.Provider["type"] = "deepgram"
	tOptions.Agent.Listen.Provider["model"] = "nova-3"
	tOptions.Agent.Think.Provider["type"] = "open_ai"
	tOptions.Agent.Think.Provider["model"] = "gpt-4o-mini"
	tOptions.Agent.Think.Prompt = "You are a helpful AI assistant."
	tOptions.Agent.Speak.Provider["type"] = "deepgram"
	tOptions.Agent.Speak.Provider["model"] = "aura-2-thalia-en"
	tOptions.Agent.Language = "en"
	tOptions.Agent.Greeting = "Hello! How can I help you today?"

	// NewWSUsingChanForDemo creates connection with built-in handler that prints events
	dgClient, err := agentClient.NewWSUsingChanForDemo(ctx, tOptions)
	if err != nil {
		fmt.Printf("Agent connection error: %v\n", err)
		os.Exit(1)
	}

	if !dgClient.Connect() {
		fmt.Println("Connection failed")
		os.Exit(1)
	}
	fmt.Println("Voice agent connected successfully")

	time.Sleep(3 * time.Second)
	dgClient.Stop()
	fmt.Println("Voice agent session ended")
}
