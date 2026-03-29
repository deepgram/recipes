import subprocess
from pathlib import Path


def test_example_runs():
    """Runs the topics example and verifies it produces topic output."""
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
    assert "Topics:" in result.stdout, "Expected topic detection output"
