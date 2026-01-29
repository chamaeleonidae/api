#!/bin/bash

# Remove duplicate H1 headers that match the frontmatter title
# This fixes the issue where Mintlify shows both the frontmatter title and the H1

DOCS_DIR="/Users/maxwellrand/Desktop/Chameleon/dev/api/mintlify-docs"

echo "Removing duplicate headers from all MDX files..."
echo ""

count=0

# Find all .mdx files
find "$DOCS_DIR" -name "*.mdx" -type f | while read -r file; do
  # Extract title from frontmatter (line 2)
  title=$(sed -n '2p' "$file" | sed 's/title: "//g' | sed 's/"//g')

  if [ -n "$title" ]; then
    # Check if there's a matching H1 after the frontmatter
    # Look for lines like: # Title or # Title followed by description

    # Remove the H1 if it exists (between lines 5-10 typically)
    # Use perl for more precise multiline editing
    perl -i -0pe "s/---\n\n# \Q$title\E\n\n/---\n\n/g" "$file"
    perl -i -0pe "s/---\n\n# \Q$title\E\n/---\n\n/g" "$file"

    echo "✓ Processed: $(basename "$file")"
    ((count++))
  fi
done

echo ""
echo "Processed $count files"
