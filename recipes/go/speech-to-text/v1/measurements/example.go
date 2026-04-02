// Recipe: Measurements (Speech-to-Text v1)
// Converts spoken measurements to standard abbreviations in the transcript.
// Without measurements: "five kilograms" stays as words. With measurements:
// becomes "5 kg". Works for weight, length, temperature, and other units.
// Related recipes: numerals, smart-format, dictation
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
		Model:        "nova-3",
		Measurements: true, // <-- THIS is the feature this recipe demonstrates
	}

	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		fmt.Printf("Transcript (with measurements): %s\n", res.Results.Channels[0].Alternatives[0].Transcript)
	}
}
