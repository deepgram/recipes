// Recipe: Paragraphs (Speech-to-Text v1)
// Segments transcript into paragraphs. Requires punctuate=true.
// Without paragraphs: single block. With paragraphs: structured paragraph objects.
// Related recipes: utterances, diarize, punctuate
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
		Punctuate:  true,
		Paragraphs: true, // <-- THIS is the feature this recipe demonstrates
	}

	// Response path: res.Results.Channels[0].Alternatives[0].Paragraphs.Paragraphs
	//   paragraph.Sentences — list of sentences, each with .Text field
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		paras := res.Results.Channels[0].Alternatives[0].Paragraphs
		if paras != nil {
			for i, p := range paras.Paragraphs {
				fmt.Printf("Paragraph %d: ", i+1)
				for _, s := range p.Sentences {
					fmt.Print(s.Text + " ")
				}
				fmt.Println()
			}
		}
	}
}
