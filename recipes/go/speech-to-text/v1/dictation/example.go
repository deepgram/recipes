// Recipe: Dictation Mode (Speech-to-Text v1)
// Formats transcript using dictation-style spoken punctuation commands.
// Without dictation: spoken "period" or "comma" appear as words.
// With dictation: spoken punctuation commands become actual punctuation marks.
// Related recipes: smart-format, punctuate, numerals
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
		Model:    "nova-3",
		Dictation: true, // <-- THIS is the feature this recipe demonstrates
	}

	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		fmt.Printf("Transcript (dictation mode): %s\n", res.Results.Channels[0].Alternatives[0].Transcript)
	}
}
