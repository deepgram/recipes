// Recipe: Custom TTS Voice (Voice Agents v1)
// Choose a specific aura-2 voice model for agent speech output.
// Related recipes: connect, custom-llm, function-calling
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
	tOptions.Agent.Think.Prompt = "You are a helpful AI assistant."

	// <-- THIS is the feature: configuring a custom TTS voice
	tOptions.Agent.Speak.Provider["type"] = "deepgram"
	tOptions.Agent.Speak.Provider["model"] = "aura-2-arcas-en"
	// Available: aura-2-thalia-en, aura-2-arcas-en, aura-2-helios-en,
	// aura-2-luna-en, aura-2-stella-en, aura-2-athena-en

	tOptions.Agent.Language = "en"
	tOptions.Agent.Greeting = "Hello! I'm speaking with the Arcas voice."

	dgClient, err := agentClient.NewWSUsingChanForDemo(ctx, tOptions)
	if err != nil {
		fmt.Printf("Agent connection error: %v\n", err)
		os.Exit(1)
	}

	if !dgClient.Connect() {
		fmt.Println("Connection failed")
		os.Exit(1)
	}
	fmt.Println("Voice agent with custom TTS connected")

	time.Sleep(3 * time.Second)
	dgClient.Stop()
	fmt.Println("Session ended")
}
