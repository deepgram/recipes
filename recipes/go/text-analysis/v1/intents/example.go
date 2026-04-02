// Recipe: Intent Recognition (Text Analysis v1)
// Detects speaker intents from plain text input using the Deepgram text analysis API.
// Text analysis works directly on text — no audio required.
// This is different from speech-to-text intent detection, which operates on audio.
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

const sampleText = "I'd like to return this product and get a refund. " +
	"The item arrived damaged and I'm very disappointed with the quality. " +
	"Can you also update my shipping address for future orders?"

func main() {
	client.InitWithDefault()
	c := client.NewWithDefaults()
	dg := api.New(c)

	options := &interfaces.AnalyzeOptions{
		Language: "en",
		Intents:  true, // <-- THIS is the feature this recipe demonstrates
	}

	res, err := dg.FromStream(context.Background(), strings.NewReader(sampleText), options)
	if err != nil {
		log.Fatalf("Analysis failed: %v", err)
	}

	if res.Results.Intents != nil {
		for _, seg := range res.Results.Intents.Segments {
			fmt.Printf("Text: %s\n", seg.Text)
			if seg.Intents != nil {
				for _, i := range *seg.Intents {
					fmt.Printf("  Intent: %s (confidence: %.2f)\n", i.Intent, i.ConfidenceScore)
				}
			}
		}
	} else {
		fmt.Println("No intents detected")
	}
}
