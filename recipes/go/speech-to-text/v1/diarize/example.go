// Recipe: Speaker Diarization (Speech-to-Text v1)
// Assigns a speaker label (0, 1, 2, ...) to each word. Without diarize: words
// have no speaker. With diarize: each word.Speaker indicates who said it.
// Related recipes: utterances, multichannel
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
		Diarize: true, // <-- THIS is the feature this recipe demonstrates
		// Also try: Utterances: true, SmartFormat: true
	}

	// Response: res.Results.Channels[0].Alternatives[0].Words — each has .Word, .Speaker
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		words := res.Results.Channels[0].Alternatives[0].Words
		currentSpeaker := -1
		for _, w := range words {
			if w.Speaker != currentSpeaker {
				if currentSpeaker != -1 {
					fmt.Println()
				}
				fmt.Printf("[Speaker %d] ", w.Speaker)
				currentSpeaker = w.Speaker
			}
			fmt.Printf("%s ", w.Word)
		}
		fmt.Println()
	}
}
