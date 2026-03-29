// Recipe: Generate Audio to File (Text-to-Speech v1)
// Converts text to audio and saves as a file using the aura-2 voice model.
// This is the simplest TTS operation: text in, audio file out.
// Related recipes: stream-audio, select-model, select-encoding
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	api "github.com/deepgram/deepgram-go-sdk/v3/pkg/api/speak/v1/rest"
	interfaces "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/interfaces"
	speak "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/speak"
)

func main() {
	speak.InitWithDefault()
	c := speak.NewRESTWithDefaults()
	dg := api.New(c)

	options := &interfaces.SpeakOptions{
		Model: "aura-2-thalia-en", // <-- THIS is the voice model for TTS
		// Also try: Model: "aura-2-arcas-en", Encoding: "mp3"
	}

	// ToSave writes TTS audio directly to a file
	// Response includes metadata: ContentType, RequestID, ModelName, Characters
	res, err := dg.ToSave(context.Background(), "output.wav", "Hello from Deepgram! This is a text to speech example using the Go SDK.", options)
	if err != nil {
		log.Fatalf("TTS failed: %v", err)
	}

	info, _ := os.Stat("output.wav")
	fmt.Printf("Audio saved: %s (%d bytes)\n", res.Filename, info.Size())
	fmt.Printf("Model: %s, Characters: %d\n", res.ModelName, res.Characters)
	os.Remove("output.wav")
}
