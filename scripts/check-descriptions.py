#!/usr/bin/env python3

import re
from pathlib import Path

def check_description(file_path):
    """Check if description ends cleanly"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract description from frontmatter
    desc_match = re.search(r'^description:\s*["\'](.+?)["\']', content, re.MULTILINE)
    if not desc_match:
        return None

    description = desc_match.group(1)

    # Check if it ends badly (mid-word, incomplete)
    # Good endings: . ! ? " ) or complete word
    # Bad endings: single letter, incomplete word
    if description.endswith(('ti', 'ta', 'te', 'to', 'si', 'sa', 'se', 'so',
                            'ri', 'ra', 're', 'ro', 'ni', 'na', 'ne', 'no',
                            'li', 'la', 'le', 'lo', 'ci', 'ca', 'ce', 'co',
                            ' d', ' s', ' a', ' t', ' w', ' h', ' m')):
        return description

    return None

def main():
    docs_dir = Path('/Users/maxwellrand/Desktop/Chameleon/dev/api/mintlify-docs')

    print("Checking for potentially cut-off descriptions...\n")

    issues = []

    for mdx_file in docs_dir.rglob('*.mdx'):
        bad_desc = check_description(mdx_file)
        if bad_desc:
            issues.append((mdx_file.relative_to(docs_dir), bad_desc))

    if issues:
        print(f"Found {len(issues)} files with potentially cut-off descriptions:\n")
        for file, desc in issues:
            print(f"❌ {file}")
            print(f"   \"{desc}\"")
            print()
    else:
        print("✅ All descriptions look good!")

if __name__ == '__main__':
    main()
