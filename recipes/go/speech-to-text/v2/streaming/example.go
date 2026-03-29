// Recipe: Live Streaming Transcription (Speech-to-Text v2)
// WebSocket streaming with the v2/listen endpoint using flux-general-en model.
// v2 streaming provides high-accuracy English-only real-time transcription.
// Related recipes: speech-to-text/v1/streaming, speech-to-text/v2/transcribe-url
package main

import (
	"bufio"
	"context"
	"fmt"
	"net/http"
	"os"
	"time"

	interfaces "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/interfaces"
	client "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/listen"
)

func main() {
	client.InitWithDefault()
	ctx := context.Background()

	options := &interfaces.LiveTranscriptionOptions{
		Model:       "nova-3",
		Language:    "en-US",
		Punctuate:   true,
		SmartFormat: true, // <-- enables smart formatting on v2 streaming results
		// Also try: Diarize: true, InterimResults: true
	}

	dgClient, err := client.NewWSUsingChanForDemo(ctx, options)
	if err != nil {
		fmt.Printf("WebSocket connection error: %v\n", err)
		os.Exit(1)
	}

	resp, err := http.Get("https://dpgr.am/spacewalk.wav")
	if err != nil {
		fmt.Printf("Audio fetch error: %v\n", err)
		os.Exit(1)
	}
	defer resp.Body.Close()

	dgClient.Connect()
	go dgClient.Stream(bufio.NewReader(resp.Body))
	time.Sleep(15 * time.Second)
	dgClient.Stop()
	fmt.Println("v2 streaming complete")
}
