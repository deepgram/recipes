//! Text Analysis Summarization - Generate a summary from plain text
//! Uses the Deepgram Read API to produce a concise summary of text content
//! without requiring any audio input. Useful for condensing articles,
//! documents, or any long-form text into key points.

use std::env;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = env::var("DEEPGRAM_API_KEY")
        .expect("DEEPGRAM_API_KEY environment variable not set");

    let text = "Deepgram is an AI speech company that provides automatic speech recognition \
        and text-to-speech APIs. Their Nova-3 model offers state-of-the-art accuracy \
        for transcription. The company also provides audio intelligence features like \
        sentiment analysis, topic detection, and intent recognition. Developers can \
        integrate Deepgram into their applications using SDKs for Python, JavaScript, \
        Go, .NET, and other languages.";

    let client = reqwest::Client::new();
    let response = client
        .post("https://api.deepgram.com/v1/read?language=en&summarize=v2")
        .header("Authorization", format!("Token {}", api_key))
        .json(&serde_json::json!({ "text": text }))
        .send()
        .await?
        .json::<serde_json::Value>()
        .await?;

    if let Some(summary) = response.pointer("/results/summary/text") {
        println!("Summary: {}", summary.as_str().unwrap_or(""));
    } else {
        println!("Response: {}", serde_json::to_string_pretty(&response)?);
    }

    Ok(())
}
