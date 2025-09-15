#!/usr/bin/env python3
"""
Comprehensive fix for all broken anchor links in the migrated documentation
This addresses the systematic failure in link cleaning during migration
"""

import os
import re
import glob

def get_path_mapping():
    """Define the path mappings for link fixes"""
    return {
        'apis/': '/api/',
        'concepts/': '/concepts/',
        'webhooks/': '/webhooks/',
        'js/': '/js/',
        'guides/': '/guides/',
        'guides/js/installing-correctly': '/guides/installation',
        'guides/helpbar/user-generated-content': '/guides/helpbar-user-content',
        'concepts/authentication': '/authentication',
        'apis/translation': '/concepts/localization',  # Special case
    }

def fix_anchor_links(content, current_file_path):
    """Fix all broken anchor links in content"""

    path_mapping = get_path_mapping()

    # Pattern to match links like [text](path.md?id=anchor) or [text](path.md#anchor)
    link_pattern = r'\[([^\]]+)\]\(([^)]+\.md)(\?id=|#)([^)]+)\)'

    def replace_link(match):
        link_text = match.group(1)
        file_path = match.group(2)
        separator = match.group(3)  # ?id= or #
        anchor = match.group(4)

        # Remove .md extension
        clean_path = file_path.replace('.md', '')

        # Check if this is a self-reference (same page)
        current_page = current_file_path.replace('.mdx', '').replace('/', '')
        target_page = clean_path.split('/')[-1]

        # If it's the same page, make it an on-page anchor
        if (current_page == target_page or
            (current_file_path == 'concepts/personalizing.mdx' and 'personalizing' in clean_path) or
            (current_file_path == 'guides/helpbar-user-content.mdx' and 'user-generated-content' in clean_path)):
            return f'[{link_text}](#{anchor})'

        # Apply path mapping for cross-page links
        new_path = clean_path
        for old_prefix, new_prefix in path_mapping.items():
            if clean_path.startswith(old_prefix):
                new_path = clean_path.replace(old_prefix, new_prefix, 1)
                break

        # Return fixed cross-page link
        return f'[{link_text}]({new_path}#{anchor})'

    # Apply the fixes
    fixed_content = re.sub(link_pattern, replace_link, content)

    return fixed_content

def fix_file(file_path):
    """Fix anchor links in a single file"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_links = len(re.findall(r'\.md\?id=', content))
    if original_links == 0:
        return 0  # No links to fix

    fixed_content = fix_anchor_links(content, file_path)
    fixed_links = len(re.findall(r'\.md\?id=', fixed_content))

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)

    links_fixed = original_links - fixed_links
    if links_fixed > 0:
        print(f"✅ {file_path}: Fixed {links_fixed} anchor links")

    return links_fixed

def main():
    """Fix all anchor links across all .mdx files"""

    print("🔗 COMPREHENSIVE ANCHOR LINK FIX")
    print("=" * 50)

    # Find all .mdx files
    mdx_files = []
    for pattern in ['*.mdx', '*/*.mdx', '*/*/*.mdx']:
        mdx_files.extend(glob.glob(pattern))

    # Remove any files in node_modules or other irrelevant directories
    mdx_files = [f for f in mdx_files if 'node_modules' not in f]
    mdx_files.sort()

    total_fixed = 0
    files_fixed = 0

    for file_path in mdx_files:
        if os.path.exists(file_path):
            links_fixed = fix_file(file_path)
            if links_fixed > 0:
                files_fixed += 1
                total_fixed += links_fixed

    print(f"\n📊 SUMMARY:")
    print(f"✅ Files processed: {len(mdx_files)}")
    print(f"✅ Files with fixes: {files_fixed}")
    print(f"✅ Total links fixed: {total_fixed}")

    # Check for remaining issues
    remaining_issues = 0
    for file_path in mdx_files:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
                remaining = len(re.findall(r'\.md\?id=', content))
                if remaining > 0:
                    remaining_issues += remaining
                    print(f"⚠️  {file_path}: {remaining} links still need manual review")

    if remaining_issues == 0:
        print(f"\n🎉 SUCCESS: All anchor links fixed!")
    else:
        print(f"\n⚠️  {remaining_issues} links need manual review")

    return remaining_issues == 0

if __name__ == "__main__":
    main()