// Recipe: Find and Replace (Speech-to-Text v1)
// Finds and replaces terms in the transcript output.
// Format: "original:replacement" — each entry replaces one term.
// Useful for correcting brand names, normalizing terminology, or censoring words.
// Related recipes: redact, profanity-filter, keywords
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
		Replace: []string{"mankind:humankind", "man:person"}, // <-- THIS is the feature this recipe demonstrates
	}

	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		fmt.Printf("Transcript (with replacements): %s\n", res.Results.Channels[0].Alternatives[0].Transcript)
	}
}
