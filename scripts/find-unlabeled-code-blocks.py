#!/usr/bin/env python3

import re
from pathlib import Path

def find_unlabeled_code_blocks(file_path):
    """Find code blocks without language identifiers"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    issues = []
    for i, line in enumerate(lines, 1):
        # Find code blocks that start with just ``` and nothing else (or only whitespace)
        if re.match(r'^```\s*$', line):
            # Get a preview of the next line for context
            preview = lines[i].strip()[:60] if i < len(lines) else ""
            issues.append((i, preview))

    return issues

def main():
    docs_dir = Path('/Users/maxwellrand/Desktop/Chameleon/dev/api/mintlify-docs')

    print("Finding code blocks without language identifiers...\n")

    all_issues = []

    for mdx_file in sorted(docs_dir.rglob('*.mdx')):
        issues = find_unlabeled_code_blocks(mdx_file)
        if issues:
            all_issues.append((mdx_file.relative_to(docs_dir), issues))

    if all_issues:
        print(f"Found {sum(len(issues) for _, issues in all_issues)} unlabeled code blocks in {len(all_issues)} files:\n")
        for file, issues in all_issues:
            print(f"\n{file}:")
            for line_num, preview in issues[:5]:  # Show first 5 per file
                print(f"  Line {line_num}: {preview}")
            if len(issues) > 5:
                print(f"  ... and {len(issues) - 5} more")
    else:
        print("✅ No unlabeled code blocks found!")

if __name__ == '__main__':
    main()
