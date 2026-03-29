# Instruction: Update Coverage Documentation

You are an autonomous agent maintaining coverage documentation for the Deepgram code samples
repository. Your job is to scan the `samples/` directory, build an accurate coverage matrix,
and update `COVERAGE.md` and per-language/per-product README files to reflect the current state.

This instruction is triggered on PR merge. Run it after every merge to `main` that touches
`samples/`.

---

## Step 1: Identify the Merged PR (Optional Context)

If the environment variable `GITHUB_EVENT_PATH` is set, read it for context:

```bash
if [ -n "${GITHUB_EVENT_PATH:-}" ]; then
  cat "$GITHUB_EVENT_PATH" | jq '{number: .pull_request.number, title: .pull_request.title}'
fi
```

If not available, find the most recently merged PR:

```bash
gh pr list --state merged --limit 1 --json number,title,mergedAt
```

Log the PR number for reference. This is informational only — the coverage update is based
entirely on the current filesystem state, not on what the PR contained.

---

## Step 2: Scan the `samples/` Directory

Find all recipe paths that have an example file:

```bash
find samples/ -name "example.*" ! -name "*_test*" ! -name "*.mod" | \
  sed 's|samples/||' | sed 's|/example.*||' | sort
```

This produces lines like:
```
go/speech-to-text/v1/transcribe-url-nova3
javascript/speech-to-text/v1/smart-format
python/audio-intelligence/v1/summarize
```

Each line has the structure: `{language}/{product}/{version}/{recipe-slug}`

Also collect the full list of languages present:

```bash
find samples/ -mindepth 1 -maxdepth 1 -type d | sed 's|samples/||' | sort
```

---

## Step 3: Load the Features Registry

```bash
cat .deepgram/features.json
```

This gives you the complete list of expected recipes (canonical paths without language prefix).
Use this as the source of truth for which recipes SHOULD exist.

---

## Step 4: Build the Coverage Matrix

For each recipe path in features.json, check whether it exists for each language:

- ✅ = `samples/{language}/{recipe-path}/example.*` exists
- ❌ = does not exist

Build a matrix where:
- Rows = recipe paths (grouped by product, then version)
- Columns = languages (python, javascript, go, dotnet, java, rust, cli)

Also calculate:
- Per-language coverage percentage: (covered / total) × 100
- Per-product coverage across all languages
- Total coverage: (total covered / (total recipes × languages)) × 100

---

## Step 5: Write COVERAGE.md

Write (or overwrite) `COVERAGE.md` at the repository root with this structure:

```markdown
# Coverage Matrix

Last updated: {current date}

## Summary

| Language | Covered | Total | Coverage |
|----------|---------|-------|----------|
| Python | {n} | {total} | {pct}% |
| JavaScript | {n} | {total} | {pct}% |
| Go | {n} | {total} | {pct}% |
| .NET | {n} | {total} | {pct}% |
| Java | {n} | {total} | {pct}% |
| Rust | {n} | {total} | {pct}% |
| CLI | {n} | {total} | {pct}% |
| **Total** | {n} | {total} | {pct}% |

## Recipe Coverage

### {Product Name} / {version}

| Recipe | Python | JS | Go | .NET | Java | Rust | CLI |
|--------|--------|----|----|------|------|------|-----|
| [{recipe-slug}](samples/python/{product}/{version}/{recipe-slug}/) | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

{Repeat for each product/version group}

## Notes

- ✅ = Example exists in `samples/{language}/`
- ❌ = Not yet generated (run `discover-sdks` to queue generation)
- Coverage auto-updates on every PR merge to `main`
```

For recipe rows, link each ✅ to the actual directory path. For ❌, leave it as plain text.

---

## Step 6: Update Per-Language README Files

For each language directory that exists under `samples/`, write or update
`samples/{language}/README.md`:

```markdown
# {Language} Samples

{N} recipe(s) covering {M} product(s).

## Recipes

### {Product Name}

| Version | Recipe | Description |
|---------|--------|-------------|
| {version} | [{recipe-slug}]({product}/{version}/{recipe-slug}/) | {one-line description from recipe README} |

{Repeat for each product}

## Running Tests

{Language-appropriate test instructions, e.g.:}

```bash
# Python
pip install -r requirements.txt
pytest . -v --timeout=60

# JavaScript
npm install && npm test

# Go
go test ./... -v -timeout 120s
```

## Prerequisites

- Set `DEEPGRAM_API_KEY` in your environment
- {Language-specific version requirement, e.g. Python 3.9+, Node 20+, Go 1.22+}
```

To get one-line descriptions for each recipe, read the first line after the `#` heading
in each recipe's `README.md`:

```bash
head -3 "samples/{language}/{product}/{version}/{recipe-slug}/README.md" 2>/dev/null | tail -1
```

---

## Step 7: Update Per-Product-Per-Version README Files

For each `samples/{language}/{product}/{version}/` directory that contains at least one
recipe, write or update a README:

```markdown
# {Language} / {Product} / {version}

## Recipes

| Recipe | Description |
|--------|-------------|
| [{recipe-slug}]({recipe-slug}/) | {one-line description} |

## Notes

All recipes in this directory require `DEEPGRAM_API_KEY` to be set in the environment.
```

---

## Step 8: Commit Changes if Anything Changed

Check whether any files were actually modified:

```bash
git diff --quiet && git diff --cached --quiet
```

If nothing changed:
```
No coverage changes to commit. Files are already up to date.
```
Stop here.

If changes exist:

```bash
git add COVERAGE.md
git add samples/

git commit -m "docs: update coverage matrix

Triggered by PR merge. Reflects current state of samples/."

git push
```

Verify the push succeeded. If it fails due to a conflict, pull and retry:

```bash
git pull --rebase && git push
```

---

## Safety Rules

- NEVER delete any existing `example.*`, `example_test.*`, or recipe-level `README.md` files
- ONLY write to: `COVERAGE.md`, `samples/{language}/README.md`, `samples/{language}/{product}/{version}/README.md`
- NEVER commit to a non-main branch from this instruction — coverage updates always go to main
- If reading any recipe README fails (file missing), skip the description column and leave it blank
- If the push fails twice, output an error and stop — do not retry indefinitely
