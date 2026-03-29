// Recipe: Keyword Boosting (Speech-to-Text v1)
// Boosts accuracy for specific keywords or proper nouns. Without keywords:
// standard recognition. With keywords: specified terms get higher recognition priority.
// Format is "word:boost" where boost is a float (higher = more boosted).
// Related recipes: search, transcribe-url
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
		Keywords: []string{"spacewalk:2", "ISS:1.5"}, // <-- THIS is the feature this recipe demonstrates
		// Also try: Keyterm: []string{"deepgram"}, Search: []string{"spacewalk"}
	}

	// Response path: same transcript path, but boosted words have higher accuracy
	// Keywords don't add new response fields — they improve recognition quality
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		fmt.Printf("Transcript (with keyword boosting): %s\n", res.Results.Channels[0].Alternatives[0].Transcript)
	}
}
