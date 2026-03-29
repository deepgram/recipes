# Instruction: Discover SDKs and Queue Missing Recipes

You are an autonomous agent maintaining a Deepgram code samples repository. Your job is to find
coverage gaps in `recipes/` and create GitHub Issues to queue generation of missing recipes.
You must also detect new Deepgram SDK repositories that are not yet tracked.

Work from the repository root. Be methodical, idempotent, and safe — never commit to main,
never create duplicate issues, never modify configuration files without human review.

---

## Step 1: Load the SDK Registry and Feature Map

Read both configuration files:

```bash
cat .deepgram/sdks.json
cat .deepgram/features.json
```

Parse `sdks.json` to get the list of tracked SDKs. Each entry has at minimum:
- `language` — the language slug (e.g., `python`, `javascript`, `go`)
- `slug` — the directory name under `recipes/` (usually same as language)
- `repo` — the GitHub repo in `owner/name` format (e.g., `deepgram/deepgram-python-sdk`)

Parse `features.json` to get ALL expected recipe paths. Each entry is a relative path like
`speech-to-text/v1/transcribe-url-nova3` representing
`{product}/{api-version}/{recipe-slug}`.

---

## Step 2: For Each SDK, Check the Latest Release Tag

For each SDK entry in sdks.json, fetch the latest release tag:

```bash
gh api "repos/{repo}/releases/latest" --jq '.tag_name' 2>/dev/null || \
  gh api "repos/{repo}/tags" --jq '.[0].name' 2>/dev/null || echo "unknown"
```

Replace `{repo}` with the actual repo value from sdks.json.

Store this as `latest_tag` for later use.

---

## Step 3: Check Existing Coverage for Each Language

For each SDK, find all recipe paths that already have an example file:

```bash
find "recipes/{slug}/" -name "example.*" ! -name "*_test*" ! -name "*.mod" 2>/dev/null | \
  sed "s|recipes/{slug}/||" | sed "s|/example.*||" | sort
```

Replace `{slug}` with the SDK's slug value.

This produces a list of paths like:
```
speech-to-text/v1/transcribe-url-nova3
speech-to-text/v1/smart-format
```

---

## Step 4: Build the List of Missing Recipe Paths

Compare the existing coverage list against ALL entries in features.json for the given language.

Features in features.json may be:
- Universal (apply to all languages) — include these for every language
- Language-specific — only include if they match the current language

A recipe path is MISSING if it appears in features.json (for this language) but does NOT
appear in the existing coverage list from Step 3.

Build a bullet list of missing paths for this language.

If there are zero missing paths for a language, skip to the next SDK.

---

## Step 5: Check for an Existing Open Queue Issue

Before creating any issue, check whether a `queue:generate` issue already exists for this
language:

```bash
gh issue list \
  --label "type:queue" \
  --label "action:generate" \
  --label "language:{slug}" \
  --state open \
  --json number,title --limit 5
```

If any issues are returned, log a message like:
```
[SKIP] Open queue issue already exists for {slug} (issue #{number}). Skipping.
```

Do NOT create a duplicate. Move on to the next SDK.

---

## Step 6: Create a Queue Issue for Missing Recipes

If missing recipes were found AND no open issue exists for this language, create a new issue:

```bash
gh issue create \
  --title "queue:generate {slug}: cover missing recipes" \
  --label "type:queue" \
  --label "action:generate" \
  --label "language:{slug}" \
  --body "$(cat <<'BODY'
<!-- metadata
type: queue
action: generate
language: {slug}
repo: {repo}
sdk-version: {latest_tag}
reason: coverage-gap
-->

## Missing Recipe Paths

{bullet list of missing paths, one per line starting with "- "}

## Context
- SDK: {repo}
- Latest release: {latest_tag}
- Triggered: {current date in YYYY-MM-DD format}
BODY
)"
```

Replace all `{placeholder}` values with actual data before running.

Log the created issue number.

---

## Step 7: Search for New Deepgram SDK Repos Not in sdks.json

Fetch all repositories from the Deepgram GitHub organization:

```bash
gh api "orgs/deepgram/repos?per_page=100" --paginate \
  --jq '.[] | select(.name | test("sdk$|^deepgram-cli$")) | .full_name'
```

This returns repos whose names end with `sdk` or are exactly `deepgram-cli`.

Extract the full list of repos currently tracked in sdks.json (the `repo` field of each entry).

For any repo returned by the API that is NOT present in sdks.json, create a `queue:new-sdk`
issue for human review:

```bash
gh issue create \
  --title "queue:new-sdk: {repo_name} discovered" \
  --label "type:queue" \
  --label "action:new-sdk" \
  --body "$(cat <<'BODY'
<!-- metadata
type: queue
action: new-sdk
repo: {full_repo_name}
-->

## New SDK Repository Discovered

A Deepgram SDK repository was found that is not currently tracked in `.deepgram/sdks.json`.

**Repository:** {full_repo_name}
**Discovered:** {current date}

## Action Required

This requires human review before the SDK can be added to the tracking system:

1. Verify this is an official Deepgram SDK (not a fork, demo, or archived repo)
2. Add an entry to `.deepgram/sdks.json` with the correct `language`, `slug`, and `repo` fields
3. Create a `recipes/{language}/` directory with an appropriate manifest file
4. Manually add a `test-{language}.yml` workflow by copying an existing one and adapting it
   NOTE: Workflow files CANNOT be created by agents — GITHUB_TOKEN lacks the `workflows`
   scope, and even if bypassed, workflow changes don't trigger CI until after they are merged.
   This step must be done by a human in a separate PR.
5. Close this issue once onboarding is complete

Do NOT auto-add this repository to sdks.json.
BODY
)"
```

Before creating, check if an open `action:new-sdk` issue already exists for this repo to
avoid duplicates:

```bash
gh issue list \
  --label "type:queue" \
  --label "action:new-sdk" \
  --state open \
  --json number,title --limit 20
```

Only create the issue if none of the existing titles mention this repo name.

---

## Step 8: Output a Summary

After processing all SDKs, print a summary report:

```
=== discover-sdks run complete ===

SDKs checked: {N}
Queue issues created: {N}
New SDK issues created: {N}
Languages already up to date: {list}
Errors/warnings: {list or "none"}
```

---

## Safety Rules

- NEVER commit directly to main or any branch.
- NEVER create duplicate queue issues — always check with `gh issue list` first.
- NEVER modify `.deepgram/sdks.json` or `.deepgram/features.json` — these require human review.
- NEVER modify any file in `recipes/` — this instruction is read-only for source files.
- If any single SDK check fails with an error, log a warning and continue to the next SDK.
  Do not abort the entire run because one SDK API call failed.
- If `gh` commands fail due to rate limiting, wait 10 seconds and retry once.
- If `.deepgram/sdks.json` or `.deepgram/features.json` do not exist, output an error and exit.
