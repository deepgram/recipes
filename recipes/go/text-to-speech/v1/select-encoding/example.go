// Recipe: Select Audio Encoding (Text-to-Speech v1)
// Choose output audio encoding format: linear16, mp3, opus, flac, aac, mulaw.
// Different encodings suit different use cases (streaming, storage, telephony).
// Related recipes: generate-audio, select-model
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
		Model:    "aura-2-thalia-en",
		Encoding: "mp3", // <-- THIS is the feature: selecting output encoding
		// Available: linear16, mp3, opus, flac, aac, mulaw
		// Also try: Container: "none" for raw audio without headers
	}

	text := "Hello! This audio is encoded as MP3."
	res, err := dg.ToSave(context.Background(), "output.mp3", text, options)
	if err != nil {
		log.Fatalf("TTS failed: %v", err)
	}

	info, _ := os.Stat("output.mp3")
	fmt.Printf("Encoding: %s\n", res.ContextType)
	fmt.Printf("Audio saved: %d bytes\n", info.Size())
	fmt.Printf("Characters processed: %d\n", res.Characters)
	os.Remove("output.mp3")
}
