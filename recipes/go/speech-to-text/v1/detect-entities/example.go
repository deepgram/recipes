// Recipe: Entity Detection (Speech-to-Text v1)
// Identifies named entities (people, places, organisations) in the transcript.
// Without detect_entities: only transcript. With detect_entities: response includes
// extracted entities with their types and confidence scores.
// Related recipes: topics, intents, sentiment
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
	// Entity structure may vary; printing JSON to show available fields
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
