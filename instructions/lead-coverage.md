# Instruction: PM — Documentation Sweep

You are the PM sweeping documentation up to date after recipes have merged.
Run on a cron. Scan the current state of `recipes/`, update all documentation,
and open (or update) a single PR.

**One open PR at a time.** Always use branch `pm/docs`. If it already exists on
origin, force-push to it — GitHub updates the open PR automatically. This means
however many times this cron runs, there is never more than one docs PR open.

---

## Step 1: Reset to a clean pm/docs branch

```bash
git fetch origin
git checkout main
git pull origin main

# Create (or hard-reset) pm/docs on top of latest main
git checkout -B pm/docs
```

---

## Step 2: Rebuild the coverage matrix in README.md

Run this Python script to regenerate the table between the README markers:

```python
import json, os, re, subprocess
from datetime import datetime, timezone

features = json.load(open('.deepgram/features.json'))
expected = {}
for product_slug, product in features['products'].items():
    for version, vdata in product['versions'].items():
        expected[(product_slug, version)] = len(vdata['recipes'])

langs = ['python','javascript','go','dotnet','java','rust','cli']
lang_display = {
    'python':'Python','javascript':'JavaScript','go':'Go',
    'dotnet':'.NET','java':'Java','rust':'Rust','cli':'CLI'
}

actual = {}
result = subprocess.run(
    ['find','recipes','-name','README.md','-mindepth','5','-maxdepth','5'],
    capture_output=True, text=True)
for path in result.stdout.strip().split('\n'):
    if not path: continue
    parts = os.path.dirname(path).split('/')
    if len(parts) != 5: continue
    _, lang, product, version, _ = parts
    key = (lang, product, version)
    actual[key] = actual.get(key, 0) + 1

def test_status(lang):
    r = subprocess.run(
        ['gh','run','list','--repo','deepgram/recipes',
         '--workflow',f'lead-test-{lang}.yml','--branch','main',
         '--limit','1','--json','conclusion','--jq','.[0].conclusion'],
        capture_output=True, text=True, timeout=10)
    c = r.stdout.strip().strip('"')
    return {'success':'✅','failure':'❌'}.get(c,'—')

lang_tests = {l: test_status(l) for l in langs}

def cell(lang, product, version):
    got = actual.get((lang, product, version), 0)
    exp = expected.get((product, version), 0)
    if exp == 0: return '—'
    if got == exp: return '✅'
    if got == 0: return '❌'
    return f'{got}/{exp}'

now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
total_expected = sum(expected.values())
total_actual = {l: sum(actual.get((l,p,v),0) for (p,v) in expected) for l in langs}

header = '| | ' + ' | '.join(lang_display[l] for l in langs) + ' |'
sep    = '|---|' + '|'.join(['---']*len(langs)) + '|'
rows = [header, sep]

for product_slug, product in features['products'].items():
    for version, vdata in product['versions'].items():
        label = f"{product['name']} `{version}`"
        cells = [cell(l, product_slug, version) for l in langs]
        rows.append(f"| {label} | " + ' | '.join(cells) + ' |')

totals = [f"**{total_actual[l]}/{total_expected}**" for l in langs]
rows.append('| **Total** | ' + ' | '.join(totals) + ' |')
tests = [lang_tests[l] for l in langs]
rows.append('| **Tests** | ' + ' | '.join(tests) + ' |')

table = f"*Last updated {now}*\n\n" + '\n'.join(rows)

content = open('README.md').read()
new = re.sub(
    r'<!-- recipes-table-start -->.*?<!-- recipes-table-end -->',
    f'<!-- recipes-table-start -->\n{table}\n<!-- recipes-table-end -->',
    content, flags=re.DOTALL)
open('README.md','w').write(new)
print("README updated")
```

Run it:
```bash
python3 -c "$(cat the script above)"
```

---

## Step 3: Rebuild COVERAGE.md

Scan `recipes/` and write a full per-recipe coverage matrix to `COVERAGE.md`:

