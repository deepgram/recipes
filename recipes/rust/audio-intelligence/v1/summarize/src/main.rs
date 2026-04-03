/*
 * Audio Intelligence Summarization Recipe
 * 
 * This recipe demonstrates how to use Deepgram's AI summarization feature 
 * to get an automatic summary of audio content. The summary provides a 
 * concise overview of the main topics and key points discussed.
 */

use std::env;
use deepgram::Deepgram;
use deepgram::common::{audio_source::AudioSource, options::{Options, Model}};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let _ = rustls::crypto::ring::default_provider().install_default();
    let api_key = env::var("DEEPGRAM_API_KEY")?;
    let dg = Deepgram::new(&api_key)?;
    
    // Use demo spacewalk audio
    let source = AudioSource::from_url("https://dpgr.am/spacewalk.wav");
    
    let options = Options::builder()
        .model(Model::CustomId(String::from("nova-3")))
        .summarize(true)  // <-- THIS is the feature this recipe demonstrates
        .build();
    
    // Get transcription with summarization
    let response = dg.transcription().prerecorded(source, &options).await?;
    
    // Print the transcript
    println!("Transcript: {}", &response.results.channels[0].alternatives[0].transcript);
    
    // Extract and print the AI-generated summary
    // Summarization results appear in response.results.summary
    let json = serde_json::to_value(&response)?;
    if let Some(summary) = json.pointer("/results/summary") {
        println!("\nAI Summary:");
        println!("{}", serde_json::to_string_pretty(summary)?);
    } else {
        println!("\nNote: Summary may not be available for short audio files");
    }
    
    Ok(())
}