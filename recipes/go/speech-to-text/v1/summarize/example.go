// Recipe: Summarize (Speech-to-Text v1)
// Generates a concise text summary of the transcribed audio content.
// Without summarize: only raw transcript. With summarize: response includes
// a short summary of the entire audio. This is an Audio Intelligence feature.
// Related recipes: topics, intents, sentiment
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
		Summarize: "v2", // <-- THIS is the feature this recipe demonstrates (string, not bool)
		// Also try: Topics: true, Sentiment: true, Intents: true
	}

	// Response path: res.Results.Summary.Short — the summary string
	// Summary may be nil if the audio is too short to summarize
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if res.Results.Summary != nil {
		fmt.Printf("Summary: %s\n", res.Results.Summary.Short)
	} else {
		fmt.Println("No summary generated (audio may be too short)")
	}
	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		fmt.Printf("Transcript: %s\n", res.Results.Channels[0].Alternatives[0].Transcript)
	}
}
