//! Text Analysis Sentiment - Analyze sentiment from plain text
//! Uses the Deepgram Read API to detect positive, negative, and neutral
//! sentiment in text content without requiring audio input. Returns both
//! an overall average and per-segment sentiment breakdowns.

use std::env;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = env::var("DEEPGRAM_API_KEY")
        .expect("DEEPGRAM_API_KEY environment variable not set");

    let text = "I absolutely love this product! It exceeded all my expectations. \
        However, the shipping was terrible and took three weeks to arrive. \
        Overall, I'm satisfied with my purchase despite the delivery issues.";

    let client = reqwest::Client::new();
    let response = client
        .post("https://api.deepgram.com/v1/read?language=en&sentiment=true")
        .header("Authorization", format!("Token {}", api_key))
        .json(&serde_json::json!({ "text": text }))
        .send()
        .await?
        .json::<serde_json::Value>()
        .await?;

    if let Some(sentiments) = response.pointer("/results/sentiments") {
        if let Some(avg) = sentiments.pointer("/average") {
            println!("Average sentiment: {} (score: {:.2})",
                avg["sentiment"].as_str().unwrap_or(""),
                avg["sentiment_score"].as_f64().unwrap_or(0.0));
        }
        if let Some(segments) = sentiments["segments"].as_array() {
            for seg in segments {
                println!("  [{}] {}",
                    seg["sentiment"].as_str().unwrap_or(""),
                    seg["text"].as_str().unwrap_or(""));
            }
        }
    } else {
        println!("Response: {}", serde_json::to_string_pretty(&response)?);
    }

    Ok(())
}
