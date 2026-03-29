# Instruction: Reconcile Index

You are an autonomous agent performing daily maintenance on the Deepgram code samples
repository. Your job is to verify that the root `README.md` count table is accurate,
and to create `queue:fix` issues for any sample directories that are missing required files.

This instruction is idempotent — running it multiple times should produce the same result.

---

## Step 1: Count Actual Samples Per Language

Count the number of example files present for each language:

```bash
for lang in python javascript go dotnet java rust cli; do
  count=$(find "samples/$lang/" -name "example.*" ! -name "*_test*" ! -name "*.mod" 2>/dev/null | wc -l | tr -d ' ')
  echo "$lang: $count"
done
```

Also count distinct products and recipe slugs per language:

```bash
for lang in python javascript go dotnet java rust cli; do
  products=$(find "samples/$lang/" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
  echo "$lang products: $products"
done
```

Store these counts for comparison in Step 2.

---

## Step 2: Check Root README.md Count Table

Read the root `README.md`:

```bash
cat README.md
```

Find the count table in the README. It should have a section or table showing per-language
sample counts. This might look like:

```
| Language | Recipes |
|----------|---------|
| Python | 12 |
| JavaScript | 10 |
...
```

Or it may be inline text like "12 Python examples".

Compare the counts in the README against the actual counts from Step 1.

If the README does not have a count table or count section, note that it needs to be added.

---

## Step 3: Update the README Count Table if Inaccurate

If any count in the README differs from the actual filesystem count, update ONLY the count
table section. Do not rewrite the entire README.

Use the Read and Edit tools to make targeted updates to the count table.

Only modify the count numbers — do not change any other content in the README.

If the README has no count table at all, add one in an appropriate location (after the
introduction, before any detailed sections):

```markdown
## Sample Coverage

| Language | Recipes |
|----------|---------|
| Python | {count} |
| JavaScript | {count} |
| Go | {count} |
| .NET | {count} |
| Java | {count} |
| Rust | {count} |
| CLI | {count} |
```

---

## Step 4: Verify Each Sample Directory Has All Required Files

For every directory under `samples/` that represents a recipe (depth 4: language/product/version/slug):

```bash
find samples/ -mindepth 4 -maxdepth 4 -type d
```

For each directory found, check that ALL three required files exist:
1. An example file: `example.*` (not ending in `_test` or `.mod`)
2. A test file: `example_test.*` or `example.test.*` or `ExampleTest.*` or `example_test.sh`
3. A README: `README.md`

```bash
# Check each directory
for dir in $(find samples/ -mindepth 4 -maxdepth 4 -type d); do
  has_example=$(find "$dir" -maxdepth 1 -name "example.*" ! -name "*_test*" ! -name "*.mod" 2>/dev/null | head -1)
  has_test=$(find "$dir" -maxdepth 1 \( -name "example_test.*" -o -name "example.test.*" -o -name "ExampleTest.*" -o -name "example_test.sh" \) 2>/dev/null | head -1)
  has_readme=$([ -f "$dir/README.md" ] && echo "yes" || echo "")

  if [ -z "$has_example" ] || [ -z "$has_test" ] || [ -z "$has_readme" ]; then
    echo "INCOMPLETE: $dir"
    [ -z "$has_example" ] && echo "  - Missing: example file"
    [ -z "$has_test" ] && echo "  - Missing: test file"
    [ -z "$has_readme" ] && echo "  - Missing: README.md"
  fi
done
```

---

## Step 5: Create queue:fix Issues for Incomplete Directories

For each incomplete directory found in Step 4, check if a `queue:fix` issue already exists:

```bash
gh issue list \
  --label "type:queue" \
  --label "action:fix" \
  --state open \
  --json number,title --limit 50
```

For any incomplete directory that does NOT already have an open fix issue, create one:

```bash
gh issue create \
  --title "queue:fix: incomplete recipe at {path}" \
  --label "type:queue" \
  --label "action:fix" \
  --label "language:{language}" \
  --body "$(cat <<'BODY'
## Incomplete Recipe Directory

The following recipe directory is missing required files:

**Path:** `{path}`
**Language:** {language}

### Missing Files

{list of missing files}

### Required Files

Every recipe directory must contain:
1. `example.{ext}` — the runnable example (< 50 lines)
2. `example_test.{ext}` — a test that runs the example
3. `README.md` — documentation for the recipe

### How to Fix

Generate the missing files manually or re-trigger example generation:

```bash
claude --model claude-opus-4-6 -p "$(cat instructions/generate-examples.md)"
```

Or add the missing files manually following the templates in `instructions/generate-examples.md`.
BODY
)"
```

Check for existing issues by looking for the path in issue titles. Only create if no
existing open issue covers this path.

---

## Step 6: Commit README Changes if Anything Changed

```bash
git diff --quiet README.md
```

If the README was modified:

```bash
git add README.md
git commit -m "docs: update sample count table in README

Reconciled counts based on current state of samples/."
git push
```

If nothing changed:
```
README counts are accurate. No commit needed.
```

---

## Step 7: Output a Summary Report

```
=== reconcile-index run complete ===

Languages checked: python, javascript, go, dotnet, java, rust, cli
README count table: {accurate | updated}
Incomplete recipe directories found: {N}
  {list of incomplete paths, or "none"}
queue:fix issues created: {N}
  {list of issue numbers and titles, or "none"}
```

---

## Safety Rules

- NEVER modify any file except `README.md` from this instruction
- NEVER delete any files
- NEVER commit to a feature branch — only push to main (README updates only)
- If the `find` command produces no results for a language (directory doesn't exist), that is
  not an error — just report 0 for that language
- If creating a `queue:fix` issue fails, log the error and continue checking other directories
- This instruction must be safe to run on a repo with zero samples (all counts will be 0)
