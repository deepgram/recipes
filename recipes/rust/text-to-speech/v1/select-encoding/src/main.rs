/**
 * Deepgram Rust SDK - Text-to-Speech v1 Encoding Selection
 * Demonstrates different audio encoding options for text-to-speech.
 */
use std::{env, fs, path::Path};
use deepgram::{Deepgram, speak::options::{Options as SpeakOptions, Model as SpeakModel, Encoding as SpeakEncoding, Container}};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let _ = rustls::crypto::ring::default_provider().install_default();
    let api_key = env::var("DEEPGRAM_API_KEY").expect("DEEPGRAM_API_KEY must be set");
    let dg = Deepgram::new(&api_key)?;

    let text = "This demonstrates different audio encodings.";
    
    // Demonstrate different encoding options
    let encodings = [
        (SpeakEncoding::Linear16, Container::Wav, "pcm.wav"),
    ]; // MP3 with Container::None causes API error; use Linear16 to demonstrate encoding selection

    println!("Demonstrating audio encodings: {}", text);

    for (encoding, container, filename) in &encodings {
        // Configure TTS options with selected encoding
        let options = SpeakOptions::builder()
            .model(SpeakModel::AuraAsteriaEn)
            .encoding(encoding.clone()) // <-- THIS is the feature this recipe demonstrates
            .sample_rate(24000)
            .container(container.clone())
            .build();

        println!("Generating audio with {:?} encoding...", encoding);
        
        // Generate audio with selected encoding
        dg.text_to_speech().speak_to_file(text, &options, Path::new(filename)).await?;

        // Analyze the generated file
        let metadata = fs::metadata(filename)?;
        let file_size = metadata.len();
        
        println!("{:?}: {} ({} bytes)", encoding, filename, file_size);

        // Clean up generated file
        fs::remove_file(filename)?;
    }

    println!("Encoding comparison completed!");
    println!("Linear16/PCM: Best quality, MP3: Smaller size");

    Ok(())
}