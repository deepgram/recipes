# Instruction: Consolidate Test Workflows

> ⛔ Never modify `.github/` directly — open a PR.

The `deepgram/examples` repo has a single `test-examples.yml` workflow that
runs per-language test jobs in parallel, skipping jobs with no changed files.
Recipes needs the same pattern to get a reliable `e2e-api-check` for auto-merge.

## Step 1 — Fetch the reference workflow

```bash
curl -s https://raw.githubusercontent.com/deepgram/examples/main/.github/workflows/test-examples.yml \
  -o /tmp/test-examples-reference.yml
cat /tmp/test-examples-reference.yml
```

## Step 2 — Adapt for recipes structure

Key differences from examples:
- **Directory structure**: `recipes/{language}/{product}/{version}/{slug}/` not `examples/{NNN}-{slug}/`
- **Language marker**: each language dir already IS the language (no need to detect from files)
- **No credentials per example**: recipes only need `DEEPGRAM_API_KEY`
- **Test commands**: `pytest`, `node --test`, `go test`, `cargo test`, `dotnet test`, `bash example_test.sh`

The detect job should find changed recipe directories:
```bash
if [ "$EVENT" = "pull_request" ]; then
  DIRS=$(git diff origin/main...HEAD --name-only | grep '^recipes/' | cut -d/ -f1-2 | sort -u)
else
  DIRS=$(ls -d recipes/*/ | sed 's|/$||')
fi
# DIRS will be like: recipes/python, recipes/javascript, recipes/go ...
# Language is just the directory name
```

For recipes, each language directory contains all recipes for that language.
A changed `recipes/python/...` file means the python job runs; nothing else.

## Step 3 — Create the workflow as a PR

```bash
BRANCH="chore/consolidate-test-workflows"
git checkout -b "$BRANCH"
# Write the adapted workflow to .github/workflows/test-recipes.yml
# (keep existing lead-test-*.yml files until this is verified working)
git add .github/workflows/test-recipes.yml
git commit -m "feat(workflows): add consolidated test-recipes.yml with e2e-api-check"
git push origin "$BRANCH"
gh pr create --title "chore: consolidate test workflows with e2e-api-check gate" \
  --body "Adds test-recipes.yml mirroring deepgram/examples pattern.
  Once verified, the individual lead-test-*.yml files can be removed." \
  --base main --head "$BRANCH"
```

## Step 4 — Update branch protection / ruleset

After the PR is merged, add `e2e-api-check` as the required status check
in the repo ruleset so PRs auto-merge when tests pass.
