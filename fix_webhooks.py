#!/usr/bin/env python3
"""
Fix webhook content by migrating the CORRECT webhook documentation
"""

import os
import re

def clean_content(content):
    """Clean Docsify-specific syntax from content"""

    # Remove Docsify :id= anchors
    content = re.sub(r' :id=[a-zA-Z0-9\\-_]+', '', content)

    # Fix internal links - remove .md extensions for Mintlify
    content = re.sub(r'\\]\\(([^)]+)\\.md\\)', r'](\\1)', content)

    # Fix relative paths for new structure
    content = content.replace('(apis/', '(/api/')
    content = content.replace('(concepts/', '(/concepts/')
    content = content.replace('(webhooks/', '(/webhooks/')
    content = content.replace('(js/', '(/js/')
    content = content.replace('(guides/', '(/guides/')

    # Remove page-level headers (since Mintlify provides page titles)
    lines = content.split('\\n')
    if lines and lines[0].startswith('# '):
        # Find the next non-empty line after the title
        start_idx = 1
        while start_idx < len(lines) and lines[start_idx].strip() == '':
            start_idx += 1

        # If there's a bold description right after, keep it but make it normal
        if start_idx < len(lines) and lines[start_idx].startswith('**') and lines[start_idx].endswith('**'):
            lines[start_idx] = lines[start_idx][2:-2]  # Remove ** **

        content = '\\n'.join(lines[start_idx:])

    return content

def main():
    # Read the original webhook overview file
    with open('docs/webhooks/overview.md', 'r', encoding='utf-8') as f:
        original_content = f.read()

    # Clean the content
    cleaned_content = clean_content(original_content)

    # Write to the correct location
    with open('webhooks/overview.mdx', 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

    print("✅ Fixed webhooks/overview.mdx with correct outgoing webhook documentation")

if __name__ == "__main__":
    main()