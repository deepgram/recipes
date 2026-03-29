// Recipe: WebSocket Streaming TTS (Text-to-Speech v1)
// Low-latency TTS via WebSocket for real-time use cases. Text is sent over
// WebSocket and audio chunks are received as binary messages.
// Related recipes: generate-audio, stream-audio
package main

import (
	"context"
	"fmt"
	"os"
	"time"

	interfaces "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/interfaces"
	speak "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/speak"
)

func main() {
	speak.InitWithDefault()
	ctx := context.Background()

	ttsOptions := &interfaces.WSSpeakOptions{
		Model:      "aura-2-thalia-en", // <-- THIS is the TTS model for WebSocket streaming
		Encoding:   "linear16",
		SampleRate: 48000,
		// Also try: Model: "aura-2-arcas-en", Encoding: "mp3"
	}

	// NewWSUsingChanForDemo provides a built-in handler that saves audio chunks
	dgClient, err := speak.NewWSUsingChanForDemo(ctx, ttsOptions)
	if err != nil {
		fmt.Printf("TTS WebSocket error: %v\n", err)
		os.Exit(1)
	}

	dgClient.Connect()
	dgClient.SpeakWithText("Hello from Deepgram! WebSocket streaming TTS example.")
	dgClient.Flush()

	time.Sleep(5 * time.Second)
	dgClient.Stop()
	fmt.Println("WebSocket TTS streaming complete")
}
