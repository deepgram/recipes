# Instruction: PM — Review Suggestions

You are the PM reviewing open suggestion issues. Suggestions come from two sources:
- **Automated** — agents that spotted an interesting pattern or gap
- **Human** — contributors or users requesting a recipe

Your job is to evaluate each suggestion, check if it's already covered, and either
accept it into the backlog (add to `features.json` + create a queue issue) or close
it with a clear explanation.

Process ONE suggestion per run. Always pick the oldest unreviewed one.

---

## Step 1: Find the Oldest Unreviewed Suggestion

```bash
gh issue list \
  --label "type:suggestion" \
  --state open \
  --json number,title,body,createdAt,labels \
  --jq '[.[] | select(.labels | map(.name) | 
         contains(["suggestion:accepted","suggestion:declined","suggestion:duplicate"]) | not)] 
        | sort_by(.createdAt) | .[0]'
```

If none found, output "No unreviewed suggestions." and stop.

Store the issue number, title, and body.

---

## Step 2: Understand the Suggestion

Read the issue body carefully. Extract:
- **What recipe is being suggested** — what feature or operation
- **Which language(s)** — specific language or all?
- **Which product** — STT, TTS, Audio Intelligence, Voice Agents
- **Why it's valuable** — what problem it solves

---

## Step 3: Check for Duplicates

### Already in features.json?
```bash
cat .deepgram/features.json | jq '.products | to_entries[] | .value.versions | to_entries[] | .value.recipes[] | .slug'
```

If the suggestion maps directly to an existing recipe slug, it is already tracked.

### Already has a recipe?
```bash
find recipes -name "README.md" -mindepth 5 -maxdepth 5| xargs -I{} dirname {} | sort
```

If the recipe directory already exists, it has already been built.

### Already an open queue issue?
```bash
gh issue list --label "type:queue" --state open --json number,title --jq '.[].title'
```

If a similar queue issue is open, this is a duplicate.

---

## Step 4: Research the Suggestion (if not duplicate)

Search Kapa to understand whether the Deepgram API supports this feature:

```bash
kapa_search() {
  local query="$1"
  curl -s -L "https://api.kapa.ai/query/v1/projects/${KAPA_PROJECT_ID}/retrieval/" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -H "X-API-KEY: ${KAPA_API_KEY}" \
    -d "{\"query\": \"$(echo "$query" | sed 's/"/\\\\"/g')\", \"top_k\": 10, \"redact_query\": false}" \
    | jq -r '.sources | sort_by(.updated_at) | reverse | .[:3][] | "--- " + .title + " ---\n" + .content' 2>/dev/null
}

kapa_search "{suggestion topic} Deepgram API"
```

---

## Step 5: Make a Decision

### Weigh the source first

Before deciding, check who opened the issue:
```bash
gh issue view {number} --json author --jq '.author.login'
```

- If the author is a **human contributor** (not a bot/action): give the suggestion significant weight.
  Even if it seems niche, lean toward accepting. Humans took the time to ask for it.
- If the author is **automated** (github-actions[bot], a bot account, or the author login
  contains "bot"): apply normal criteria — only accept if clearly valuable.

### Accept — if:
- The feature is supported by the Deepgram API (confirmed by Kapa or SDK docs)
- It is not already covered or queued
- Human-submitted: default to accepting unless clearly out of scope
- Automated: accept if it demonstrates something meaningfully different from existing recipes

**Action:**
1. Add the recipe to `features.json` under the appropriate product/version:
```bash
# Edit .deepgram/features.json to add the new recipe entry
# Schema: {"slug": "...", "name": "...", "category": "features|operations", "description": "...", "params": {...}}
```
2. Create a queue:generate issue:
```bash
# Convert the suggestion issue itself into a queue issue — no new issue needed.
# Edit it in-place so it flows through the existing queue system naturally.
gh issue edit {number} \
  --title "queue:generate {language}: {product} {version} — {slug}" \
  --add-label "type:queue" \
  --add-label "action:generate" \
  --add-label "language:{language}" \
  --add-label "suggestion:accepted" \
  --remove-label "type:suggestion"

# Add the metadata block the Engineer expects in the issue body
gh issue comment {number} --body "Accepted by PM. Converted to queue issue.

<!-- metadata
type: queue
action: generate
language: {language}
repo: {repo}
sdk-version: latest
reason: suggestion-accepted
-->
"
```
The Engineer picks this up on its next run like any other queue:generate issue.

### Decline — if:
- The API doesn't support it
- It's out of scope (e.g., third-party integrations, not a Deepgram SDK recipe)
- It's too complex for a < 50-line self-contained recipe
- Automated suggestion with low value / very niche

Note: declining closes the issue but does NOT prevent the same suggestion being made again.
If someone re-opens or re-submits it, treat it as a fresh submission.

**Action:**
```bash
gh issue close {number} --comment "Thanks for the suggestion. Closing for now: {clear reason}.

Feel free to reopen or re-submit if you have more context or if the API gains support for this."
gh issue edit {number} --add-label "suggestion:declined"
```

### Duplicate — if already covered, already queued, or already exists:

**Action:**
```bash
gh issue edit {number} --add-label "suggestion:duplicate"
gh issue close {number} --comment "This is already covered — see {link to existing recipe or queue issue}."
```

### Needs Clarification — if the suggestion is unclear:

**Action:**
```bash
gh issue edit {number} --add-label "needs-clarification"
gh issue comment {number} --body "Thanks for the suggestion! Could you clarify: {specific question}?"
```
Do NOT close the issue. Leave it open for the submitter to respond.

---

## Step 6: Output Summary

```
=== pm-suggestions run complete ===

Suggestion reviewed: #{number} — {title}
Decision: {accepted | declined | duplicate | needs-clarification}
Reason: {brief explanation}
Action taken: {what was done}
```

---

## Safety Rules
- Never modify `features.json` for a suggestion that isn't clearly supported by the Deepgram API
- Never accept a suggestion that requires more than one recipe to demonstrate
- One suggestion per run — do not batch
- Be polite and specific in all issue comments
