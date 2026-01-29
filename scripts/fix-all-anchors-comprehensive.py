#!/usr/bin/env python3

import re
from pathlib import Path
from collections import defaultdict

def get_docsify_anchor_mappings(docsify_file):
    """Extract anchor ID mappings from original Docsify file"""
    if not docsify_file.exists():
        return {}

    mappings = {}
    with open(docsify_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Look for patterns like: ## Heading :id=anchor-id
            match = re.match(r'^(#{1,6})\s+(.+?)\s+:id=([a-z0-9-_]+)\s*$', line)
            if match:
                heading = match.group(1) + ' ' + match.group(2).strip()
                anchor_id = match.group(3)
                mappings[heading] = anchor_id

    return mappings

def add_anchors_to_file(mdx_file, docsify_file):
    """Add HTML anchor tags to MDX file based on Docsify mappings"""
    mappings = get_docsify_anchor_mappings(docsify_file)

    if not mappings:
        return False, 0

    with open(mdx_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified = False
    added_count = 0
    new_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]
        line_stripped = line.strip()

        # Check if this line matches a heading that needs an anchor
        if line_stripped in mappings:
            anchor_id = mappings[line_stripped]
            # Check if there's already an anchor on the previous line
            if i > 0 and '<a id=' in new_lines[-1]:
                # Already has an anchor, skip
                new_lines.append(line)
            else:
                # Add the anchor
                new_lines.append(f'<a id="{anchor_id}"></a>\n')
                new_lines.append(line)
                modified = True
                added_count += 1
        else:
            new_lines.append(line)

        i += 1

    if modified:
        with open(mdx_file, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

    return modified, added_count

def main():
    docs_dir = Path('/Users/maxwellrand/Desktop/Chameleon/dev/api/mintlify-docs')
    docsify_dir = Path('/Users/maxwellrand/Desktop/Chameleon/dev/api/docs')

    print("Processing all files to add missing anchor tags...\n")

    total_files = 0
    total_anchors = 0

    for mdx_file in sorted(docs_dir.rglob('*.mdx')):
        # Find corresponding Docsify file
        relative_path = mdx_file.relative_to(docs_dir)
        docsify_file = docsify_dir / str(relative_path).replace('.mdx', '.md')

        if docsify_file.exists():
            modified, count = add_anchors_to_file(mdx_file, docsify_file)
            if modified:
                print(f"✅ {relative_path}: Added {count} anchor tags")
                total_files += 1
                total_anchors += count

    print(f"\n{'='*60}")
    print(f"Processed {total_files} files")
    print(f"Added {total_anchors} anchor tags total")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
