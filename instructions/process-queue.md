# Instruction: Process Queue Issues

You are an autonomous agent that routes open GitHub queue issues to the appropriate handler.
Your job is to read the oldest open queue issue, determine what action it requires, and
either execute that action or surface it for human review.

---

## Step 1: List Open Queue Issues

Fetch all open queue issues, sorted by creation date (oldest first):

```bash
gh issue list \
  --label "type:queue" \
  --state open \
  --json number,title,labels,createdAt \
  --limit 10 \
  --jq 'sort_by(.createdAt)'
```

If no issues are returned, output:
```
No open queue issues found. Nothing to do.
```
And stop.

---

## Step 2: Determine the Action for the Oldest Issue

Take the FIRST (oldest) issue from the list.

Inspect its labels to determine the required action:

- If it has the label `action:generate` → proceed to **Step 3: Execute Generate**
- If it has the label `action:update`   → proceed to **Step 4: Execute Update**
- If it has the label `action:new-sdk`  → proceed to **Step 5: Surface New SDK for Review**
- If none of the above → output a warning and skip:
  ```
  [WARN] Issue #{number} has type:queue but no recognized action label. Skipping.
  ```

Only process ONE issue per run. This prevents runaway execution and keeps each run focused.

---

## Step 3: Execute Generate

Read and fully execute the instructions in `instructions/generate-examples.md`.

That instruction is self-contained. It will:
1. Find the triggering queue issue
2. Load SDK and feature configuration
3. Check existing coverage
4. Fetch SDK context
5. Create a feature branch
6. Generate all missing recipe files
7. Commit, push, and open a PR
8. Close the queue issue

After executing generate-examples.md, return here and output a summary of what was done.

---

## Step 4: Execute Update

Read and fully execute the instructions in `instructions/update-recipes.md`.

That instruction will:
1. Find the triggering queue:update issue
2. Read the recipe that needs updating
3. Fetch the SDK's new API patterns
4. Apply the changes and open a PR
5. Close the queue issue

After executing update-recipes.md, return here and output a summary of what was done.

---

## Step 5: Surface New SDK for Review

For `action:new-sdk` issues, do NOT auto-process. Instead, output a formatted summary for
the human who will review it:

```
=== New SDK Requires Human Review ===

Issue: #{number} — {title}
Created: {createdAt}

This issue was created because a new Deepgram SDK repository was discovered that is not
tracked in .deepgram/sdks.json.

To onboard this SDK:

1. Review the issue body for the repository name and language
2. Visit the GitHub repository and confirm it is an official Deepgram SDK
3. Edit .deepgram/sdks.json and add an entry:
   {
     "language": "{language}",
     "slug": "{language}",
     "repo": "{full_repo_name}",
     "manifest": "{appropriate manifest filename}"
   }
4. Create the recipes/{language}/ directory with an appropriate manifest file
5. Manually create a `test-{language}.yml` workflow — this CANNOT be done by an agent.
   Workflow files require the `workflows` GitHub token scope, which is not available to
   automated runs. The workflow also will not take effect until it is merged into main.
   A human must add this file via a separate PR.
6. Close the issue once onboarding is complete

No automated action has been taken. Human review is required.
===
```

Do not close the issue or add a comment — leave it for the human to handle.

---

## Step 5: Output a Summary

After processing, output a brief summary:

```
=== process-queue run complete ===

Issues checked: {N}
Action taken: {generate | review-required | skipped | none}
Issue processed: #{number} ({title})
Result: {brief description}
```
