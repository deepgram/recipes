// Recipe: Topic Detection (Text Analysis v1)
// =============================================
// Demonstrates Deepgram's text topic detection which identifies key
// topics discussed in plain text input — no audio required.
//
// The API segments the text and returns detected topics for each segment.
//
// See also: text-analysis/v1/intents, text-analysis/v1/sentiment.

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
        Topics = true,  // <-- THIS enables topic detection on text
    });

Console.WriteLine(response);

Library.Terminate();
