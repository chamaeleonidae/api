#!/bin/bash

# Bulk migrate all markdown files from Docsify to Mintlify
# Usage: bash migrate-all.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCS_DIR="$SCRIPT_DIR/../docs"
OUTPUT_DIR="$SCRIPT_DIR/../mintlify-docs"
CONVERT_SCRIPT="$SCRIPT_DIR/convert-docsify-to-mintlify.js"

echo "Starting bulk migration from Docsify to Mintlify..."
echo ""

SUCCESS=0
FAILED=0

# Find all .md files excluding ones starting with _
while IFS= read -r -d '' input_file; do
  # Get relative path from docs directory
  rel_path="${input_file#$DOCS_DIR/}"

  # Handle README.md -> introduction.mdx
  if [[ "$(basename "$input_file")" == "README.md" ]]; then
    output_file="$OUTPUT_DIR/introduction.mdx"
  else
    # Change .md to .mdx and preserve directory structure
    output_file="$OUTPUT_DIR/${rel_path%.md}.mdx"
  fi

  # Convert the file
  if node "$CONVERT_SCRIPT" "$input_file" "$output_file"; then
    ((SUCCESS++))
  else
    ((FAILED++))
    echo "✗ Failed: $rel_path"
  fi
done < <(find "$DOCS_DIR" -name "*.md" -not -name "_*" -type f -print0)

echo ""
echo "============================================================"
echo "Migration complete: $SUCCESS files converted, $FAILED failed"
echo ""
echo "Next steps:"
echo "1. Update mint.json with complete navigation structure"
echo "2. Run: cd mintlify-docs && mintlify dev"
echo "3. Test all pages and links"

if [ $FAILED -gt 0 ]; then
  exit 1
fi
