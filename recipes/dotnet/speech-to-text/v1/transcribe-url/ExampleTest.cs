using System.Diagnostics;
using Xunit;

public class ExampleTest
{
    [Fact]
    public void ExampleRunsAndProducesOutput()
    {
        var dir = Path.GetDirectoryName(typeof(ExampleTest).Assembly.Location)!;
        var projectDir = Path.GetFullPath(Path.Combine(dir, "..", "..", "..", ".."));

        var psi = new ProcessStartInfo("dotnet", "run")
        {
            WorkingDirectory = projectDir,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
        };

        using var process = Process.Start(psi)!;
        var stdout = process.StandardOutput.ReadToEnd();
        var stderr = process.StandardError.ReadToEnd();
        process.WaitForExit(60_000);

        Assert.Equal(0, process.ExitCode);
        Assert.NotEmpty(stdout.Trim());
    }
}
