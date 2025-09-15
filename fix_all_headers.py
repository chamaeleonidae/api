#!/usr/bin/env python3
"""
Fix all duplicate headers and formatting issues across entire documentation
"""

import os
import re
import glob

def fix_duplicate_headers(content, file_path):
    """Remove duplicate headers and fix bold text formatting"""

    lines = content.split('\n')
    if not lines:
        return content

    # Check if first line is a duplicate header (starts with # )
    if lines[0].startswith('# '):
        header_text = lines[0][2:].strip()  # Remove # and spaces

        # Find the next non-empty line after the header
        start_idx = 1
        while start_idx < len(lines) and lines[start_idx].strip() == '':
            start_idx += 1

        # Check if the next content line is bold version of the same header
        if start_idx < len(lines):
            next_line = lines[start_idx].strip()

            # If it's unnecessarily bold description, make it normal
            if next_line.startswith('**') and next_line.endswith('**'):
                # Remove the bold formatting
                lines[start_idx] = next_line[2:-2]

        # Remove the duplicate header and any empty lines after it
        # Keep content starting from the first meaningful line
        result_lines = []
        found_content = False

        for i in range(1, len(lines)):
            line = lines[i].strip()

            # Skip empty lines until we find content
            if not found_content and line == '':
                continue
            elif not found_content and line != '':
                found_content = True
                result_lines.append(lines[i])
            else:
                result_lines.append(lines[i])

        return '\n'.join(result_lines)

    return content

def fix_file(file_path):
    """Fix headers in a single file"""

    if not os.path.exists(file_path):
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        original_content = f.read()

    # Check if it needs fixing (starts with # )
    if not original_content.startswith('# '):
        return False

    fixed_content = fix_duplicate_headers(original_content, file_path)

    # Only write if content changed
    if fixed_content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        print(f"✅ Fixed: {file_path}")
        return True

    return False

def main():
    """Fix all duplicate headers across documentation"""

    print("🔧 COMPREHENSIVE HEADER CLEANUP")
    print("=" * 50)

    # Find all .mdx files
    mdx_files = []
    for pattern in ['*.mdx', '*/*.mdx', '*/*/*.mdx']:
        mdx_files.extend(glob.glob(pattern))

    # Remove node_modules and sort
    mdx_files = [f for f in mdx_files if 'node_modules' not in f]
    mdx_files.sort()

    fixed_count = 0

    for file_path in mdx_files:
        if fix_file(file_path):
            fixed_count += 1

    print(f"\n📊 SUMMARY:")
    print(f"✅ Files processed: {len(mdx_files)}")
    print(f"✅ Headers fixed: {fixed_count}")

    # Verify the fix worked
    remaining_duplicates = []
    for file_path in mdx_files:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
                if content.startswith('# '):
                    remaining_duplicates.append(file_path)

    if not remaining_duplicates:
        print(f"🎉 SUCCESS: All duplicate headers removed!")
    else:
        print(f"⚠️  {len(remaining_duplicates)} files still have duplicate headers:")
        for file_path in remaining_duplicates:
            print(f"   • {file_path}")

    return len(remaining_duplicates) == 0

if __name__ == "__main__":
    main()