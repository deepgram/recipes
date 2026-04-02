import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ExampleTest {
    @Test
    void exampleRunsAndProducesOutput() throws Exception {
        ProcessBuilder pb = new ProcessBuilder(
            "mvn", "-q", "exec:java", "-Dexec.mainClass=Example"
        );
        pb.directory(new java.io.File(System.getProperty("user.dir")));
        pb.redirectErrorStream(true);
        Process process = pb.start();
        String output = new String(process.getInputStream().readAllBytes());
        boolean exited = process.waitFor(60, java.util.concurrent.TimeUnit.SECONDS);
        assertTrue(exited, "Process did not exit in time");
        assertEquals(0, process.exitValue(), "Example exited with code " + process.exitValue() + "\n" + output);
        assertFalse(output.trim().isEmpty(), "Example produced no output");
    }
}
