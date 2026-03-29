// Recipe: Select Voice Model (Text-to-Speech v1)
// Choose from available aura-2 voice models. Each model has a different voice
// character (e.g., thalia, arcas, helios, luna).
// Related recipes: generate-audio, select-encoding
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
		Model: "aura-2-arcas-en", // <-- THIS is the feature: selecting a specific voice model
		// Available models include: aura-2-thalia-en, aura-2-arcas-en,
		// aura-2-helios-en, aura-2-luna-en, aura-2-stella-en, aura-2-athena-en
	}

	text := "Hello! This is the Arcas voice model from Deepgram's aura-2 family."
	res, err := dg.ToSave(context.Background(), "output.wav", text, options)
	if err != nil {
		log.Fatalf("TTS failed: %v", err)
	}

	info, _ := os.Stat("output.wav")
	fmt.Printf("Voice: %s\n", res.ModelName)
	fmt.Printf("Audio saved: %d bytes\n", info.Size())
	fmt.Printf("Characters processed: %d\n", res.Characters)
	os.Remove("output.wav")
}
