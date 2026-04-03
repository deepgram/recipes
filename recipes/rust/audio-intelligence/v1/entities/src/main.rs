/*
 * Audio Intelligence Entity Detection Recipe
 * 
 * This recipe demonstrates how to use Deepgram's AI entity detection feature
 * to automatically identify and extract named entities from audio content.
 * Entity detection helps identify people, places, organizations, dates,
 * and other important information mentioned in speech.
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
        .detect_entities(true)  // <-- THIS is the feature this recipe demonstrates
        .build();
    
    // Get transcription with entity detection
    let response = dg.transcription().prerecorded(source, &options).await?;
    
    // Print the transcript
    println!("Transcript: {}", &response.results.channels[0].alternatives[0].transcript);
    
    // Extract and print detected entities
    // Entity detection results appear in response.results.entities
    let json = serde_json::to_value(&response)?;
    if let Some(entities) = json.pointer("/results/entities/detected_entities") {
        println!("\nDetected Entities:");
        if let Some(entities_array) = entities.as_array() {
            for entity in entities_array {
                println!("{}", serde_json::to_string_pretty(entity)?);
            }
        }
    } else {
        println!("\nNote: No entities detected - may require audio with clear proper nouns or identifiable entities");
    }
    
    Ok(())
}