```bash
python3 << 'PYEOF'
import json, os, subprocess
from datetime import datetime, timezone

features = json.load(open('.deepgram/features.json'))
langs = ['python','javascript','go','dotnet','java','rust','cli']

result = subprocess.run(
    ['find','recipes','-name','README.md','-mindepth','5','-maxdepth','5'],
    capture_output=True, text=True)

covered = set()
for path in result.stdout.strip().split('\n'):
    if not path: continue
    parts = os.path.dirname(path).split('/')
    if len(parts) == 5:
        _, lang, product, version, slug = parts
        covered.add((lang, product, version, slug))

now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
lines = [f"# Coverage\n\n*Last updated {now}*\n"]

for product_slug, product in features['products'].items():
    for version, vdata in product['versions'].items():
        lines.append(f"\n## {product['name']} `{version}`\n")
        header = '| Recipe | ' + ' | '.join(l.capitalize() for l in langs) + ' |'
        sep = '|---|' + '|'.join(['---']*len(langs)) + '|'
        lines.append(header)
        lines.append(sep)
        for recipe in vdata['recipes']:
            slug = recipe['slug']
            cells = ['✅' if (l, product_slug, version, slug) in covered else '❌'
                     for l in langs]
            lines.append(f"| {slug} | " + ' | '.join(cells) + ' |')

open('COVERAGE.md', 'w').write('\n'.join(lines) + '\n')
print("COVERAGE.md updated")
PYEOF
```

---

## Step 4: Update per-language READMEs

For each language that has at least one recipe, create or update
`recipes/{language}/README.md` with a table of available recipes grouped by product:

```bash
python3 << 'PYEOF'
import json, os, subprocess

features = json.load(open('.deepgram/features.json'))
langs = ['python','javascript','go','dotnet','java','rust','cli']
lang_display = {
    'python':'Python','javascript':'JavaScript','go':'Go',
    'dotnet':'.NET','java':'Java','rust':'Rust','cli':'CLI'
}

result = subprocess.run(
    ['find','recipes','-name','README.md','-mindepth','5','-maxdepth','5'],
    capture_output=True, text=True)

covered = {}
for path in result.stdout.strip().split('\n'):
    if not path: continue
    parts = os.path.dirname(path).split('/')
    if len(parts) == 5:
        _, lang, product, version, slug = parts
        covered.setdefault(lang, {}).setdefault((product, version), []).append(slug)

for lang in langs:
    if lang not in covered:
        continue
    display = lang_display[lang]
    lines = [f"# {display} Recipes\n"]
    total = sum(len(v) for v in covered[lang].values())
    lines.append(f"{total} recipe(s) available.\n")
    for (product, version), slugs in sorted(covered[lang].items()):
        product_name = next(
            (p['name'] for p in features['products'].values() if
             next(iter(p['versions'])) == version or version in p['versions']),
            product)
        lines.append(f"\n## {product_name} `{version}`\n")
        for slug in sorted(slugs):
            path = f"recipes/{lang}/{product}/{version}/{slug}"
            lines.append(f"- [{slug}]({product}/{version}/{slug}/)")
    open(f"recipes/{lang}/README.md", 'w').write('\n'.join(lines) + '\n')
    print(f"Updated recipes/{lang}/README.md")
PYEOF
```

---

## Step 5: Check for changes

```bash
if git diff --quiet HEAD -- README.md COVERAGE.md recipes/*/README.md 2>/dev/null && \
   ! git ls-files --others --exclude-standard recipes/*/README.md 2>/dev/null | grep -q .; then
  echo "Documentation is already up to date — nothing to do."
  exit 0
fi
```

---

## Step 6: Commit

```bash
git add README.md COVERAGE.md recipes/*/README.md
git commit -m "docs: update coverage documentation"
```

---

## Step 7: Push and open or update the PR

Use a fixed branch name so there is never more than one open docs PR:

```bash
git push origin pm/docs --force

EXISTING=$(gh pr list --head pm/docs --state open --json number --jq '.[0].number // empty')

if [ -z "$EXISTING" ]; then
  PR_URL=$(gh pr create \
    --base main \
    --head pm/docs \
    --title "docs: update coverage documentation" \
    --label "type:docs" \
    --body "Automated documentation sweep — updates README coverage matrix, COVERAGE.md, and per-language READMEs to reflect the current state of \`recipes/\`.")
  gh pr merge "$PR_URL" --auto --squash
  echo "Opened new docs PR: $PR_URL"
else
  echo "Updated existing PR #$EXISTING with latest docs state."
fi

# Always re-trigger E2E on the branch (required check for merge)
gh workflow run lead-e2e.yml --ref pm/docs
```

---

## Safety Rules

- Only modify: `README.md`, `COVERAGE.md`, `recipes/{language}/README.md`
- Never touch recipe code files (`example.*`, `example_test.*`)
- Never commit directly to `main`
- If any script step fails, output the error and continue — do not abort entirely
