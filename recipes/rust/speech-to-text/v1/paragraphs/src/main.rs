//! # Paragraphs - Structured paragraph detection
//! This recipe demonstrates paragraph detection, which segments transcripts into logical
//! paragraphs with start/end times and speaker information. With paragraphs enabled, 
//! you get structured output that groups related sentences together.

use std::env;
use deepgram::Deepgram;
use deepgram::common::{
    audio_source::AudioSource,
    options::{Options, Model}
};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let _ = rustls::crypto::ring::default_provider().install_default();
    let api_key = env::var("DEEPGRAM_API_KEY")
        .expect("DEEPGRAM_API_KEY environment variable not set");

    let dg = Deepgram::new(&api_key)?;

    // Create audio source from URL
    let source = AudioSource::from_url("https://dpgr.am/spacewalk.wav");

    // Enable paragraph detection for structured output
    let options = Options::builder()
        .model(Model::CustomId(String::from("nova-3")))
        .paragraphs(true)  // <-- THIS is the feature this recipe demonstrates
        .punctuate(true)   // Punctuation recommended with paragraphs
        .build();

    // Transcribe with paragraph detection
    let response = dg.transcription().prerecorded(source, &options).await?;

    // Response path: response.results.channels[0].alternatives[0].paragraphs
    // The Paragraphs struct has private inner fields; use serde to inspect them.
    // Paragraphs may be None if content is too short for paragraph detection.
    let json = serde_json::to_value(&response)?;
    if let Some(paras) = json.pointer("/results/channels/0/alternatives/0/paragraphs/paragraphs") {
        if let Some(arr) = paras.as_array() {
            for (i, p) in arr.iter().enumerate() {
                let sentences = p.get("sentences").and_then(|s| s.as_array());
                let text: String = sentences.map(|ss| {
                    ss.iter().filter_map(|s| s.get("text").and_then(|t| t.as_str())).collect::<Vec<_>>().join(" ")
                }).unwrap_or_default();
                println!("Paragraph {}: {}", i + 1, text);
            }
        }
    } else {
        println!("{}", &response.results.channels[0].alternatives[0].transcript);
    }

    Ok(())
}

// Other useful parameters: .diarize(true), .utterances(true), .smart_format(true)