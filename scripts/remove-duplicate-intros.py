#!/usr/bin/env python3

import re
from pathlib import Path

def remove_duplicate_intro(file_path):
    """Remove duplicate bold first paragraph that matches description"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract description from frontmatter
    desc_match = re.search(r'^description:\s*["\'](.+?)["\']', content, re.MULTILINE | re.DOTALL)
    if not desc_match:
        return False

    description = desc_match.group(1).strip()

    # Clean description for comparison (remove markdown links, normalize whitespace)
    clean_desc = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', description)
    clean_desc = re.sub(r'\s+', ' ', clean_desc).strip()

    # Look for bold paragraph after frontmatter that matches description
    # Pattern: ---\n\n**[text that matches description]**\n

    # Get content after frontmatter
    frontmatter_end = re.search(r'^---\n\n', content, re.MULTILINE)
    if not frontmatter_end:
        return False

    after_frontmatter = content[frontmatter_end.end():]

    # Check if starts with bold paragraph
    bold_match = re.match(r'\*\*(.+?)\*\*\n', after_frontmatter, re.DOTALL)
    if not bold_match:
        return False

    bold_text = bold_match.group(1).strip()
    clean_bold = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', bold_text)
    clean_bold = re.sub(r'\s+', ' ', clean_bold).strip()

    # Check if they match (or bold text starts with description)
    if clean_bold.startswith(clean_desc[:50]) or clean_desc.startswith(clean_bold[:50]):
        # Remove the duplicate bold paragraph
        new_after = re.sub(r'^\*\*.+?\*\*\n\n?', '', after_frontmatter, count=1, flags=re.DOTALL)
        new_content = content[:frontmatter_end.end()] + new_after

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    return False

def main():
    docs_dir = Path('/Users/maxwellrand/Desktop/Chameleon/dev/api/mintlify-docs')

    print("Removing duplicate intro paragraphs...\n")

    count = 0
    fixed = 0

    for mdx_file in docs_dir.rglob('*.mdx'):
        count += 1
        if remove_duplicate_intro(mdx_file):
            print(f"✓ Fixed: {mdx_file.relative_to(docs_dir)}")
            fixed += 1

    print(f"\nProcessed {count} files, removed duplicates from {fixed} files")

if __name__ == '__main__':
    main()
