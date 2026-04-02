//! Text Analysis Intent Recognition - Detect intents from plain text
//! Uses the Deepgram Read API to analyze text and identify speaker intents
//! without any audio input. This is useful for understanding what actions
//! or outcomes a speaker is trying to achieve from text content.

use std::env;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = env::var("DEEPGRAM_API_KEY")
        .expect("DEEPGRAM_API_KEY environment variable not set");

    let text = "I'd like to return this product and get a refund. \
        The item arrived damaged and I'm very disappointed with the quality. \
        Can you also update my shipping address for future orders?";

    let client = reqwest::Client::new();
    let response = client
        .post("https://api.deepgram.com/v1/read?language=en&intents=true")
        .header("Authorization", format!("Token {}", api_key))
        .json(&serde_json::json!({ "text": text }))
        .send()
        .await?
        .json::<serde_json::Value>()
        .await?;

    if let Some(segments) = response.pointer("/results/intents/segments") {
        if let Some(arr) = segments.as_array() {
            for seg in arr {
                println!("Text: {}", seg["text"].as_str().unwrap_or(""));
                if let Some(intents) = seg["intents"].as_array() {
                    for intent in intents {
                        println!("  Intent: {} (confidence: {:.2})",
                            intent["intent"].as_str().unwrap_or(""),
                            intent["confidence_score"].as_f64().unwrap_or(0.0));
                    }
                }
            }
        }
    } else {
        println!("Response: {}", serde_json::to_string_pretty(&response)?);
    }

    Ok(())
}
