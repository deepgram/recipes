// Recipe: Profanity Filter (Speech-to-Text v1)
// Masks profanity in the transcript output with asterisks.
// Without profanity_filter: profanity appears verbatim.
// With profanity_filter: profane words are replaced (e.g., "f***").
// Note: spacewalk.wav has no profanity, so no masking occurs on this demo audio.
// Related recipes: redact, replace, smart-format
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
		Model:           "nova-3",
		ProfanityFilter: true, // <-- THIS is the feature this recipe demonstrates
	}

	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		fmt.Printf("Transcript (profanity filtered): %s\n", res.Results.Channels[0].Alternatives[0].Transcript)
	}
}
