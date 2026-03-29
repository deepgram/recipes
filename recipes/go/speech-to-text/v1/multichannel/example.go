// Recipe: Multichannel (Speech-to-Text v1)
// Transcribes each audio channel independently. Without multichannel: all channels
// are mixed into one transcript. With multichannel: each channel gets its own transcript.
// Related recipes: transcribe-url, diarize
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
		Multichannel: true, // <-- THIS is the feature this recipe demonstrates
		// Also try: Diarize: true, SmartFormat: true
	}

	// Response path: res.Results.Channels — one entry per audio channel
	//   channel.Alternatives[0].Transcript — transcript for that channel
	// Note: spacewalk.wav is mono, so only one channel will be returned
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	for i, channel := range res.Results.Channels {
		if len(channel.Alternatives) > 0 {
			fmt.Printf("Channel %d: %s\n", i, channel.Alternatives[0].Transcript)
		}
	}
}
