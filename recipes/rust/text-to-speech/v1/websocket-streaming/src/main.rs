/**
 * Deepgram Rust SDK - Text-to-Speech v1 WebSocket Streaming
 * Demonstrates streaming TTS via speak_to_stream as closest equivalent.
 */
use std::env;
use deepgram::{Deepgram, speak::options::{Options as SpeakOptions, Model as SpeakModel, Encoding as SpeakEncoding, Container}};
use futures::StreamExt;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let _ = rustls::crypto::ring::default_provider().install_default();
    let api_key = env::var("DEEPGRAM_API_KEY").expect("DEEPGRAM_API_KEY must be set");
    let dg = Deepgram::new(&api_key)?;

    let text = "WebSocket-style streaming for real-time text-to-speech.";

    // Configure options for low-latency streaming
    let options = SpeakOptions::builder()
        .model(SpeakModel::AuraAsteriaEn)
        .encoding(SpeakEncoding::Linear16)
        .sample_rate(16000)
        .container(Container::Wav)
        .build();

    println!("Starting WebSocket-style TTS streaming...");
    println!("Text: \"{}\"", text);

    // Use streaming API as closest equivalent to WebSocket streaming
    let mut audio_stream = dg.text_to_speech().speak_to_stream(text, &options).await?; // <-- THIS is the feature this recipe demonstrates

    let mut total_bytes = 0;
    let mut chunk_count = 0;
    
    println!("Simulating WebSocket-like streaming connection...");

    // Process audio chunks with WebSocket-style handling
    while let Some(chunk) = audio_stream.next().await {
        let chunk_size = chunk.len();
        total_bytes += chunk_size;
        chunk_count += 1;
        
        // WebSocket-style real-time processing
        println!("Real-time chunk {}: {} bytes", chunk_count, chunk_size);
    }

    println!("WebSocket-style streaming session completed!");
    println!("Total audio streamed: {} bytes", total_bytes);
    println!("Chunks transmitted: {}", chunk_count);
    
    Ok(())
}