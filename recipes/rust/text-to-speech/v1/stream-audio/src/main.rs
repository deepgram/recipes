/**
 * Deepgram Rust SDK - Text-to-Speech v1 Audio Streaming
 * Demonstrates streaming audio response from text-to-speech API.
 * Receives audio data in chunks rather than as a complete file.
 */
use std::env;
use deepgram::{Deepgram, speak::options::{Options as SpeakOptions, Model as SpeakModel, Encoding as SpeakEncoding, Container}};
use futures::StreamExt;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let _ = rustls::crypto::ring::default_provider().install_default();
    let api_key = env::var("DEEPGRAM_API_KEY").expect("DEEPGRAM_API_KEY must be set");
    let dg = Deepgram::new(&api_key)?;

    let text = "This is a streaming text-to-speech example.";

    // Configure streaming TTS options
    let options = SpeakOptions::builder()
        .model(SpeakModel::AuraAsteriaEn)
        .encoding(SpeakEncoding::Linear16)
        .sample_rate(24000)
        .container(Container::Wav)
        .build();

    println!("Starting streaming text-to-speech...");
    println!("Text: \"{}\"", text);

    // Stream audio data instead of saving to file
    let mut audio_stream = dg.text_to_speech().speak_to_stream(text, &options).await?; // <-- THIS is the feature this recipe demonstrates

    let mut total_bytes = 0;
    let mut chunk_count = 0;

    println!("Receiving audio stream...");

    // Process streaming audio chunks as they arrive
    while let Some(chunk) = audio_stream.next().await {
        let chunk_size = chunk.len();
        total_bytes += chunk_size;
        chunk_count += 1;
        
        // In a real application, you would process these chunks
        println!("Received chunk {}: {} bytes", chunk_count, chunk_size);
    }

    println!("Streaming completed!");
    println!("Total audio data: {} bytes", total_bytes);
    println!("Total chunks: {}", chunk_count);
    
    Ok(())
}