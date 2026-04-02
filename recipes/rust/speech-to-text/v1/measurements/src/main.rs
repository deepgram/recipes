//! Measurements - Convert spoken measurements to standard abbreviations
//! When enabled, spoken measurement values like "five kilograms" or "ten
//! miles per hour" are converted to their abbreviated forms ("5 kg",
//! "10 mph") in the transcript output.

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
        .measurements(true)  // <-- Converts spoken measurements to abbreviations
        .punctuate(true)
        .build();

    let response = dg.transcription().prerecorded(source, &options).await?;

    let transcript = &response.results.channels[0].alternatives[0].transcript;
    println!("{}", transcript);

    Ok(())
}
