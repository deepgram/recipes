// Recipe: Stream Audio Response (Text-to-Speech v1)
// Streams TTS audio as it generates via REST, collecting chunks into a buffer.
// Without streaming: wait for entire audio. With streaming: process chunks as they arrive.
// Related recipes: generate-audio, websocket-streaming
package main

import (
	"context"
	"fmt"
	"log"

	api "github.com/deepgram/deepgram-go-sdk/v3/pkg/api/speak/v1/rest"
	interfaces "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/interfaces"
	speak "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/speak"
)

func main() {
	speak.InitWithDefault()
	c := speak.NewRESTWithDefaults()
	dg := api.New(c)

	options := &interfaces.SpeakOptions{
		Model:    "aura-2-thalia-en",
		Encoding: "linear16", // <-- THIS selects the streaming-friendly encoding
		// Also try: Encoding: "mp3", Encoding: "opus"
	}

	// ToStream writes TTS audio to a RawResponse buffer
	var buf interfaces.RawResponse
	res, err := dg.ToStream(context.Background(), "Hello from Deepgram! Streaming audio response example.", options, &buf)
	if err != nil {
		log.Fatalf("TTS stream failed: %v", err)
	}

	fmt.Printf("Streamed audio: %d bytes\n", len(buf))
	fmt.Printf("Content-Type: %s\n", res.ContextType)
	fmt.Printf("Model: %s, Characters: %d\n", res.ModelName, res.Characters)
}
