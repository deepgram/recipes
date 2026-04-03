/*
 * Voice Agents Basic Connection Recipe
 * Demonstrates establishing a WebSocket connection to Deepgram's Voice Agents API.
 * Voice agents provide real-time conversational AI.
 */

use std::env;
use tokio_tungstenite::{connect_async, tungstenite::Message};
use futures::{SinkExt, StreamExt};
use serde_json::json;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let _ = rustls::crypto::ring::default_provider().install_default();
    let api_key = env::var("DEEPGRAM_API_KEY")?;
    // Connect to Deepgram Voice Agents endpoint  // <-- THIS is the feature this recipe demonstrates
    let url = format!("wss://agent.deepgram.com/agent?authorization=token%20{}", api_key);
    let (ws_stream, _) = connect_async(&url).await?;
    
    println!("Connected to Deepgram Voice Agents");
    let (mut write, mut read) = ws_stream.split();
    
    // Send basic agent settings
    let settings = json!({
        "type": "Settings",
        "audio": {
            "input": { "encoding": "linear16", "sample_rate": 16000 },
            "output": { "encoding": "linear16", "sample_rate": 16000, "container": "none" }
        },
        "agent": {
            "listen": { "model": "nova-3" },
            "think": {
                "provider": { "type": "open_ai" },
                "model": "gpt-4o-mini",
                "instructions": "You are a helpful assistant."
            },
            "speak": { "model": "aura-2-thalia-en" }
        }
    });
    
    write.send(Message::Text(settings.to_string())).await?;
    println!("Sent agent configuration");
    
    // Listen for Welcome message
    if let Some(Ok(Message::Text(text))) = read.next().await {
        println!("Received: {}", text);
        if text.contains("\"type\":\"Welcome\"") {
            println!("Voice agent connection established successfully!");
        }
    }
    Ok(())
}