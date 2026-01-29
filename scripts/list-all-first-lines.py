#!/usr/bin/env python3

import re
from pathlib import Path

def get_first_content_line(file_path):
    """Get the first line of content after frontmatter"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get description
    desc_match = re.search(r'^description:\s*["\'](.+?)["\']', content, re.MULTILINE | re.DOTALL)
    description = desc_match.group(1).strip() if desc_match else None

    # Get content after frontmatter
    frontmatter_end = re.search(r'^---\n\n', content, re.MULTILINE)
    if not frontmatter_end:
        return None, None

    after_fm = content[frontmatter_end.end():]

    # Get first line (skip blank lines)
    lines = after_fm.split('\n')
    first_line = None
    for line in lines:
        if line.strip() and not line.strip().startswith('---'):
            first_line = line.strip()
            break

    return description, first_line

def main():
    docs_dir = Path('/Users/maxwellrand/Desktop/Chameleon/dev/api/mintlify-docs')

    print("Listing first content line for all files:\n")

    for mdx_file in sorted(docs_dir.rglob('*.mdx')):
        description, first_line = get_first_content_line(mdx_file)

        if description and first_line:
            # Clean both for comparison
            clean_desc = re.sub(r'[*"\']', '', description).strip().lower()
            clean_first = re.sub(r'[*"\']', '', first_line).strip().lower()

            # Check if they overlap significantly (more than 30 chars in common)
            is_similar = False
            if len(clean_desc) > 30 and len(clean_first) > 30:
                if clean_first[:40] in clean_desc or clean_desc[:40] in clean_first:
                    is_similar = True

            # Only show potential duplicates
            if is_similar and not first_line.startswith('#') and not first_line.startswith('-') and not first_line.startswith('>'):
                print(f"\n❌ {mdx_file.relative_to(docs_dir)}")
                print(f"   DESC: {description[:100]}")
                print(f"   FIRST: {first_line[:100]}")

if __name__ == '__main__':
    main()
