// Recipe: Language Detection (Speech-to-Text v1)
// Automatically detects the spoken language. Without detect_language: you must
// specify the language. With detect_language: the API identifies it for you.
// Related recipes: transcribe-url, smart-format
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
		Model:          "nova-3",
		DetectLanguage: true, // <-- THIS is the feature this recipe demonstrates
		// Also try: SmartFormat: true, Punctuate: true
	}

	// Response path: res.Results.Channels[0].DetectedLanguage — language code (e.g. "en")
	// DetectedLanguage may be empty if confidence is too low
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 {
		ch := res.Results.Channels[0]
		fmt.Printf("Detected Language: %s\n", ch.DetectedLanguage)
		if len(ch.Alternatives) > 0 {
			fmt.Printf("Transcript: %s\n", ch.Alternatives[0].Transcript)
		}
	}
}
