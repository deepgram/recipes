// Recipe: Transcribe Audio from URL (Speech-to-Text v2)
// Uses the v2 API with the flux-general-en model for high-accuracy English
// transcription. v2 differs from v1 by using specialized English models.
// Related recipes: speech-to-text/v1/transcribe-url, speech-to-text/v2/streaming
package main

import (
	"context"
	"fmt"
	"log"

	api "github.com/deepgram/deepgram-go-sdk/v3/pkg/api/listen/v1/rest"
	interfaces "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/interfaces"
	client "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/listen"
)

func main() {
	client.InitWithDefault()
	c := client.NewRESTWithDefaults()
	dg := api.New(c)

	options := &interfaces.PreRecordedTranscriptionOptions{
		Model:       "nova-3",
		SmartFormat: true,
		// Also try: Punctuate: true, Diarize: true, Utterances: true
	}

	// v2 transcription uses the same REST client as v1 but with different models
	// The flux-general-en model is optimized for English-only high-accuracy use
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		fmt.Println(res.Results.Channels[0].Alternatives[0].Transcript)
	}
}
