// Recipe: Search (Speech-to-Text v1)
// Finds specific words or phrases in audio with confidence scores and timestamps.
// Without search: only transcript. With search: response includes hit locations
// for each search term with timing and confidence.
// Related recipes: keywords, transcribe-url
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
		Search: []string{"space", "NASA"}, // <-- THIS is the feature this recipe demonstrates
		// Also try: Keywords: []string{"spacewalk:2"}
	}

	// Response path: res.Results.Channels[0].Search — list of search result groups
	//   group.Query — the search term
	//   group.Hits  — list of hits, each with .Start, .End, .Confidence, .Snippet
	// Search may return empty hits if terms not found in audio
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 {
		for _, group := range res.Results.Channels[0].Search {
			fmt.Printf("Term: %s (%d hits)\n", group.Query, len(group.Hits))
			for _, hit := range group.Hits {
				fmt.Printf("  %.2fs-%.2fs confidence=%.3f\n", hit.Start, hit.End, hit.Confidence)
			}
		}
	}
}
