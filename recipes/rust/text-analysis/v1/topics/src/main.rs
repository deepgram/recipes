//! Text Analysis Topic Detection - Identify topics from plain text
//! Uses the Deepgram Read API to detect topics discussed in text content
//! without requiring audio input. Returns per-segment topic lists with
//! confidence scores for each detected topic.

use std::env;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = env::var("DEEPGRAM_API_KEY")
        .expect("DEEPGRAM_API_KEY environment variable not set");

    let text = "The new electric vehicle from Tesla features a range of 400 miles \
        and uses a revolutionary battery technology. Meanwhile, SpaceX \
        successfully launched another batch of Starlink satellites into orbit. \
        In healthcare news, a new mRNA vaccine shows promising results in \
        early clinical trials for treating certain types of cancer.";

    let client = reqwest::Client::new();
    let response = client
        .post("https://api.deepgram.com/v1/read?language=en&topics=true")
        .header("Authorization", format!("Token {}", api_key))
        .json(&serde_json::json!({ "text": text }))
        .send()
        .await?
        .json::<serde_json::Value>()
        .await?;

    if let Some(segments) = response.pointer("/results/topics/segments") {
        if let Some(arr) = segments.as_array() {
            for seg in arr {
                println!("Text: {}", seg["text"].as_str().unwrap_or(""));
                if let Some(topics) = seg["topics"].as_array() {
                    for topic in topics {
                        println!("  Topic: {} (confidence: {:.2})",
                            topic["topic"].as_str().unwrap_or(""),
                            topic["confidence_score"].as_f64().unwrap_or(0.0));
                    }
                }
            }
        }
    } else {
        println!("Response: {}", serde_json::to_string_pretty(&response)?);
    }

    Ok(())
}
