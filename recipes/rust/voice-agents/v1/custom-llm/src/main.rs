/*
 * Voice Agents Custom LLM Configuration Recipe
 * Demonstrates configuring a voice agent with a custom LLM provider.
 * Customizes the AI reasoning engine while keeping Deepgram speech processing.
 */

use std::env;
use tokio_tungstenite::{connect_async, tungstenite::Message};
use futures::{SinkExt, StreamExt};
use serde_json::json;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let _ = rustls::crypto::ring::default_provider().install_default();
    let api_key = env::var("DEEPGRAM_API_KEY")?;
    
    // Connect to Deepgram Voice Agents endpoint
    let url = format!("wss://agent.deepgram.com/agent?authorization=token%20{}", api_key);
    let (ws_stream, _) = connect_async(&url).await?;
    
    println!("Connected to Deepgram Voice Agents");
    let (mut write, mut read) = ws_stream.split();
    
    // Configure agent with custom LLM provider
    let settings = json!({
        "type": "Settings",
        "audio": {
            "input": { "encoding": "linear16", "sample_rate": 16000 },
            "output": { "encoding": "linear16", "sample_rate": 16000, "container": "none" }
        },
        "agent": {
            "listen": { "model": "nova-3" },
            "think": {  // <-- THIS is the feature this recipe demonstrates
                "provider": { "type": "anthropic" },
                "model": "claude-3-5-sonnet",
                "instructions": "You are a technical expert specializing in space technology."
            },
            "speak": { "model": "aura-2-thalia-en" }
        }
    });
    
    write.send(Message::Text(settings.to_string())).await?;
    println!("Sent custom LLM configuration: Anthropic Claude 3.5 Sonnet");
    
    // Listen for Welcome message
    if let Some(Ok(Message::Text(text))) = read.next().await {
        println!("Received: {}", text);
    }
    
    Ok(())
}