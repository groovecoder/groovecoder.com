#!/usr/bin/env bash
# link-checker.sh — Check for broken internal links after build
set -euo pipefail

SITE_DIR="${1:-_site}"

if [[ ! -d "$SITE_DIR" ]]; then
    echo "Error: site directory '$SITE_DIR' not found. Run jekyll build first."
    exit 1
fi

broken=0
total=0

for html in $(find "$SITE_DIR" -name '*.html' -type f); do
    # Extract internal href values
    hrefs=$(grep -oP 'href="(/[^"]*)"' "$html" | grep -oP '"/[^"]*"' | tr -d '"' || true)

    for href in $hrefs; do
        total=$((total + 1))
        # Strip anchor
        path="${href%%#*}"

        # Check if file exists
        target="$SITE_DIR$path"
        if [[ "$path" == */ ]]; then
            target="${target}index.html"
        fi

        if [[ ! -f "$target" && ! -f "${target}.html" ]]; then
            echo "BROKEN: $href (in $(basename "$html"))"
            broken=$((broken + 1))
        fi
    done
done

echo ""
echo "Checked $total internal links, found $broken broken."

if [[ $broken -gt 0 ]]; then
    exit 1
fi
