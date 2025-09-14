#!/usr/bin/env python3
"""
Complete migration of ALL Chameleon documentation from Docsify to Mintlify
Based on the exact _sidebar.md structure
"""

import os
import re
import shutil
from pathlib import Path

def clean_content(content):
    """Clean Docsify-specific syntax from content"""

    # Remove Docsify :id= anchors
    content = re.sub(r' :id=[a-zA-Z0-9\-_]+', '', content)

    # Fix internal links - remove .md extensions for Mintlify
    content = re.sub(r'\]\(([^)]+)\.md\)', r'](\1)', content)

    # Fix relative paths for new structure
    content = content.replace('(apis/', '(/api/')
    content = content.replace('(concepts/', '(/concepts/')
    content = content.replace('(webhooks/', '(/webhooks/')
    content = content.replace('(js/', '(/js/')
    content = content.replace('(guides/', '(/guides/')

    # Remove page-level headers (since Mintlify provides page titles)
    lines = content.split('\n')
    if lines and lines[0].startswith('# '):
        # Find the next non-empty line after the title
        start_idx = 1
        while start_idx < len(lines) and lines[start_idx].strip() == '':
            start_idx += 1

        # If there's a bold description right after, keep it but make it normal
        if start_idx < len(lines) and lines[start_idx].startswith('**') and lines[start_idx].endswith('**'):
            lines[start_idx] = lines[start_idx][2:-2]  # Remove ** **

        content = '\n'.join(lines[start_idx:])

    return content

def migrate_file(source_path, target_path):
    """Migrate a single file from Docsify to Mintlify format"""

    if not os.path.exists(source_path):
        print(f"WARNING: Source file not found: {source_path}")
        return

    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean the content
    content = clean_content(content)

    # Create target directory if needed
    target_dir = os.path.dirname(target_path)
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)

    # Write migrated content
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Migrated: {source_path} -> {target_path}")

def main():
    """Complete migration based on _sidebar.md structure"""

    # Complete migration mappings based on _sidebar.md
    migrations = [
        # Getting Started (concepts)
        ('docs/concepts/any-model.md', 'concepts/any-model.mdx'),
        ('docs/concepts/personalizing.md', 'concepts/personalizing.mdx'),
        ('docs/apis/translation.md', 'concepts/localization.mdx'),
        ('docs/concepts/custom-triggers.md', 'concepts/custom-triggers.mdx'),

        # JavaScript API (complete section)
        ('docs/js/demos.md', 'js/demos.mdx'),
        ('docs/js/events.md', 'js/events.mdx'),
        ('docs/js/show-tour.md', 'js/show-tour.mdx'),
        ('docs/js/show-launcher.md', 'js/show-launcher.mdx'),
        ('docs/js/show-automation.md', 'js/show-automation.mdx'),
        ('docs/js/show-demo.md', 'js/show-demo.mdx'),
        ('docs/apis/search.md', 'js/helpbar.mdx'),  # Control the HelpBar
        ('docs/js/listen.md', 'js/listen.mdx'),

        # Webhooks (complete section)
        ('docs/webhooks/events.md', 'webhooks/events.mdx'),
        ('docs/webhooks/companies.md', 'webhooks/companies.mdx'),

        # REST API (all remaining endpoints)
        ('docs/apis/profiles-search.md', 'api/profiles-search.mdx'),
        ('docs/apis/segments.md', 'api/segments.mdx'),
        ('docs/apis/demos.md', 'api/demos.mdx'),
        ('docs/apis/search.md', 'api/search.mdx'),
        ('docs/apis/properties.md', 'api/properties.mdx'),
        ('docs/apis/translation.md', 'api/translation.mdx'),
        ('docs/apis/survey-responses.md', 'api/survey-responses.mdx'),
        ('docs/apis/tour-interactions.md', 'api/tour-interactions.mdx'),
        ('docs/apis/limit-groups.md', 'api/limit-groups.mdx'),
        ('docs/apis/alert-groups.md', 'api/alert-groups.mdx'),
        ('docs/apis/imports.md', 'api/imports.mdx'),
        ('docs/apis/launchers.md', 'api/launchers.mdx'),
        ('docs/apis/tooltips.md', 'api/tooltips.mdx'),
        ('docs/apis/changes.md', 'api/changes.mdx'),
        ('docs/apis/urls.md', 'api/urls.mdx'),
        ('docs/apis/webhooks.md', 'api/webhooks.mdx'),

        # Guides (complete section)
        # Note: js/demos.md is referenced in guides too - this is a duplicate reference
    ]

    print("🚀 Starting COMPLETE documentation migration...")
    print(f"📄 Migrating {len(migrations)} files...")

    migrated_count = 0
    for source, target in migrations:
        migrate_file(source, target)
        migrated_count += 1

    print(f"\n✅ Migration complete! Migrated {migrated_count} files")
    print("📝 Note: Navigation will need to be updated for complete structure")

if __name__ == "__main__":
    main()