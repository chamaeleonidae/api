#!/usr/bin/env python3

import re
from pathlib import Path
from collections import defaultdict

def get_anchors_and_headings(file_path):
    """Extract all same-page anchor links and headings from a file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all same-page anchor links (not cross-file)
    # Pattern: ]( followed by # but not ](/
    anchor_links = re.findall(r'\]\(#([a-z0-9-]+)\)', content)

    # Find all headings
    headings = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)

    # Also find explicit HTML anchors
    html_anchors = re.findall(r'<a\s+id="([^"]+)"', content)

    return anchor_links, headings, html_anchors

def heading_to_anchor(heading):
    """Convert a heading to what Mintlify would auto-generate as anchor"""
    # Remove markdown formatting
    clean = re.sub(r'[`*_]', '', heading)
    # Convert to lowercase
    clean = clean.lower()
    # Replace spaces with hyphens
    clean = re.sub(r'\s+', '-', clean)
    # Remove special characters
    clean = re.sub(r'[^a-z0-9-]', '', clean)
    return clean

def main():
    docs_dir = Path('/Users/maxwellrand/Desktop/Chameleon/dev/api/mintlify-docs')

    print("Checking for broken anchor links...\n")

    issues = []

    for mdx_file in sorted(docs_dir.rglob('*.mdx')):
        anchor_links, headings, html_anchors = get_anchors_and_headings(mdx_file)

        if not anchor_links:
            continue

        # Generate what Mintlify would create for each heading
        generated_anchors = set()
        for heading in headings:
            generated_anchors.add(heading_to_anchor(heading))

        # Combine generated and explicit HTML anchors
        all_available_anchors = generated_anchors | set(html_anchors)

        # Check if each link target exists
        for link in anchor_links:
            if link not in all_available_anchors:
                issues.append((mdx_file.relative_to(docs_dir), link, headings))

    if issues:
        print(f"Found {len(issues)} files with broken anchor links:\n")
        for file, link, headings in issues:
            print(f"❌ {file}")
            print(f"   Link: #{link}")
            print(f"   Available headings: {headings[:3]}")
            print()
    else:
        print("✅ No broken anchor links found!")

if __name__ == '__main__':
    main()
