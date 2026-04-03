// Recipe: Key Term Prompting (Speech-to-Text v1)
// ================================================
// Demonstrates Deepgram's keyterm prompting feature which boosts
// recognition of specific key terms or phrases with Nova-3.
//
// Keyterm prompting improves Keyword Recall Rate (KRR) by up to 90%
// for domain-specific vocabulary, proper nouns, and technical terms.
//
// See also: keywords (boost with multipliers), smart-format (formatting).

using Deepgram;
using Deepgram.Models.Listen.v1.REST;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-3",
        Keyterm = new List<string> { "spacewalk", "ISS", "EVA" },  // <-- THIS prompts the model for key terms
    });

Console.WriteLine(response.Results.Channels[0].Alternatives[0].Transcript);

Library.Terminate();
