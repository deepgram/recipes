// Recipe: Intent Recognition (Audio Intelligence v1)
// Detects caller/speaker intents from context. Applied via the pre-recorded
// transcription API with intents=true.
// Related recipes: speech-to-text/v1/intents, topics, sentiment
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
		Model:   "nova-3",
		Intents: true, // <-- THIS is the feature this recipe demonstrates
		// Also try: Topics: true, Sentiment: true, Summarize: "v2"
	}

	// Response path: res.Results.Intents.Segments
	//   segment.Text    — text of the segment
	//   segment.Intents — list of intents, each with .Intent field
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if res.Results.Intents != nil {
		for _, seg := range res.Results.Intents.Segments {
			for _, i := range seg.Intents {
				fmt.Printf("Intent: %s\n  Text: %s\n", i.Intent, seg.Text)
			}
		}
	} else {
		fmt.Println("No intents detected")
	}
}
