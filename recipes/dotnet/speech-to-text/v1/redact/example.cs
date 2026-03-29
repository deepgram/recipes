// Recipe: Redact (Speech-to-Text v1)
// ==================================
// Demonstrates Deepgram's redaction feature which automatically
// removes or masks sensitive information from transcripts.
//
// The redaction feature identifies and replaces sensitive data
// like PCI (credit cards), SSN (social security numbers), and other
// personally identifiable information with [REDACTED] placeholders.

using Deepgram;
using Deepgram.Models.Listen.v1.REST;
using System.Collections.Generic;

Library.Initialize();

var client = ClientFactory.CreateListenRESTClient();

var response = await client.TranscribeUrl(
    new UrlSource("https://dpgr.am/spacewalk.wav"),
    new PreRecordedSchema()
    {
        Model = "nova-2",
        Redact = new List<string> { "pci", "ssn" },  // <-- THIS is the feature this recipe demonstrates
        // Available redaction types: pci, ssn, numbers, banking
    });

// The redacted transcript is available at the standard transcript location
// Sensitive information is automatically replaced with [REDACTED]
Console.WriteLine("Redacted transcript:");
Console.WriteLine(response.Results.Channels[0].Alternatives[0].Transcript);

Library.Terminate();