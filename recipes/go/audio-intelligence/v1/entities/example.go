// Recipe: Entity Detection (Audio Intelligence v1)
// Identifies named entities (people, organisations, locations) in audio.
// Applied via the pre-recorded transcription API with detect_entities=true.
// Related recipes: speech-to-text/v1/detect-entities, topics, intents
package main

import (
	"context"
	"encoding/json"
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
		Model:          "nova-3",
		DetectEntities: true, // <-- THIS is the feature this recipe demonstrates
		// Also try: Topics: true, Sentiment: true, Intents: true
	}

	// Response path: res.Results.Entities — entity detection results
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		fmt.Printf("Transcript: %s\n", res.Results.Channels[0].Alternatives[0].Transcript)
	}
	data, _ := json.MarshalIndent(res.Results.Entities, "", "  ")
	fmt.Printf("Entities: %s\n", string(data))
}
