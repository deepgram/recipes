//! Filler Words - Include filler words in transcript output
//! When enabled, filler words such as "uh", "um", "mhm", and "uh huh" are
//! preserved in the transcript rather than being filtered out. This is useful
//! for conversation analysis, speaker profiling, and verbatim transcription.

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
        .filler_words(true)  // <-- Preserves filler words in transcript
        .punctuate(true)
        .build();

    let response = dg.transcription().prerecorded(source, &options).await?;

    let transcript = &response.results.channels[0].alternatives[0].transcript;
    println!("{}", transcript);

    Ok(())
}
