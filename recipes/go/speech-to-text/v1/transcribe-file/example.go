// Recipe: Transcribe Local File (Speech-to-Text v1)
// Downloads demo audio, then transcribes from the local file via dg.FromFile.
// Related recipes: transcribe-url, smart-format, diarize
package main

import (
	"context"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"

	api "github.com/deepgram/deepgram-go-sdk/v3/pkg/api/listen/v1/rest"
	interfaces "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/interfaces"
	client "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/listen"
)

func main() {
	client.InitWithDefault()
	c := client.NewRESTWithDefaults()
	dg := api.New(c)

	tmpFile, err := os.CreateTemp("", "spacewalk*.wav")
	if err != nil {
		log.Fatalf("Temp file error: %v", err)
	}
	defer os.Remove(tmpFile.Name())

	resp, err := http.Get("https://dpgr.am/spacewalk.wav")
	if err != nil {
		log.Fatalf("Failed to download audio: %v", err)
	}
	defer resp.Body.Close()
	io.Copy(tmpFile, resp.Body)

	options := &interfaces.PreRecordedTranscriptionOptions{
		Model:       "nova-3",
		SmartFormat: true,
	}

	res, err := dg.FromFile(context.Background(), tmpFile.Name(), options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if len(res.Results.Channels) > 0 && len(res.Results.Channels[0].Alternatives) > 0 {
		fmt.Println(res.Results.Channels[0].Alternatives[0].Transcript)
	}
}
