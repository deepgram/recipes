// Recipe: Filler Words (Speech-to-Text v1)
// Captures filler words ("uh", "um") in the transcript.
// Without filler_words: fillers are omitted. With filler_words: fillers appear in output.
// Useful for conversation analysis, coaching tools, and verbatim transcription.
// Related recipes: smart-format, punctuate, dictation
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
		Model:       "nova-3",
		FillerWords: true, // <-- THIS is the feature this recipe demonstrates
	}

	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		fmt.Printf("Transcript (with filler words): %s\n", res.Results.Channels[0].Alternatives[0].Transcript)
	}
}
