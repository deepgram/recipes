use std::process::Command;

#[test]
#[ignore] // WebSocket voice agent — hangs indefinitely in CI (requires live session)
fn example_runs_and_produces_output() {
    let output = Command::new("cargo")
        .args(["run", "--quiet"])
        .output()
        .expect("Failed to run example");
    assert!(output.status.success(), "Example failed with: {}", String::from_utf8_lossy(&output.stderr));
    assert!(!String::from_utf8_lossy(&output.stdout).trim().is_empty(), "Example produced no output");
}