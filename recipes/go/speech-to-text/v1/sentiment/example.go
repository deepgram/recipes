// Recipe: Sentiment Analysis (Speech-to-Text v1)
// Analyzes sentiment (positive/negative/neutral) per segment. Without sentiment:
// only transcript. With sentiment: each segment gets a sentiment label and score.
// Related recipes: topics, intents, summarize
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

	// Response path: res.Results.Sentiments.Segments — list of sentiment segments
	//   segment.Text           — the text of the segment
	//   segment.Sentiment      — "positive", "negative", or "neutral"
	//   segment.SentimentScore — float score
	// Sentiments may be nil if audio is too short
	res, err := dg.FromURL(context.Background(), "https://dpgr.am/spacewalk.wav", options)
	if err != nil {
		log.Fatalf("Transcription failed: %v", err)
	}

	if res.Results.Sentiments != nil {
		for _, seg := range res.Results.Sentiments.Segments {
			fmt.Printf("[%s] (%.2f) %s\n", seg.Sentiment, seg.SentimentScore, seg.Text)
		}
	} else {
		fmt.Println("No sentiment data available")
	}
}
