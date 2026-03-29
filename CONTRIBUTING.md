# Contributing

## Automatic generation

This repository is self-evolving. The `discover-sdks.yml` workflow checks for coverage gaps every hour and creates queue issues that trigger example generation.

To trigger generation manually:
1. Go to Actions → "Process Queue" → "Run workflow"
2. Or create an issue using the "Queue - Generate Examples" template

## Adding examples manually

To add a recipe manually, create a directory following this structure:

```
recipes/{language}/{product}/{version}/{recipe-slug}/
  example.{ext}          # Runnable example
  example_test.{ext}     # Test
  README.md              # Explanation
```

### Recipe standards

**`example.{ext}`:**
- Read API key from `DEEPGRAM_API_KEY` environment variable (never hardcode)
- Use `https://dpgr.am/spacewalk.wav` as demo audio
- Print meaningful output (transcript text, file size, etc.)
- Keep under 50 lines

**`example_test.{ext}`:**
- Run the example as a subprocess
- Assert exit code == 0
- Assert stdout is non-empty
- Set a 60-second timeout

**`README.md`:**
- Explain what the feature does
- List the key parameters and their values
- Show a sample output
- Include prerequisites and run command

### README template

```markdown
# {Feature Name} ({Product} {Version})

{One-sentence description}

## What it does

{2-3 sentences explaining the feature and when to use it}

## Key parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `param` | `value` | description |

## Example output

\`\`\`
{sample output}
\`\`\`

## Prerequisites

- {Language} {version}+
- Set `DEEPGRAM_API_KEY` environment variable
- Install: `{install_command}`

## Run

\`\`\`bash
{run_command}
\`\`\`
```

## Adding a new SDK

If Deepgram publishes a new SDK:
1. Add an entry to `.deepgram/sdks.json`
2. Create `recipes/{language}/` with appropriate manifest file (requirements.txt, package.json, etc.)
3. Create `.github/workflows/test-{language}.yml`
4. Trigger discovery: Actions → "Discover SDKs" → "Run workflow"

## Running tests locally

```bash
# Python
export DEEPGRAM_API_KEY=your_key
cd recipes/python
pip install -r requirements.txt
pytest . -v --timeout=60

# JavaScript
cd recipes/javascript
npm install
npm test

# Go
cd recipes/go
go test ./... -v

# All: run the test workflow locally with act
act -j test --secret DEEPGRAM_API_KEY=your_key
```

## Pull requests

1. Branch naming: `recipes/{language}/{product}-{feature}`
2. Commit message: `feat({language}): add {product} {version} {recipe} recipe`
3. Tests must pass before merging
4. COVERAGE.md is auto-updated on merge
