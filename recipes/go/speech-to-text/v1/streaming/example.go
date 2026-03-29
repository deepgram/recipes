// Recipe: Live Streaming (Speech-to-Text v1)
// Real-time WebSocket transcription from HTTP audio stream.
// Related recipes: streaming-file, transcribe-url
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
		SmartFormat: true, // <-- enables smart formatting on streaming results
		// Also try: Diarize: true, InterimResults: true
	}

	// NewWSUsingChanForDemo prints transcripts to stdout automatically
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
	fmt.Println("Streaming complete")
}
