// Recipe: Intent Recognition (Speech-to-Text v1)
// Detects speaker intents in the transcript. Without intents: only transcript.
// With intents: response includes detected intents per segment.
// Related recipes: topics, sentiment, summarize
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

	// Response path: res.Results.Intents.Segments — list of intent segments
	//   segment.Text    — the text of the segment
	//   segment.Intents — list of detected intents, each with .Intent field
	// Intents may be nil if audio is too short or no clear intents found
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
