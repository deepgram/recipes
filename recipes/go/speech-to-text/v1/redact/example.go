// Recipe: Redaction (Speech-to-Text v1)
// Redacts sensitive information (PCI, PII, SSNs) from the transcript.
// Without redact: full transcript. With redact: sensitive patterns replaced.
// Note: spacewalk.wav has no PCI/SSN data, so no redaction occurs on this demo audio.
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
		Model:  "nova-3",
		Redact: []string{"pci", "ssn"}, // <-- THIS is the feature this recipe demonstrates
		// Also try: Redact: []string{"numbers", "true"} for broader redaction
	}

	// Response path: same as normal transcript, but sensitive data replaced
	// In audio with credit card numbers or SSNs, those would appear as redacted
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		fmt.Printf("Redacted Transcript: %s\n", res.Results.Channels[0].Alternatives[0].Transcript)
	}
}
