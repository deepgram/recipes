// Recipe: Bit Rate Control (Text-to-Speech v1)
// Controls the output audio bit rate for compressed encodings like MP3.
// Lower bit rates produce smaller files; higher bit rates improve audio quality.
// Requires a compressed encoding (mp3, opus, etc.) — not applicable to linear16.
// Related recipes: select-encoding, generate-audio, select-model
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
		Encoding: "mp3",
		BitRate:  48000, // <-- THIS is the feature: controlling output bit rate (bps)
	}

	text := "Hello from Deepgram! This audio uses a controlled bit rate for smaller file size."
	res, err := dg.ToSave(context.Background(), "output.mp3", text, options)
	if err != nil {
		log.Fatalf("TTS failed: %v", err)
	}

	info, _ := os.Stat("output.mp3")
	fmt.Printf("Bit rate: 48000 bps\n")
	fmt.Printf("Audio saved: %d bytes\n", info.Size())
	fmt.Printf("Model: %s, Characters: %d\n", res.ModelName, res.Characters)
	os.Remove("output.mp3")
}
