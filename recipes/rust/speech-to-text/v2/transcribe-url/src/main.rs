/**
 * Deepgram Rust SDK - Speech-to-Text v2/Flux URL Transcription
 * Demonstrates Flux real-time streaming transcription from a remote URL.
 * Downloads audio file first, then streams it through Flux API for live transcription.
 */
use std::{env, fs, time::Duration};
use deepgram::{Deepgram, common::{flux_response::{FluxResponse, TurnEvent}, options::{Model, Encoding, Options}}};
use futures::StreamExt;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let _ = rustls::crypto::ring::default_provider().install_default();
    let api_key = env::var("DEEPGRAM_API_KEY").expect("DEEPGRAM_API_KEY must be set");
    let dg = Deepgram::new(&api_key)?;

    // Download the audio file to a temporary location
    let audio_url = "https://dpgr.am/spacewalk.wav";
    let response = reqwest::get(audio_url).await?;
    let audio_data = response.bytes().await?;
    let temp_path = "temp_audio.wav";
    fs::write(temp_path, &audio_data)?;

    // Set up Flux v2 options with the Model::FluxGeneralEn model
    let options = Options::builder()
        .model(Model::FluxGeneralEn) // <-- THIS is the feature this recipe demonstrates
        .build();

    // Stream the downloaded file through Flux API
    let mut results = dg.transcription()
        .flux_request_with_options(options)
        .encoding(Encoding::Linear16)
        .sample_rate(44100)
        .file(temp_path, 3174, Duration::from_millis(16))
        .await?;

    println!("Starting Flux transcription...");
    
    // Process streaming results - transcripts appear in TurnEvent::Update responses
    while let Some(result) = results.next().await {
        match result? {
            FluxResponse::Connected { request_id: _, sequence_id: _ } => println!("Connected to Flux API"),
            FluxResponse::TurnInfo { event, turn_index: _, transcript, .. } => {
                match event {
                    TurnEvent::EndOfTurn => println!("Transcript: {}", transcript),
                    TurnEvent::Update => {
                        if !transcript.is_empty() {
                            println!("Transcript: {}", transcript);
                        }
                    },
                    _ => {}
                }
            }
            FluxResponse::FatalError { code: _, description, .. } => eprintln!("Fatal error: {:?}", description),
            _ => {} // Handle other response types
        }
    }

    // Clean up temporary file
    let _ = fs::remove_file(temp_path);
    
    Ok(())
}