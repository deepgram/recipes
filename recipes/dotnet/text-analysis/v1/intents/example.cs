// Recipe: Intent Recognition (Text Analysis v1)
// ================================================
// Demonstrates Deepgram's text analysis intent recognition which detects
// speaker intents directly from plain text input — no audio required.
//
// The API returns text segments with detected intents for each segment.
//
// See also: text-analysis/v1/sentiment, text-analysis/v1/topics.

using Deepgram;
using Deepgram.Models.Analyze.v1;

Library.Initialize();

var client = ClientFactory.CreateAnalyzeClient();

var text = "I'd like to return this product and get a refund. "
    + "Can you also help me track my other order? "
    + "I want to speak with a manager about my experience.";

var response = await client.AnalyzeText(
    new TextSource(text),
    new AnalyzeSchema()
    {
        Language = "en",
        Intents = true,  // <-- THIS enables intent detection on text
    });

Console.WriteLine(response);

Library.Terminate();
