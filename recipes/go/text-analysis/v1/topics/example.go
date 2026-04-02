// Recipe: Topic Detection (Text Analysis v1)
// Identifies topics discussed in plain text input using the text analysis API.
// Text analysis works directly on text — no audio required.
// Each segment is annotated with detected topics and confidence scores.
// Related recipes: text-analysis/v1/intents, text-analysis/v1/sentiment
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

const sampleText = "The stock market saw significant gains today as technology companies " +
	"reported strong quarterly earnings. Meanwhile, the Federal Reserve is expected to " +
	"announce its decision on interest rates next week. In sports news, the championship " +
	"finals drew record viewership numbers across streaming platforms."

func main() {
	client.InitWithDefault()
	c := client.NewWithDefaults()
	dg := api.New(c)

	options := &interfaces.AnalyzeOptions{
		Language: "en",
		Topics:   true, // <-- THIS is the feature this recipe demonstrates
	}

	res, err := dg.FromStream(context.Background(), strings.NewReader(sampleText), options)
	if err != nil {
		log.Fatalf("Analysis failed: %v", err)
	}

	if res.Results.Topics != nil {
		for _, seg := range res.Results.Topics.Segments {
			fmt.Printf("Text: %s\n", seg.Text)
			if seg.Topics != nil {
				for _, t := range *seg.Topics {
					fmt.Printf("  Topic: %s (confidence: %.2f)\n", t.Topic, t.ConfidenceScore)
				}
			}
		}
	} else {
		fmt.Println("No topics detected")
	}
}
