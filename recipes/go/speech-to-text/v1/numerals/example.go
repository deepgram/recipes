// Recipe: Numerals (Speech-to-Text v1)
// Converts spoken numbers to numeric digits in the transcript.
// Without numerals: "twenty three" stays as words. With numerals: becomes "23".
// Useful for financial, medical, or data-heavy audio content.
// Related recipes: measurements, smart-format, dictation
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
		Numerals: true, // <-- THIS is the feature this recipe demonstrates
	}

	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		fmt.Printf("Transcript (with numerals): %s\n", res.Results.Channels[0].Alternatives[0].Transcript)
	}
}
