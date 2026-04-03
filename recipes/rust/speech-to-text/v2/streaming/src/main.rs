/**
 * Deepgram Rust SDK - Speech-to-Text v2/Flux Streaming
 * Demonstrates live streaming transcription using Flux v2 API.
 * Simulates real-time audio by streaming a file with proper timing delays.
 */
use std::{env, fs, time::Duration};
use deepgram::{Deepgram, common::{flux_response::{FluxResponse, TurnEvent}, options::{Model, Encoding, Options}}};
use futures::StreamExt;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let _ = rustls::crypto::ring::default_provider().install_default();
    let api_key = env::var("DEEPGRAM_API_KEY").expect("DEEPGRAM_API_KEY must be set");
    let dg = Deepgram::new(&api_key)?;

    // Download demo audio file
    let audio_url = "https://dpgr.am/spacewalk.wav";
    let response = reqwest::get(audio_url).await?;
    let audio_data = response.bytes().await?;
    let temp_path = "temp_streaming.wav";
    fs::write(temp_path, &audio_data)?;

    // Configure Flux v2 streaming options
    let options = Options::builder()
        .model(Model::FluxGeneralEn) // <-- THIS is the feature this recipe demonstrates
        .build();

    println!("Starting live streaming transcription...");

    // Start streaming with realistic timing for live audio simulation
    let mut results = dg.transcription()
        .flux_request_with_options(options)
        .encoding(Encoding::Linear16) // Audio encoding format
        .sample_rate(44100) // Sample rate in Hz - could also use 16000 or 8000
        .file(temp_path, 3174, Duration::from_millis(16)) // Chunk size and frame delay for real-time
        .await?;

    // Process streaming transcription results
    while let Some(result) = results.next().await {
        match result? {
            FluxResponse::Connected { request_id: _, sequence_id: _ } => {
                println!("Live streaming connected");
            }
            FluxResponse::TurnInfo { event, turn_index: _, transcript, .. } => {
                match event {
                    TurnEvent::StartOfTurn => println!("Turn started"),
                    TurnEvent::Update => {
                        // Real-time transcript updates appear here
                        if !transcript.is_empty() {
                            println!("Live: {}", transcript);
                        }
                    }
                    TurnEvent::EndOfTurn => println!("Turn completed"),
                    _ => {}
                }
            }
            FluxResponse::FatalError { code: _, description, .. } => {
                eprintln!("Streaming error: {:?}", description);
                break;
            }
            _ => {}
        }
    }

    // Clean up
    let _ = fs::remove_file(temp_path);
    println!("Streaming session ended");
    
    Ok(())
}