// Recipe: Stream File (Speech-to-Text v1)
// Streams audio over WebSocket with explicit encoding parameters.
// Related recipes: streaming, transcribe-file
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
		Model:     "nova-3",
		Language:  "en-US",
		Punctuate: true,
		Encoding:  "linear16",
		Channels:  1,
		SampleRate: 8000, // <-- matches the WAV file's encoding parameters
		// Also try: SmartFormat: true, Diarize: true
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
	fmt.Println("Stream file transcription complete")
}
