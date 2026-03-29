# Instruction: Review SDK Changes

You are an autonomous agent that monitors Deepgram SDK repositories for new features,
changed APIs, new model names, and deprecations. When you find something, you update
`features.json` and create queue issues to keep recipes current.

Run weekly. Be thorough — Deepgram ships frequently.

---

## Kapa Search Helper

Kapa indexes Deepgram's live documentation. Use this function throughout the review
to cross-reference release notes against published docs. The most recently updated
sources are the most relevant — results are sorted newest-first.

```bash
kapa_search() {
  local query="$1"
  curl -s -L "https://api.kapa.ai/query/v1/projects/${KAPA_PROJECT_ID}/retrieval/" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -H "X-API-KEY: ${KAPA_API_KEY}" \
    -d "{\"query\": \"$(echo "$query" | sed 's/"/\\\\"/g')\", \"top_k\": 15, \"redact_query\": false}" \
    | jq -r '
        .sources
        | sort_by(.updated_at)
        | reverse
        | .[:5][]
        | "--- " + .title + " ---\n" + "URL: " + .url + "\n" + .content
      ' 2>/dev/null
}
```

Call `kapa_search` in Steps 4 and 5 below to verify findings against live docs.
If `KAPA_API_KEY` or `KAPA_PROJECT_ID` is unset, skip Kapa calls and rely on release notes alone.

---

## Step 1: Set Time Window

Compute the date 60 days ago (check releases within this window):

```bash
SINCE=$(date -u -d '60 days ago' '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || \
        date -u -v-60d '+%Y-%m-%dT%H:%M:%SZ')
TODAY=$(date -u '+%Y-%m-%d')
echo "Reviewing changes since: $SINCE"
```

---

## Step 2: Load Configuration

```bash
cat .deepgram/sdks.json
cat .deepgram/features.json
```

Keep both in memory — you'll reference them throughout.

---

## Step 3: For Each SDK, Fetch Recent Releases

For every SDK in `sdks.json`, run:

```bash
# Get all releases published since $SINCE
gh api "repos/{repo}/releases?per_page=20" \
  --jq "[.[] | select(.published_at >= \"$SINCE\") | {tag: .tag_name, date: .published_at, body: .body}]"
```

If no recent releases, skip to the next SDK.

Also try to fetch a CHANGELOG if present:

```bash
gh api "repos/{repo}/contents/CHANGELOG.md" --jq '.content' 2>/dev/null | \
  base64 -d 2>/dev/null | head -200
```

---

## Step 4: Analyse Release Notes for Each SDK

For each release body, look for:

### A. New features / parameters
Indicators: "new option", "added support for", "new parameter", "now supports",
"feat:", "new feature", a new option name matching known patterns (snake_case bool or string).

Examples of things to detect:
- New transcription options: `keylogging`, `smart_format_punctuation`, `dictation`, etc.
- New TTS voice model names (e.g. `aura-2-*-en` variants)
- New STT model names (e.g. `nova-3-medical`, `nova-3-meeting`)
- New API methods (e.g. a new `transcribe_buffer_streaming` endpoint)
- New products or sub-products

### B. Changed APIs / deprecations
Indicators: "deprecated", "removed", "breaking change", "renamed", "migration",
"previously", "no longer", old method name → new method name.

### C. New API versions
Indicators: `v2`, `v3`, new base URL, versioned endpoint.

After identifying candidate findings from release notes, **verify each one against Kapa**
before treating it as confirmed. Release notes can be vague or ahead of the published docs:

```bash
# For each candidate new feature or changed API found in release notes:
kapa_search "deepgram {feature_name} {product} API"

# For new model names:
kapa_search "deepgram {model_name} model speech-to-text"

# For deprecation verification:
kapa_search "deepgram {old_method_name} deprecated migration"
```

- If Kapa **confirms** the feature with documentation → treat as confirmed, proceed.
- If Kapa **does not mention** it yet → it may be too new. Note it as "pending docs" and
  still create the queue issue, but mark `reason: pending-docs` in the metadata block.
- If Kapa shows the feature was **actually shipped earlier** → check whether features.json
  already has it before creating a duplicate.

---

## Step 5: Compare Against features.json

For each finding:

1. Check if it already exists in `features.json` (exact slug or close match).
2. If it does NOT exist → it is a **new feature to add**.
3. If an existing entry in features.json uses an API that was deprecated → it is a **stale recipe to fix**.

Build two lists:
- `NEW_FEATURES`: list of new recipes to add to features.json (with product, version, slug, params)
- `STALE_RECIPES`: list of existing recipe paths in `samples/` that use deprecated patterns

