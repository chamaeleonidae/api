#!/usr/bin/env python3

import re
from pathlib import Path

def check_for_duplicate(file_path):
    """Check if first content paragraph is similar to description"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get content after frontmatter
    frontmatter_end = re.search(r'^---\n\n', content, re.MULTILINE)
    if not frontmatter_end:
        return None

    after_frontmatter = content[frontmatter_end.end():]

    # Check for bold paragraph at start (with or without extra text)
    bold_match = re.match(r'\*\*(.+?)\*\*(.*)?\n', after_frontmatter, re.DOTALL)
    if bold_match:
        bold_text = bold_match.group(0).strip()
        return ('bold', bold_text[:150])

    # Check for regular paragraph that might be duplicate
    para_match = re.match(r'^([A-Z][^\n]+?)\.\s*\n', after_frontmatter)
    if para_match:
        para_text = para_match.group(1)
        # Get description
        desc_match = re.search(r'^description:\s*["\'](.+?)["\']', content, re.MULTILINE | re.DOTALL)
        if desc_match:
            description = desc_match.group(1).strip()
            # Clean both for comparison
            clean_desc = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', description)
            clean_desc = re.sub(r'\s+', ' ', clean_desc).strip()[:80]
            clean_para = re.sub(r'\s+', ' ', para_text).strip()[:80]

            if clean_para.lower() == clean_desc.lower():
                return ('paragraph', para_text[:150])

    return None

def main():
    docs_dir = Path('/Users/maxwellrand/Desktop/Chameleon/dev/api/mintlify-docs')

    print("Checking for remaining duplicate introductions...\n")

    issues = []

    for mdx_file in docs_dir.rglob('*.mdx'):
        result = check_for_duplicate(mdx_file)
        if result:
            issue_type, text = result
            issues.append((mdx_file.relative_to(docs_dir), issue_type, text))

    if issues:
        print(f"Found {len(issues)} files with potential duplicates:\n")
        for file, issue_type, text in issues:
            print(f"❌ {file} ({issue_type})")
            print(f"   {text}...")
            print()
    else:
        print("✅ No duplicates found!")

if __name__ == '__main__':
    main()
