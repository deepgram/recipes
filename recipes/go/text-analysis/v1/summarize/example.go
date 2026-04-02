// Recipe: Text Summarization (Text Analysis v1)
// Generates a concise summary from plain text input using the text analysis API.
// Text analysis works directly on text — no audio required.
// The summary condenses the input into a brief overview.
// Related recipes: text-analysis/v1/topics, text-analysis/v1/sentiment
package main

import (
	"context"
	"fmt"
	"log"
	"strings"

	api "github.com/deepgram/deepgram-go-sdk/v3/pkg/api/analyze/v1"
	interfaces "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/interfaces"
	client "github.com/deepgram/deepgram-go-sdk/v3/pkg/client/analyze"
)

const sampleText = "Deepgram is a speech AI company that provides automatic speech recognition " +
	"and natural language understanding APIs. Their Nova-3 model delivers high accuracy " +
	"transcription with features like smart formatting, speaker diarization, and topic detection. " +
	"The platform supports real-time streaming and pre-recorded audio processing across " +
	"multiple languages. Deepgram also offers text-to-speech with their Aura voice models."

func main() {
	client.InitWithDefault()
	c := client.NewWithDefaults()
	dg := api.New(c)

	options := &interfaces.AnalyzeOptions{
		Language:  "en",
		Summarize: true, // <-- THIS is the feature this recipe demonstrates
	}

	res, err := dg.FromStream(context.Background(), strings.NewReader(sampleText), options)
	if err != nil {
		log.Fatalf("Analysis failed: %v", err)
	}

	if res.Results.Summary != nil {
		fmt.Printf("Summary: %s\n", res.Results.Summary.Text)
	} else {
		fmt.Println("No summary generated")
	}
}
