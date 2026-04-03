/*
 * Audio Intelligence Sentiment Analysis Recipe
 * 
 * This recipe demonstrates how to use Deepgram's AI sentiment analysis feature
 * to detect emotional tone and sentiment in audio content. Sentiment is analyzed
 * at the segment level, providing insights into positive, negative, or neutral 
 * emotions throughout the conversation.
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
        .sentiment(true)  // <-- THIS is the feature this recipe demonstrates
        .paragraphs(true)  // Enable paragraphs for better sentiment segmentation
        .build();
    
    // Get transcription with sentiment analysis
    let response = dg.transcription().prerecorded(source, &options).await?;
    
    // Print the transcript
    println!("Transcript: {}", &response.results.channels[0].alternatives[0].transcript);
    
    // Extract and print sentiment analysis results  
    // Sentiment results appear per-segment in response.results.channels[].alternatives[].paragraphs
    let json = serde_json::to_value(&response)?;
    if let Some(channels) = json.pointer("/results/channels") {
        if let Some(paragraphs) = channels.get(0).and_then(|c| c.pointer("/alternatives/0/paragraphs/paragraphs")) {
            println!("\nSentiment Analysis:");
            if let Some(paragraphs_array) = paragraphs.as_array() {
                for (i, paragraph) in paragraphs_array.iter().enumerate() {
                    if let Some(sentiment) = paragraph.pointer("/sentiment") {
                        println!("Paragraph {}: {}", i + 1, serde_json::to_string_pretty(sentiment)?);
                    }
                }
            }
        }
    }
    
    Ok(())
}