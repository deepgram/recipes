/*
 * Audio Intelligence Intent Recognition Recipe
 * 
 * This recipe demonstrates how to use Deepgram's AI intent recognition feature
 * to automatically detect user intents and purposes within audio content.
 * Intent recognition helps understand what actions or outcomes the speaker
 * is trying to achieve through their speech.
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
        .intents(true)  // <-- THIS is the feature this recipe demonstrates
        .build();
    
    // Get transcription with intent recognition
    let response = dg.transcription().prerecorded(source, &options).await?;
    
    // Print the transcript
    println!("Transcript: {}", &response.results.channels[0].alternatives[0].transcript);
    
    // Extract and print detected intents
    // Intent recognition results appear in response.results.intents
    let json = serde_json::to_value(&response)?;
    if let Some(intents) = json.pointer("/results/intents/segments") {
        println!("\nDetected Intents:");
        if let Some(intents_array) = intents.as_array() {
            for (i, intent_segment) in intents_array.iter().enumerate() {
                if let Some(intents_list) = intent_segment.pointer("/intents") {
                    println!("Segment {}: {}", i + 1, serde_json::to_string_pretty(intents_list)?);
                }
            }
        }
    } else {
        println!("\nNote: No intents detected - may require audio with clear actionable requests");
    }
    
    Ok(())
}