# Java SDK Samples

Code samples for the [Deepgram Java SDK](https://github.com/deepgram/deepgram-java-sdk).

## Structure

Each recipe is a standalone Maven project:

```
samples/java/{product}/v1/{recipe}/
  src/main/java/Example.java       # The runnable example
  src/test/java/ExampleTest.java   # JUnit test
  pom.xml                          # Maven project with Deepgram SDK dependency
  README.md                        # Recipe explanation
```

## Requirements

- Java 21+
- Maven 3.9+
- `DEEPGRAM_API_KEY` environment variable

## Run any example

```bash
cd samples/java/{product}/v1/{recipe}
mvn exec:java -Dexec.mainClass="Example"
```

## Run all tests

From the root samples/java/ directory:
```bash
find . -name "pom.xml" -maxdepth 4 | xargs -I{} sh -c 'cd "$(dirname {})" && mvn test'
```
