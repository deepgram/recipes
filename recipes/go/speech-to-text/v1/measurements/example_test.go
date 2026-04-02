package main

import (
	"os/exec"
	"strings"
	"testing"
)

func TestExampleRuns(t *testing.T) {
	cmd := exec.Command("go", "run", "example.go")
	output, err := cmd.CombinedOutput()
	if err != nil {
		t.Fatalf("Example failed: %v\nOutput: %s", err, string(output))
	}
	if strings.TrimSpace(string(output)) == "" {
		t.Fatal("Example produced no output")
	}
}
