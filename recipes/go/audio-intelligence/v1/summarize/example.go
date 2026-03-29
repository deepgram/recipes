// Recipe: Audio Summarization (Audio Intelligence v1)
// Generates a concise text summary of spoken content. Applied via the pre-recorded
// transcription API with summarize="v2". Returns both summary and full transcript.
// Related recipes: speech-to-text/v1/summarize, topics, sentiment
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
		Model:     "nova-3",
		Summarize: "v2", // <-- THIS is the feature this recipe demonstrates
		// Also try: Topics: true, Sentiment: true, Intents: true
	}

	// Response path: res.Results.Summary.Short — concise summary string
	// Summary may be nil if audio is too short or content lacks summarizable material
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if res.Results.Summary != nil {
		fmt.Printf("Summary: %s\n", res.Results.Summary.Short)
	} else {
		fmt.Println("No summary generated")
	}
}
