#!/usr/bin/env python3

import re
from pathlib import Path

def check_for_duplicate(file_path):
    """Check if first content paragraph (after blank lines) duplicates description"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract description from frontmatter
    desc_match = re.search(r'^description:\s*["\'](.+?)["\']', content, re.MULTILINE | re.DOTALL)
    if not desc_match:
        return None

    description = desc_match.group(1).strip()

    # Get content after frontmatter
    frontmatter_end = re.search(r'^---\n\n', content, re.MULTILINE)
    if not frontmatter_end:
        return None

    after_frontmatter = content[frontmatter_end.end():]

    # Skip any leading blank lines
    after_frontmatter = after_frontmatter.lstrip('\n')

    # Check for bold paragraph
    bold_match = re.match(r'\*\*(.+?)\*\*[^\n]*\n', after_frontmatter, re.DOTALL)
    if bold_match:
        bold_text = bold_match.group(0).strip()
        # Clean for comparison
        clean_bold = re.sub(r'\*\*', '', bold_text)
        clean_bold = re.sub(r'\s+', ' ', clean_bold).strip()
        clean_desc = re.sub(r'\s+', ' ', description).strip()

        # Check if they're similar (allowing for minor variations)
        if clean_bold[:100].lower() in clean_desc.lower() or clean_desc.lower() in clean_bold[:100].lower():
            return ('bold', bold_text[:150])

    # Check for regular paragraph (before any list, heading, or code block)
    para_match = re.match(r'^([A-Z][^\n]+?)[.!?]\s*\n', after_frontmatter)
    if para_match:
        para_text = para_match.group(1).strip()
        # Clean for comparison
        clean_para = re.sub(r'\s+', ' ', para_text).strip()
        clean_desc = re.sub(r'\s+', ' ', description).strip()

        # Check if they match (exact or very similar)
        if clean_para.lower() == clean_desc.lower():
            return ('exact', para_text[:150])
        elif clean_para[:80].lower() == clean_desc[:80].lower():
            return ('similar', para_text[:150])

    return None

def main():
    docs_dir = Path('/Users/maxwellrand/Desktop/Chameleon/dev/api/mintlify-docs')

    print("Comprehensive check for duplicate introductions...\n")

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
