#!/usr/bin/env python3
"""
Migrate Docsify documentation to Mintlify format
Preserves all content, only changes format
"""

import os
import re
import shutil
from pathlib import Path

def migrate_file(source_path, target_path):
    """Migrate a single file from Docsify to Mintlify format"""

    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

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

    # Create target directory if needed
    os.makedirs(os.path.dirname(target_path), exist_ok=True)

    # Write migrated content
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Migrated: {source_path} -> {target_path}")

def main():
    """Main migration function"""

    # Define migration mappings
    migrations = [
        # Core API docs
        ('docs/apis/profiles.md', 'api/profiles.mdx'),
        ('docs/apis/companies.md', 'api/companies.mdx'),
        ('docs/apis/surveys.md', 'api/surveys.mdx'),
        ('docs/apis/tours.md', 'api/tours.mdx'),
        ('docs/apis/deliveries.md', 'api/deliveries.mdx'),
        ('docs/apis/overview.md', 'api/overview.mdx'),

        # Concepts
        ('docs/concepts/authentication.md', 'authentication.mdx'),

        # JavaScript API
        ('docs/js/overview.md', 'js/overview.mdx'),
        ('docs/js/profiles.md', 'js/profiles.mdx'),

        # Webhooks
        ('docs/webhooks/overview.md', 'webhooks/overview.mdx'),
        ('docs/webhooks/profiles.md', 'webhooks/profiles.mdx'),

        # Guides
        ('docs/guides/js/installing-correctly.md', 'guides/installation.mdx'),
        ('docs/guides/helpbar/user-generated-content.md', 'guides/helpbar.mdx'),
    ]

    print("Starting migration...")

    for source, target in migrations:
        if os.path.exists(source):
            migrate_file(source, target)
        else:
            print(f"Warning: Source file not found: {source}")

    print("\nMigration complete!")
    print("Note: Manual pages (introduction.mdx, overview.mdx) were preserved")

if __name__ == "__main__":
    main()