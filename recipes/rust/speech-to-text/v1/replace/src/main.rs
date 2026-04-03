//! Find and Replace - Substitute terms in the transcript output
//! The replace feature finds specific words or phrases in the transcript
//! and replaces them with alternatives. This is useful for correcting
//! brand names, standardizing terminology, or removing unwanted words.

use std::env;
use deepgram::{Deepgram, DeepgramError};
use deepgram::common::{
    audio_source::AudioSource,
    options::{Options, Model, Replace}
};

#[tokio::main]
async fn main() -> Result<(), DeepgramError> {
    let api_key = env::var("DEEPGRAM_API_KEY")
        .expect("DEEPGRAM_API_KEY environment variable not set");

    let dg = Deepgram::new(&api_key)?;
    let source = AudioSource::from_url("https://dpgr.am/spacewalk.wav");

    let options = Options::builder()
        .model(Model::CustomId(String::from("nova-3")))
        .replace([
            Replace { find: "NASA".to_string(), replace: Some("Space Agency".to_string()) },
            Replace { find: "mankind".to_string(), replace: Some("humankind".to_string()) },
        ])
        .punctuate(true)
        .build();

    let response = dg.transcription().prerecorded(source, &options).await?;

    let transcript = &response.results.channels[0].alternatives[0].transcript;
    println!("{}", transcript);

    Ok(())
}
