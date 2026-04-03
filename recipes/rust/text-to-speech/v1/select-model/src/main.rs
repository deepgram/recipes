/**
 * Deepgram Rust SDK - Text-to-Speech v1 Model Selection
 * Demonstrates choosing different voice models for text-to-speech.
 */
use std::{env, fs, path::Path};
use deepgram::{Deepgram, speak::options::{Options as SpeakOptions, Model as SpeakModel, Encoding as SpeakEncoding, Container}};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let _ = rustls::crypto::ring::default_provider().install_default();
    let api_key = env::var("DEEPGRAM_API_KEY").expect("DEEPGRAM_API_KEY must be set");
    let dg = Deepgram::new(&api_key)?;

    let text = "This is a voice model demonstration.";
    
    // Demonstrate different voice models
    let models = [
        (SpeakModel::AuraOrpheusEn, "Orpheus"),
        (SpeakModel::AuraAsteriaEn, "Asteria"),
    ];

    println!("Demonstrating voice models: {}", text);

    for (i, (model, name)) in models.iter().enumerate() {
        let output_path = format!("voice_{}.wav", i + 1);
        
        // Configure TTS options with selected model
        let options = SpeakOptions::builder()
            .model(model.clone()) // <-- THIS is the feature this recipe demonstrates
            .encoding(SpeakEncoding::Linear16)
            .sample_rate(24000)
            .container(Container::Wav)
            .build();

        println!("Generating audio with {} model...", name);
        
        // Generate audio with selected voice model
        dg.text_to_speech().speak_to_file(text, &options, Path::new(&output_path)).await?;

        // Display information about the generated audio
        let metadata = fs::metadata(&output_path)?;
        let file_size = metadata.len();
        
        println!("{}: {} ({} bytes)", name, output_path, file_size);

        // Clean up generated file
        fs::remove_file(&output_path)?;
    }

    println!("Voice model comparison completed!");
    Ok(())
}