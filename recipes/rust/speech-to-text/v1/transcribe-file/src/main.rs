//! # Transcribe File - Speech-to-text from local audio file
//! This recipe demonstrates transcribing audio from a local file using Deepgram's pre-recorded API.
//! It downloads demo audio to a temporary file then transcribes it, showing how to work with 
//! local audio files rather than URLs.

use std::env;
use deepgram::Deepgram;
use deepgram::common::{
    audio_source::AudioSource,
    options::{Options, Model}
};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let _ = rustls::crypto::ring::default_provider().install_default();
    let api_key = env::var("DEEPGRAM_API_KEY")
        .expect("DEEPGRAM_API_KEY environment variable not set");

    let dg = Deepgram::new(&api_key)?;

    // Download demo audio to temporary file
    let audio_data = reqwest::get("https://dpgr.am/spacewalk.wav")
        .await?
        .bytes()
        .await?;

    // Create audio source from buffer with MIME type  // <-- THIS is the feature this recipe demonstrates
    let source = AudioSource::from_buffer_with_mime_type(audio_data, "audio/wav");

    // Configure options
    let options = Options::builder()
        .model(Model::CustomId(String::from("nova-3")))
        .build();

    // Transcribe the audio
    let response = dg.transcription().prerecorded(source, &options).await?;

    // Extract and print transcript
    // Response path: response.results.channels[0].alternatives[0].transcript
    let transcript = &response.results.channels[0].alternatives[0].transcript;
    println!("{}", transcript);

    Ok(())
}

// Other useful parameters: .language(Language::en_US), .smart_format(true), .punctuate(true)