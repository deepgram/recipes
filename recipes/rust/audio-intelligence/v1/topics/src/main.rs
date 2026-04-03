/*
 * Audio Intelligence Topic Detection Recipe
 * 
 * This recipe demonstrates how to use Deepgram's AI topic detection feature
 * to automatically identify and classify topics discussed in audio content.
 * Topics help categorize conversations and understand what subjects are 
 * being discussed throughout the recording.
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
        .topics(true)  // <-- THIS is the feature this recipe demonstrates
        .build();
    
    // Get transcription with topic detection
    let response = dg.transcription().prerecorded(source, &options).await?;
    
    // Print the transcript
    println!("Transcript: {}", &response.results.channels[0].alternatives[0].transcript);
    
    // Extract and print detected topics
    // Topic detection results appear in response.results.topics
    let json = serde_json::to_value(&response)?;
    if let Some(topics) = json.pointer("/results/topics/segments") {
        println!("\nDetected Topics:");
        if let Some(topics_array) = topics.as_array() {
            for (i, topic_segment) in topics_array.iter().enumerate() {
                if let Some(topics_list) = topic_segment.pointer("/topics") {
                    println!("Segment {}: {}", i + 1, serde_json::to_string_pretty(topics_list)?);
                }
            }
        }
    } else {
        println!("\nNote: No topics detected - may require longer audio with clear subject matter");
    }
    
    Ok(())
}