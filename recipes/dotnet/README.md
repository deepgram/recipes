# .NET SDK Samples

Code samples for the [Deepgram .NET SDK](https://github.com/deepgram/deepgram-dotnet-sdk).

## Structure

Each recipe is a standalone .NET console application:

```
recipes/dotnet/{product}/v1/{recipe}/
  Program.cs          # The runnable example
  {Recipe}.csproj     # Project file with Deepgram SDK dependency
  ExampleTest.cs      # Test class
  README.md           # Recipe explanation
```

## Requirements

- .NET 8.0+
- `DEEPGRAM_API_KEY` environment variable

## Run any example

```bash
cd recipes/dotnet/{product}/v1/{recipe}
dotnet run
```

## Run all tests

```bash
cd recipes/dotnet
dotnet test
```
