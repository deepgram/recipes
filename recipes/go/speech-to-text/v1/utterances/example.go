// Recipe: Utterances (Speech-to-Text v1)
// Segments transcript into utterances with speaker and timing. Without utterances:
// continuous transcript. With utterances: discrete speech segments.
// Related recipes: diarize, paragraphs
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
		Model:      "nova-3",
		Utterances: true, // <-- THIS is the feature this recipe demonstrates
		// Also try: Diarize: true, SmartFormat: true
	}

	// Response path: res.Results.Utterances — list of utterance objects
	//   utterance.Transcript — text of the utterance
	//   utterance.Speaker    — speaker index (int)
	//   utterance.Start/End  — timing in seconds
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if res.Results.Utterances != nil {
		for i, u := range res.Results.Utterances {
			fmt.Printf("[%d] Speaker %d (%.1fs-%.1fs): %s\n", i+1, u.Speaker, u.Start, u.End, u.Transcript)
		}
	}
}