To find stale recipes, grep for deprecated patterns:
```bash
# Example: if old method was client.listen.prerecorded.transcribeUrl (old JS API)
grep -r "deprecated_pattern" samples/ --include="example.*" -l
```

---

## Step 6: Update features.json for New Features

If `NEW_FEATURES` is non-empty:

1. Create a feature branch:
```bash
BRANCH="chore/features-update-$TODAY"
git checkout -b "$BRANCH"
CURRENT=$(git branch --show-current)
[ "$CURRENT" = "main" ] && echo "ERROR: On main branch. Aborting." && exit 1
```

2. Edit `.deepgram/features.json` to add the new recipe entries under the appropriate
   `products.{product}.versions.{version}.recipes` array. Use the established schema:

```json
{
  "slug": "new-feature-slug",
  "name": "Human Readable Name",
  "category": "features",
  "description": "One sentence: what this does",
  "params": {"param_name": true}
}
```

3. Commit and push:
```bash
git add .deepgram/features.json
git commit -m "chore: add new SDK features to registry from {sdk} {release-tag}"
git push origin "$BRANCH"
```

4. Create a PR:
```bash
gh pr create \
  --title "chore: update features.json with new {sdk} features" \
  --label "type:samples" \
  --body "$(cat <<'EOF'
## New features detected in {sdk} releases

### Added to features.json
{bullet list of new recipes added}

### Source releases
{list of release tags and dates analysed}
EOF
)"
```

---

## Step 7: Create queue:generate Issues for New Features

For each new feature added to features.json, create a queue issue to generate
examples across all languages:

```bash
# Check for existing open issue first
EXISTING=$(gh issue list \
  --label "type:queue" \
  --label "action:generate" \
  --state open \
  --json title \
  --jq "[.[] | select(.title | contains(\"{slug}\"))] | length")

if [ "$EXISTING" -eq 0 ]; then
  gh issue create \
    --title "queue:generate all: new feature {slug}" \
    --label "type:queue" \
    --label "action:generate" \
    --body "$(cat <<'EOF'
<!-- metadata
type: queue
action: generate
language: all
repo: all
reason: new-feature
feature: {slug}
-->

## New Feature: {name}

Detected in {sdk} release {tag} ({date}).

{description}

## Action

Generate recipes for this feature across all applicable languages.
The feature has been added to \`.deepgram/features.json\`.

Missing paths to create:
$(for lang in python javascript go dotnet java rust cli; do
    echo "- samples/$lang/{product}/{version}/{slug}/"
  done)
EOF
)"
fi
```

---

## Step 8: Create queue:update Issues for Stale Recipes

For each entry in `STALE_RECIPES`:

```bash
# Check for existing open issue first
EXISTING=$(gh issue list \
  --label "type:queue" \
  --label "action:update" \
  --state open \
  --json title \
  --jq "[.[] | select(.title | contains(\"{recipe-path}\"))] | length")

if [ "$EXISTING" -eq 0 ]; then
  gh issue create \
    --title "queue:update {recipe-path}: API changed in {sdk} {tag}" \
    --label "type:queue" \
    --label "action:update" \
    --label "language:{language}" \
    --body "$(cat <<'EOF'
<!-- metadata
type: queue
action: update
language: {language}
recipe: {recipe-path}
sdk-version: {tag}
reason: api-change
-->

## Recipe Needs Updating

**Recipe:** \`samples/{recipe-path}/\`
**SDK:** {repo}
**Release:** {tag} ({date})

## What Changed

{description of the API change from the release notes}

**Old pattern:**
\`\`\`
{old code pattern}
\`\`\`

**New pattern:**
\`\`\`
{new code pattern}
\`\`\`

## Files to Update

- \`samples/{recipe-path}/example.{ext}\`
- \`samples/{recipe-path}/README.md\` (update params table if needed)
EOF
)"
fi
```

---

## Step 9: Output Summary

```
=== SDK change review complete ===
Date: {TODAY}
Window: last 60 days ({SINCE} → {TODAY})

SDKs reviewed: {N}
Releases analysed: {total count}

New features found: {N}
  - Added to features.json: {list}
  - queue:generate issues created: {N}

Stale recipes found: {N}
  - queue:update issues created: {N}
  - Recipes affected: {list}

Features.json PR: {url or "none"}
```

---

## Safety Rules

- Never commit directly to main
- Never overwrite existing features.json entries (only ADD new ones)
- Never create duplicate queue issues (always check first)
- If you cannot parse a release body, skip it and log a warning
- Keep changes atomic: one PR per features.json update
