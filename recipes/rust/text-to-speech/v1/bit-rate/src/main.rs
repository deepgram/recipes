//! Bit Rate Control - Set the output audio bit rate for TTS
//! Controls the bit rate of compressed audio output (e.g., MP3). Lower bit
//! rates produce smaller files at reduced quality, while higher bit rates
//! improve audio fidelity. Only applies to compressed encodings like MP3.

use std::{env, fs, path::Path};
use deepgram::{Deepgram, speak::options::{Options as SpeakOptions, Model as SpeakModel, Encoding as SpeakEncoding, Container}};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = env::var("DEEPGRAM_API_KEY").expect("DEEPGRAM_API_KEY must be set");
    let dg = Deepgram::new(&api_key)?;

    let text = "Hello world! This demonstrates bit rate control for Deepgram text-to-speech.";
    let output_path = "output.mp3";

    let options = SpeakOptions::builder()
        .model(SpeakModel::CustomId(String::from("aura-2-thalia-en")))
        .encoding(SpeakEncoding::Mp3)
        .bit_rate(48000)  // <-- Controls output bit rate (48 kbps)
        .build();

    println!("Generating MP3 audio with 48 kbps bit rate...");
    println!("Text: \"{}\"", text);

    dg.text_to_speech().speak_to_file(text, &options, Path::new(output_path)).await?;

    let metadata = fs::metadata(output_path)?;
    println!("Output file: {}", output_path);
    println!("File size: {} bytes", metadata.len());
    println!("Bit rate: 48 kbps (MP3)");

    fs::remove_file(output_path)?;
    println!("Temporary file cleaned up");

    Ok(())
}