// Recipe: Sentiment Analysis (Audio Intelligence v1)
// Segment-level positive/negative/neutral sentiment scoring. Applied via
// the pre-recorded transcription API with sentiment=true.
// Related recipes: speech-to-text/v1/sentiment, topics, intents
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
		Model:     "nova-3",
		Sentiment: true, // <-- THIS is the feature this recipe demonstrates
		// Also try: Topics: true, Intents: true, Summarize: "v2"
	}

	// Response path: res.Results.Sentiments.Segments
	//   segment.Text           — text of the segment
	//   segment.Sentiment      — "positive", "negative", or "neutral"
	//   segment.SentimentScore — confidence score (float)
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if res.Results.Sentiments != nil {
		for _, seg := range res.Results.Sentiments.Segments {
			fmt.Printf("[%s] (%.2f) %s\n", seg.Sentiment, seg.SentimentScore, seg.Text)
		}
	} else {
		fmt.Println("No sentiment data")
	}
}
