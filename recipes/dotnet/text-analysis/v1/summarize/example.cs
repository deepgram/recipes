// Recipe: Text Summarization (Text Analysis v1)
// ================================================
// Demonstrates Deepgram's text summarization which generates a concise
// summary directly from plain text input — no audio required.
//
// The API analyzes the text and returns a brief summary of its content.
//
// See also: text-analysis/v1/topics, text-analysis/v1/sentiment.

using Deepgram;
using Deepgram.Models.Analyze.v1;

Library.Initialize();

var client = ClientFactory.CreateAnalyzeClient();

var text = "Deepgram is an AI speech company that provides automatic speech recognition "
    + "and text-to-speech APIs. Their Nova-3 model offers state-of-the-art accuracy "
    + "for transcription. The company also provides audio intelligence features like "
    + "sentiment analysis, topic detection, and intent recognition. Developers can "
    + "integrate Deepgram into their applications using SDKs for Python, JavaScript, "
    + "Go, .NET, and other languages.";

var response = await client.AnalyzeText(
    new TextSource(text),
    new AnalyzeSchema()
    {
        Language = "en",
        Summarize = true,  // <-- THIS enables text summarization
    });

Console.WriteLine(response);

Library.Terminate();
