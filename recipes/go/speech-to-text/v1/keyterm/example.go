// Recipe: Key Term Prompting (Speech-to-Text v1)
// Boosts recognition of specific key terms with Nova-3.
// Without keyterm: standard recognition. With keyterm: specified terms get
// higher recognition priority without needing a boost weight.
// Different from keywords: keyterm uses Nova-3's native prompting, no weight needed.
// Related recipes: keywords, search, transcribe-url
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
		Keyterm: []string{"spacewalk", "NASA", "ISS"}, // <-- THIS is the feature this recipe demonstrates
	}

	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		fmt.Printf("Transcript (with key terms): %s\n", res.Results.Channels[0].Alternatives[0].Transcript)
	}
}
