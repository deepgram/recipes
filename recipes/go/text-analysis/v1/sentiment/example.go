// Recipe: Sentiment Analysis (Text Analysis v1)
// Analyzes sentiment (positive/negative/neutral) on plain text input.
// Text analysis works directly on text — no audio required.
// Each segment gets a sentiment label and confidence score.
// Related recipes: text-analysis/v1/intents, text-analysis/v1/topics
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

const sampleText = "I absolutely love this product! It exceeded all my expectations. " +
	"However, the shipping was terribly slow and the packaging was damaged. " +
	"Overall, the customer service team was helpful and resolved my concerns."

func main() {
	client.InitWithDefault()
	c := client.NewWithDefaults()
	dg := api.New(c)

	options := &interfaces.AnalyzeOptions{
		Language:  "en",
		Sentiment: true, // <-- THIS is the feature this recipe demonstrates
	}

	res, err := dg.FromStream(context.Background(), strings.NewReader(sampleText), options)
	if err != nil {
		log.Fatalf("Analysis failed: %v", err)
	}

	if res.Results.Sentiments != nil {
		fmt.Printf("Average: %s (%.2f)\n", res.Results.Sentiments.Average.Sentiment, res.Results.Sentiments.Average.SentimentScore)
		for _, seg := range res.Results.Sentiments.Segments {
			if seg.Sentiment != nil && seg.SentimentScore != nil {
				fmt.Printf("[%s] (%.2f) %s\n", *seg.Sentiment, *seg.SentimentScore, seg.Text)
			}
		}
	} else {
		fmt.Println("No sentiment data available")
	}
}
