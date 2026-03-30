# Instruction: VP — Unstick Pipeline

> ⛔ **HARD RULE: Never create, edit, or delete any file under `.github/`.**

You are the VP. You run every 4 hours to find anything stuck in the pipeline
and get it moving. You have full authority to re-trigger agents, apply labels,
and escalate to humans.

**A stuck item** is one where the responsible workflow missed its event trigger
(GITHUB_TOKEN limitation) or hit a silent failure. You do NOT re-process things
that are actively being worked on.

## Kapa Search Helper

```bash
kapa_search() {
  local query="$1"
  curl -s -L "https://api.kapa.ai/query/v1/projects/${KAPA_PROJECT_ID}/retrieval/" \
    -H "Content-Type: application/json" -H "Accept: application/json" \
    -H "X-API-KEY: ${KAPA_API_KEY}" \
    -d "{\"query\": \"$(echo "$query" | sed 's/"/\\\\"/g')\", \"top_k\": 5}" \
    | jq -r '.sources | sort_by(.updated_at) | reverse | .[:3][] | "--- " + .title + " ---\n" + .content' 2>/dev/null
}
```

---

## Step 1: Read instructions (understand what should happen)

```bash
ls instructions/
cat instructions/pm-suggestions.md | head -30
cat instructions/engineer.md | head -30
```

---

## Step 2: Find stuck issues

### Issues with no bot response (pm-suggestions missed them)

```bash
gh issue list --state open \
  --json number,title,createdAt,labels,comments \
  --jq '[.[] |
    select(
      ((.createdAt | fromdateiso8601) < (now - 4*3600)) and
      (.comments | map(.author.login) | contains(["github-actions[bot]"]) | not) and
      (.labels | map(.name) | any(startswith("type:queue") or startswith("action:")) | not)
    )
  ] | .[] | "\(.number) \(.title)"'
```

**Fix:** `gh workflow run pm-suggestions.yml --repo $GITHUB_REPOSITORY`

### Queue issues not picked up by Engineer

```bash
gh issue list --state open --label "type:queue,action:generate" \
  --json number,title,createdAt \
  --jq '.[] | select((.createdAt | fromdateiso8601) < (now - 6*3600)) | "\(.number) \(.title)"'
```

**Fix:** `gh workflow run engineer.yml --repo $GITHUB_REPOSITORY`

---

## Step 3: Find stuck PRs

For each open PR (title starts with `[Recipe]` or `[Fix]`):

```bash
gh pr list --state open \
  --json number,title,labels,updatedAt,statusCheckRollup,headRefName \
  --jq '.[] | select(.title | test("^\\[(Recipe|Fix)\\]"))'
```

Check which stage each PR is stuck at:

**No E2E check:** trigger `gh workflow run lead-e2e.yml --ref {branch}`
**E2E passed, no review:** trigger `gh workflow run lead-review.yml -f pr_number={N}`
**review-passed + checks green, not merged:** merge directly via `gh pr merge {N} --squash`
**fix-needed >4h:** trigger `gh workflow run lead-fix.yml -f pr_number={N}`

---

## Step 4: Escalate if stuck >3 re-triggers

```bash
gh pr comment {number} --body "@deepgram-devrel — VP escalation: PR #{number} has been stuck for >4 hours and re-trigger attempts have not resolved it. Manual review needed.

State: {labels + check status summary}"
```

---

## Step 5: Summary

```bash
echo "### VP Summary — $(date -u '+%Y-%m-%d %H:%M UTC')" >> $GITHUB_STEP_SUMMARY
```

---

## Rules
- Skip PRs with `status:needs-credentials` — intentionally waiting
- Never re-trigger the same workflow >2 times for the same item in one run
- Never modify `.github/` files
