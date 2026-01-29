#!/usr/bin/env python3

import os
import re
from pathlib import Path

def remove_duplicate_header(file_path):
    """Remove H1 header that duplicates the frontmatter title"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title from frontmatter
    title_match = re.search(r'^title:\s*["\'](.+?)["\']', content, re.MULTILINE)
    if not title_match:
        return False

    title = title_match.group(1)

    # Look for H1 that matches the title (after frontmatter end)
    # Pattern: ---\n\n# Title\n or ---\n\n# Title\n\n
    pattern1 = re.compile(r'^---\n\n#\s+' + re.escape(title) + r'\n\n', re.MULTILINE)
    pattern2 = re.compile(r'^---\n\n#\s+' + re.escape(title) + r'\n', re.MULTILINE)

    new_content = content
    changed = False

    # Try to remove "---\n\n# Title\n\n"
    if pattern1.search(new_content):
        new_content = pattern1.sub('---\n\n', new_content)
        changed = True
    # Try to remove "---\n\n# Title\n"
    elif pattern2.search(new_content):
        new_content = pattern2.sub('---\n\n', new_content)
        changed = True

    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    return False

def main():
    docs_dir = Path('/Users/maxwellrand/Desktop/Chameleon/dev/api/mintlify-docs')

    print("Removing duplicate headers from all MDX files...\n")

    count = 0
    fixed = 0

    for mdx_file in docs_dir.rglob('*.mdx'):
        count += 1
        if remove_duplicate_header(mdx_file):
            print(f"✓ Fixed: {mdx_file.relative_to(docs_dir)}")
            fixed += 1

    print(f"\nProcessed {count} files, fixed {fixed} files")

if __name__ == '__main__':
    main()
