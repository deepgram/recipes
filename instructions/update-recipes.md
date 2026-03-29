# Instruction: Update Existing Recipes

You are an autonomous agent that updates existing recipe files when SDK APIs change.
Triggered by `queue:update` GitHub Issues that describe a specific API change.

---

## Step 1: Find the Triggering Queue Issue

```bash
gh issue list \
  --label "type:queue" \
  --label "action:update" \
  --state open \
  --json number,title,body,labels \
  --limit 1 \
  --jq '.[0]'
```

If no issue is returned, output:
```
No queue:update issues found. Nothing to do.
```
And stop.

Extract from the HTML comment block:
- `language` — which SDK (e.g., `python`)
- `recipe` — the recipe path (e.g., `python/speech-to-text/v1/transcribe-url`)
- `sdk-version` — new SDK version
- `reason` — why the update is needed (e.g., `api-change`, `deprecation`)

Store the issue number for later.

---

## Step 2: Read the Recipe to Update

```bash
# Find the recipe directory
RECIPE_DIR="recipes/{recipe-path}"
ls "$RECIPE_DIR"

# Read the existing files
cat "$RECIPE_DIR/example.{ext}"
cat "$RECIPE_DIR/example_test.{ext}"
cat "$RECIPE_DIR/README.md"
```

---

## Step 3: Understand the Required Change

Read the issue body carefully. It should describe:
- What changed in the SDK (old pattern vs new pattern)
- Which files need updating

Also fetch the SDK README and relevant release notes for context:

```bash
# Load SDK config to get the repo
cat .deepgram/sdks.json

# Fetch current SDK README
gh api "repos/{repo}/readme" --jq '.content' | base64 -d | head -300

# Fetch the specific release
gh api "repos/{repo}/releases" --jq \
  "[.[] | select(.tag_name == \"{sdk-version}\")] | .[0].body"
```

---

## Step 4: Create a Feature Branch

```bash
BRANCH="update/{language}-{recipe-slug}-$(date +%Y%m%d)"
git checkout -b "$BRANCH"
CURRENT=$(git branch --show-current)
[ "$CURRENT" = "main" ] && echo "ERROR: On main branch. Aborting." && exit 1
```

---

## Step 5: Apply the Changes

Update `example.{ext}` to use the new API pattern described in the issue.

Rules:
- Keep the example under 50 lines
- Keep it runnable and printing meaningful output
- Use the same `DEEPGRAM_API_KEY` environment variable pattern
- Use the same demo audio URL `https://dpgr.am/spacewalk.wav`
- Do NOT change the structure or intent of the recipe — only update the API calls

If the README's params table is now outdated (parameters renamed or removed), update it too.
If new parameters were added that are relevant, add them to the table.

The test (`example_test.{ext}`) usually does NOT need changing — it just runs the example
and checks for output. Only update it if the expected output pattern changed fundamentally.

---

## Step 6: Commit and Push

```bash
git add "recipes/{recipe-path}/"
git commit -m "fix({language}): update {recipe-slug} for {sdk} {sdk-version}

API change: {brief description from issue}"
git push origin "$BRANCH"
```

---

## Step 7: Create a PR

```bash
gh pr create \
  --title "fix({language}): update {recipe-slug} for {sdk} {sdk-version}" \
  --label "type:samples" \
  --label "language:{language}" \
  --body "$(cat <<'EOF'
## Recipe Update: {recipe-path}

Updates this recipe to use the current API from {sdk} {sdk-version}.

### What changed

{description from the issue}

### Files updated

- `recipes/{recipe-path}/example.{ext}` — updated API call
- `recipes/{recipe-path}/README.md` — updated params table (if applicable)

### Closes

Closes #{issue-number}
EOF
)"
```

---

## Step 8: Close the Queue Issue

```bash
gh issue close {issue_number} \
  --comment "Updated recipe. See PR #{pr_number} for the changes."
```

---

## Safety Rules

- Never change the recipe's purpose — only update the API usage
- Never add hardcoded API keys
- Never commit audio files or binary outputs
- If the new API is unclear, read the SDK README and examples before guessing
- If the change would make the example non-functional, create a comment on the issue
  explaining why and ask for clarification — do not close it
