//! Key Term Prompting - Boost recognition of specific terms with Nova-3
//! Key term prompting provides a list of important terms to the model so it
//! can prioritize their correct recognition. Unlike keyword boosting, key
//! terms work at a deeper model level with Nova-3 for more accurate results
//! on domain-specific vocabulary.

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
        .keyterms(["NASA", "spacewalk", "mankind"])  // <-- Key terms to boost
        .smart_format(true)
        .build();

    let response = dg.transcription().prerecorded(source, &options).await?;

    let transcript = &response.results.channels[0].alternatives[0].transcript;
    println!("{}", transcript);

    Ok(())
}
