// Recipe: Topic Detection (Speech-to-Text v1)
// Identifies topics discussed in the audio. Without topics: only transcript.
// With topics: response includes detected topics per segment.
// Related recipes: intents, sentiment, summarize
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
		// Also try: Intents: true, Sentiment: true, Summarize: "v2"
	}

	// Response path: res.Results.Topics.Segments — list of topic segments
	//   segment.Text   — the text of the segment
	//   segment.Topics — list of detected topics, each with .Topic field
	// Topics may be nil if audio is too short or no clear topics found
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
