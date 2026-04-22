import subprocess
from pathlib import Path

def test_example_runs():
    """Runs the STT-AI-TTS pipeline example and verifies it produces output."""
    example = Path(__file__).parent / "example.py"
    output_file = Path(__file__).parent / "output.mp3"

    if output_file.exists():
        output_file.unlink()

    result = subprocess.run(
        ["python", str(example)],
        capture_output=True,
        text=True,
        timeout=120,
        cwd=str(example.parent),
    )
    assert result.returncode == 0, (
        f"Example failed\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"
    )
    assert result.stdout.strip(), "Example produced no output"
    assert "Stage 1" in result.stdout, "Missing STT stage output"
    assert "Stage 2" in result.stdout, "Missing TTS stage output"
    assert output_file.exists(), "Expected output.mp3 to be created"
    assert output_file.stat().st_size > 1000, "Audio file seems too small"

    output_file.unlink()
