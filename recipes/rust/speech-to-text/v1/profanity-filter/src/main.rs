//! Profanity Filter - Mask profanity in transcript output
//! When enabled, profane words in the transcript are replaced with
//! asterisks or symbols to produce a clean, family-friendly output.
//! Useful for content moderation, broadcast, and public-facing applications.

use std::env;
use deepgram::{Deepgram, DeepgramError};
use deepgram::common::{
    audio_source::AudioSource,
    options::{Options, Model}
};

#[tokio::main]
async fn main() -> Result<(), DeepgramError> {
    let api_key = env::var("DEEPGRAM_API_KEY")
        .expect("DEEPGRAM_API_KEY environment variable not set");

    let dg = Deepgram::new(&api_key)?;
    let source = AudioSource::from_url("https://dpgr.am/spacewalk.wav");

    let options = Options::builder()
        .model(Model::CustomId(String::from("nova-3")))
        .profanity_filter(true)  // <-- Masks profanity with symbols
        .punctuate(true)
        .build();

    let response = dg.transcription().prerecorded(source, &options).await?;

    let transcript = &response.results.channels[0].alternatives[0].transcript;
    println!("{}", transcript);

    Ok(())
}
