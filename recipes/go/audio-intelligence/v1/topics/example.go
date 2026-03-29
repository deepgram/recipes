// Recipe: Topic Detection (Audio Intelligence v1)
// Identifies key topics discussed in audio. Applied via the pre-recorded
// transcription API with topics=true.
// Related recipes: speech-to-text/v1/topics, intents, sentiment
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
		Model:  "nova-3",
		Topics: true, // <-- THIS is the feature this recipe demonstrates
		// Also try: Sentiment: true, Intents: true, Summarize: "v2"
	}

	// Response path: res.Results.Topics.Segments
	//   segment.Text   — text of the segment
	//   segment.Topics — list of topics, each with .Topic field
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if res.Results.Topics != nil {
		for _, seg := range res.Results.Topics.Segments {
			for _, t := range seg.Topics {
				fmt.Printf("Topic: %s\n  Text: %s\n", t.Topic, seg.Text)
			}
		}
	} else {
		fmt.Println("No topics detected")
	}
}
