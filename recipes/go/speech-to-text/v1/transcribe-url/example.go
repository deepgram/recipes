// Transcribe audio from URL using nova-3 model
// Shows basic URL transcription with high-accuracy model output vs base model
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	api "github.com/deepgram/deepgram-go-sdk/v3/pkg/api/listen/v1/rest"
	interfaces "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/interfaces"
	client "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/listen"
)

func main() {
	// Initialize Deepgram client with API key from environment
	client.InitWithDefault()
	c := client.NewRESTWithDefaults()
	dg := api.New(c)

	// Audio URL to transcribe
	url := "https://dpgr.am/spacewalk.wav"

	// Configure transcription options
	options := &interfaces.PreRecordedTranscriptionOptions{
		Model: "nova-3", // <-- THIS is the feature this recipe demonstrates
	}

	// Transcribe audio from URL
	res, err := dg.FromURL(context.Background(), url, options)
	if err != nil {
		log.Fatalf("Failed to transcribe: %v", err)
	}

	// Extract and print transcript from response
	// Response path: res.Results.Channels[0].Alternatives[0].Transcript
	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		transcript := res.Results.Channels[0].Alternatives[0].Transcript
		fmt.Println("Transcript:", transcript)
	} else {
		fmt.Println("No transcript available")
		os.Exit(1)
	}
}