#!/usr/bin/env python3

import re
from pathlib import Path

def remove_bold_intro(file_path):
    """Remove any bold paragraph at the start of content"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get content after frontmatter
    frontmatter_match = re.match(r'^---\n.+?\n---\n\n', content, re.DOTALL)
    if not frontmatter_match:
        return False

    frontmatter = frontmatter_match.group(0)
    after_frontmatter = content[frontmatter_match.end():]

    # Remove bold paragraph at the very start (may span multiple lines)
    # Pattern: **text** potentially followed by more text on same line
    new_after = re.sub(r'^\*\*(.+?)\*\*[^\n]*\n+', '', after_frontmatter, count=1, flags=re.DOTALL)

    # If we removed something, save the file
    if new_after != after_frontmatter:
        new_content = frontmatter + new_after
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    return False

def main():
    docs_dir = Path('/Users/maxwellrand/Desktop/Chameleon/dev/api/mintlify-docs')

    print("Removing all bold intro paragraphs...\n")

    count = 0
    fixed = 0

    for mdx_file in docs_dir.rglob('*.mdx'):
        count += 1
        if remove_bold_intro(mdx_file):
            print(f"✓ Fixed: {mdx_file.relative_to(docs_dir)}")
            fixed += 1

    print(f"\nProcessed {count} files, removed bold intros from {fixed} files")

if __name__ == '__main__':
    main()
