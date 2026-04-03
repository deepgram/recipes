// Recipe: Sentiment Analysis (Text Analysis v1)
// ================================================
// Demonstrates Deepgram's text sentiment analysis which detects sentiment
// (positive, negative, neutral) directly from plain text — no audio needed.
//
// The API segments the text and assigns sentiment scores to each segment.
//
// See also: text-analysis/v1/intents, text-analysis/v1/topics.

using Deepgram;
using Deepgram.Models.Analyze.v1;

Library.Initialize();

var client = ClientFactory.CreateAnalyzeClient();

var text = "I absolutely love this product, it works perfectly! "
    + "However, the shipping was terribly slow and frustrating. "
    + "The customer support was helpful and resolved my issue quickly.";

var response = await client.AnalyzeText(
    new TextSource(text),
    new AnalyzeSchema()
    {
        Language = "en",
        Sentiment = true,  // <-- THIS enables sentiment analysis on text
    });

Console.WriteLine(response);

Library.Terminate();
