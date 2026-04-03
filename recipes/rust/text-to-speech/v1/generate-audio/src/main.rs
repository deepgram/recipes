/**
 * Deepgram Rust SDK - Text-to-Speech v1 Audio Generation
 * Demonstrates generating audio from text and saving to a file.
 * Uses Aura voice model to convert text into natural-sounding speech.
 */
use std::{env, fs, path::Path};
use deepgram::{Deepgram, speak::options::{Options as SpeakOptions, Model as SpeakModel, Encoding as SpeakEncoding, Container}};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let _ = rustls::crypto::ring::default_provider().install_default();
    let api_key = env::var("DEEPGRAM_API_KEY").expect("DEEPGRAM_API_KEY must be set");
    let dg = Deepgram::new(&api_key)?;

    let text = "Hello world! This is a text-to-speech demo using Deepgram's Rust SDK.";
    let output_path = "output.wav";

    // Configure TTS options with Aura voice model
    let options = SpeakOptions::builder()
        .model(SpeakModel::AuraAsteriaEn) // <-- THIS is the feature this recipe demonstrates
        .encoding(SpeakEncoding::Linear16) // 16-bit linear PCM encoding
        .sample_rate(16000) // Sample rate in Hz - could also use 24000, 48000
        .container(Container::Wav) // Output container format
        .build();

    println!("Generating audio from text...");
    println!("Text: \"{}\"", text);

    // Generate audio and save to file - this creates the complete audio file
    dg.text_to_speech().speak_to_file(text, &options, Path::new(output_path)).await?;

    // Check file size and confirm creation
    let metadata = fs::metadata(output_path)?;
    let file_size = metadata.len();
    
    println!("Audio generated successfully!");
    println!("Output file: {}", output_path);
    println!("File size: {} bytes", file_size);
    println!("Voice model: Aura Asteria (English)");
    println!("Format: 16kHz WAV, 16-bit PCM");

    // Clean up the generated file
    fs::remove_file(output_path)?;
    println!("Temporary file cleaned up");

    Ok(())
}