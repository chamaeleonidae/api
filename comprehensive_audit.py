#!/usr/bin/env python3
"""
Comprehensive audit of original vs migrated content
"""

import os
import re

def extract_files_from_sidebar():
    """Extract all file references from _sidebar.md"""
    with open('docs/_sidebar.md', 'r') as f:
        content = f.read()

    # Find all markdown links like [text](path.md)
    links = re.findall(r'\[([^\]]+)\]\(([^)]+\.md[^)]*)\)', content)
    files = []
    for title, path in links:
        # Remove any anchor references
        clean_path = path.split('?')[0].split('#')[0]
        files.append((title, clean_path))

    return files

def check_migrated_files():
    """Check which files have been migrated"""
    sidebar_files = extract_files_from_sidebar()

    print("=== COMPREHENSIVE MIGRATION AUDIT ===\n")

    missing_files = []
    found_files = []

    for title, orig_path in sidebar_files:
        # Expected migrated path
        if orig_path.startswith('apis/'):
            expected_path = orig_path.replace('apis/', 'api/').replace('.md', '.mdx')
        elif orig_path.startswith('concepts/'):
            expected_path = orig_path.replace('.md', '.mdx')
        elif orig_path.startswith('js/'):
            expected_path = orig_path.replace('.md', '.mdx')
        elif orig_path.startswith('webhooks/'):
            expected_path = orig_path.replace('.md', '.mdx')
        elif orig_path.startswith('guides/'):
            if 'installing-correctly' in orig_path:
                expected_path = 'guides/installation.mdx'
            elif 'user-generated-content' in orig_path:
                expected_path = 'guides/helpbar-user-content.mdx'
            else:
                expected_path = orig_path.replace('.md', '.mdx')
        else:
            # Root level files
            if 'authentication' in orig_path:
                expected_path = 'authentication.mdx'
            else:
                expected_path = orig_path.replace('.md', '.mdx')

        # Check if file exists
        if os.path.exists(expected_path):
            found_files.append((title, orig_path, expected_path))
            print(f"✅ {title}: {orig_path} → {expected_path}")
        else:
            missing_files.append((title, orig_path, expected_path))
            print(f"❌ MISSING: {title}: {orig_path} → {expected_path}")

    print(f"\n=== SUMMARY ===")
    print(f"✅ Found: {len(found_files)}")
    print(f"❌ Missing: {len(missing_files)}")

    if missing_files:
        print(f"\n=== CRITICAL GAPS ===")
        for title, orig_path, expected_path in missing_files:
            if os.path.exists(orig_path):
                with open(orig_path, 'r') as f:
                    lines = len(f.readlines())
                print(f"• {title} ({lines} lines): {orig_path}")
            else:
                print(f"• {title}: {orig_path} (original not found)")

if __name__ == "__main__":
    check_migrated_files()