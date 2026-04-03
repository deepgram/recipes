/*
 * Deepgram Rust SDK: File Streaming Transcription
 * 
 * This recipe demonstrates streaming transcription of a local audio file
 * over WebSocket. Unlike prerecorded batch processing, file streaming
 * simulates real-time processing by sending file chunks progressively,
 * useful for large files or when you want real-time feedback.
 */

use std::{env, time::Duration};
use futures::stream::StreamExt;
use deepgram::{Deepgram, common::options::{Encoding, Language, Options}};

static CHUNK_SIZE: usize = 3174;
static FRAME_DELAY: Duration = Duration::from_millis(16);

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let _ = rustls::crypto::ring::default_provider().install_default();
    let api_key = env::var("DEEPGRAM_API_KEY")?;
    let dg = Deepgram::new(&api_key)?;

    // Download audio file first
    let audio = reqwest::get("https://dpgr.am/spacewalk.wav").await?.bytes().await?;
    let temp_path = "/tmp/dg_file_stream.wav";
    tokio::fs::write(temp_path, &audio).await?;
    println!("Downloaded audio file to {}", temp_path);

    // Configure options for file streaming
    let options = Options::builder()
        .smart_format(true)         // Optional: improve formatting
        .language(Language::en_US)  // <-- THIS demonstrates language specification for file streaming
        .build();

    println!("Starting file streaming transcription...");
    let mut results = dg.transcription()
        .stream_request_with_options(options)
        .encoding(Encoding::Linear16)
        .sample_rate(16000)
        .channels(1)
        .interim_results(true)      // <-- THIS enables progressive transcription results
        .file(temp_path, CHUNK_SIZE, FRAME_DELAY)
        .await?;

    while let Some(result) = results.next().await {
        println!("{result:?}");
    }

    // Cleanup
    tokio::fs::remove_file(temp_path).await.ok();
    println!("File streaming completed");
    Ok(())
}