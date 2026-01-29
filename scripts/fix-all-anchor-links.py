#!/usr/bin/env python3

import re
from pathlib import Path
from collections import defaultdict

def heading_to_anchor(heading):
    """Convert a heading to what Mintlify would auto-generate as anchor"""
    # Remove markdown formatting
    clean = re.sub(r'[`*_]', '', heading)
    # Convert to lowercase
    clean = clean.lower()
    # Replace spaces with hyphens
    clean = re.sub(r'\s+', '-', clean)
    # Remove special characters except hyphens
    clean = re.sub(r'[^a-z0-9-]', '', clean)
    # Remove consecutive hyphens
    clean = re.sub(r'-+', '-', clean)
    # Remove leading/trailing hyphens
    clean = clean.strip('-')
    return clean

def get_anchors_and_headings(file_path):
    """Extract all same-page anchor links and headings from a file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all same-page anchor links (not cross-file)
    # Pattern: ](#anchor) where we're looking for anchors that should map to headings
    anchor_links = re.findall(r'\]\(#([a-z0-9-]+)\)', content)

    # Find all headings with their line numbers
    headings = []
    for match in re.finditer(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE):
        level = len(match.group(1))
        heading_text = match.group(2).strip()
        line_num = content[:match.start()].count('\n') + 1
        headings.append((level, heading_text, line_num))

    # Find existing HTML anchors
    html_anchors = re.findall(r'<a\s+id="([^"]+)"', content)

    return anchor_links, headings, html_anchors, content

def fix_file_anchors(file_path):
    """Add HTML anchor tags where needed"""
    anchor_links, headings, html_anchors, original_content = get_anchors_and_headings(file_path)

    if not anchor_links:
        return False, []

    # Build a map of what anchors exist
    existing_anchors = set(html_anchors)

    # Build what Mintlify would auto-generate
    auto_generated = {}
    for level, heading_text, line_num in headings:
        generated = heading_to_anchor(heading_text)
        auto_generated[generated] = (heading_text, line_num)

    # Find which links need explicit anchors
    needs_anchors = []
    for link in set(anchor_links):
        if link not in existing_anchors and link not in auto_generated:
            # This link doesn't have an explicit anchor and won't auto-generate correctly
            needs_anchors.append(link)

    if not needs_anchors:
        return False, []

    # Now we need to figure out which heading each broken link should map to
    # by looking at the original Docsify file
    return True, needs_anchors

def main():
    docs_dir = Path('/Users/maxwellrand/Desktop/Chameleon/dev/api/mintlify-docs')
    docsify_dir = Path('/Users/maxwellrand/Desktop/Chameleon/dev/api/docs')

    print("Checking for broken anchor links across all files...\n")

    issues = []

    for mdx_file in sorted(docs_dir.rglob('*.mdx')):
        has_issues, broken_links = fix_file_anchors(mdx_file)
        if has_issues:
            issues.append((mdx_file.relative_to(docs_dir), broken_links))

    if issues:
        print(f"Found {sum(len(links) for _, links in issues)} broken anchor links in {len(issues)} files:\n")
        for file, links in issues[:20]:  # Show first 20 files
            print(f"\n{file}:")
            for link in links[:10]:
                print(f"  #{link}")
            if len(links) > 10:
                print(f"  ... and {len(links) - 10} more")
    else:
        print("✅ No broken anchor links found!")

if __name__ == '__main__':
    main()
