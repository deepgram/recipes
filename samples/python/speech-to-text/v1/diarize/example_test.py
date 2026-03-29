import os
import subprocess
from pathlib import Path

def test_example_runs():
    """Runs the diarize example and verifies speaker labels appear in output."""
    example = Path(__file__).parent / "example.py"
    result = subprocess.run(
        ["python", str(example)],
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert result.returncode == 0, (
        f"Example failed\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"
    )
    assert result.stdout.strip(), "Example produced no output"
    assert "[Speaker" in result.stdout, "Expected speaker labels in output"
