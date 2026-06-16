#!/usr/bin/env bash
# Server-side corpus guard (CI). Same checks as the local hooks, but over a
# commit RANGE and independent of where the commit came from — phone git app,
# GitHub web editor, API, or any machine. Local hooks cannot cover those;
# this can.
#
# Usage: corpus-guard-ci.sh <base-sha> <head-sha>
# Exit:  0 = clean | 2 = placeholder/elision found | 3 = silent shrink (no placeholder)

set -u
base="$1"; head="$2"
RED=$'\033[1;31m'; NC=$'\033[0m'
ph=0; sh=0

prefix='^[^A-Za-z0-9]*'
phrases='(full new content would go here|content would go here but for brevity|rest of (the )?(file|chapter|content|sections?|document) (unchanged|here|omitted|follows)|\.\.\.[[:space:]]*\(?(rest|remainder|continued)|insert (full|the) (content|chapter) here|<full[_ ]content|TODO:[[:space:]]*(write|full|fill)|content omitted for brevity|truncated for brevity)'
re="${prefix}${phrases}"

# Placeholder check on the head version of each changed text file
while IFS= read -r f; do
    [[ -n "$f" ]] || continue
    case "$f" in .githooks/*) continue ;; esac
    if git show "${head}:$f" 2>/dev/null | grep -qEi "$re"; then
        echo "${RED}PLACEHOLDER:${NC} $f"
        git show "${head}:$f" 2>/dev/null | grep -nEi "$re" | sed 's/^/    /'
        ph=1
    fi
done < <(git diff --name-only --diff-filter=ACM "$base" "$head" -- '*.md' '*.markdown' '*.txt' '*.sql' '*.sh' '*.py' '*.js' 2>/dev/null)

# Shrink check, unless any commit message in the range opts out with REWRITE:
rewrite=0
git log --format=%s "${base}..${head}" 2>/dev/null | grep -qiE '^REWRITE:' && rewrite=1
if [[ "$rewrite" == "0" ]]; then
    while IFS= read -r f; do
        [[ -n "$f" ]] || continue
        old=$(git show "${base}:$f" 2>/dev/null | wc -l)
        new=$(git show "${head}:$f" 2>/dev/null | wc -l)
        [[ "$old" -ge 40 ]] || continue
        if (( new * 100 < old * 60 )); then
            echo "${RED}SHRINK:${NC} $f  ${old} -> ${new} lines (>40% loss)"
            sh=1
        fi
    done < <(git diff --name-only --diff-filter=ACM "$base" "$head" -- '*.md' '*.markdown' 2>/dev/null)
fi

[[ "$ph" == "1" ]] && exit 2
[[ "$sh" == "1" ]] && exit 3
exit 0
