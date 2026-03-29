// Transcribe audio with smart formatting enabled
// Shows automatic formatting of numbers, dates, and currency vs raw text output
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

	// Configure transcription options with smart formatting
	options := &interfaces.PreRecordedTranscriptionOptions{
		Model:       "nova-3",
		SmartFormat: true, // <-- THIS is the feature this recipe demonstrates
	}

	// Transcribe audio from URL
	res, err := dg.FromURL(context.Background(), url, options)
	if err != nil {
		log.Fatalf("Failed to transcribe: %v", err)
	}

	// Extract and print formatted transcript
	// Response path: res.Results.Channels[0].Alternatives[0].Transcript
	// Smart formatting automatically converts spoken numbers, dates, and currency
	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		transcript := res.Results.Channels[0].Alternatives[0].Transcript
		fmt.Println("Smart Formatted Transcript:", transcript)
	} else {
		fmt.Println("No transcript available")
		os.Exit(1)
	}
}