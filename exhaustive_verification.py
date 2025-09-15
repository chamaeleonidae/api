#!/usr/bin/env python3
"""
EXHAUSTIVE bidirectional verification of ALL files in migration
This will check EVERY original file has a migrated equivalent
And EVERY migrated file has an original source
"""

import os
import glob

def get_all_original_files():
    """Get every .md file in docs directory"""
    original_files = []
    for root, dirs, files in os.walk('docs'):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                original_files.append(full_path)
    return sorted(original_files)

def get_all_migrated_files():
    """Get every .mdx file in project (excluding node_modules)"""
    migrated_files = []

    # Get all .mdx files in root and subdirectories
    for pattern in ['*.mdx', '*/*.mdx', '*/*/*.mdx']:
        for file_path in glob.glob(pattern):
            if 'node_modules' not in file_path:
                migrated_files.append(file_path)

    return sorted(migrated_files)

def get_expected_migrated_path(original_path):
    """Get expected migrated path based on original path"""

    # Remove docs/ prefix and .md extension
    rel_path = original_path.replace('docs/', '').replace('.md', '')

    # Apply migration mappings
    if rel_path.startswith('apis/'):
        return rel_path.replace('apis/', 'api/') + '.mdx'
    elif rel_path.startswith('concepts/authentication'):
        return 'authentication.mdx'
    elif rel_path.startswith('concepts/'):
        return rel_path + '.mdx'
    elif rel_path.startswith('js/'):
        return rel_path + '.mdx'
    elif rel_path.startswith('webhooks/'):
        return rel_path + '.mdx'
    elif rel_path.startswith('guides/js/installing-correctly'):
        return 'guides/installation.mdx'
    elif rel_path.startswith('guides/helpbar/user-generated-content'):
        return 'guides/helpbar-user-content.mdx'
    elif rel_path == '_sidebar':
        return None  # Skip sidebar file
    else:
        # Root level or other files
        return rel_path + '.mdx'

def get_original_source_path(migrated_path):
    """Get expected original source path based on migrated path"""

    # Remove .mdx extension
    base_path = migrated_path.replace('.mdx', '')

    # Apply reverse mappings
    if base_path.startswith('api/'):
        return 'docs/' + base_path.replace('api/', 'apis/') + '.md'
    elif base_path == 'authentication':
        return 'docs/concepts/authentication.md'
    elif base_path.startswith('concepts/'):
        return 'docs/' + base_path + '.md'
    elif base_path.startswith('js/'):
        return 'docs/' + base_path + '.md'
    elif base_path.startswith('webhooks/'):
        return 'docs/' + base_path + '.md'
    elif base_path == 'guides/installation':
        return 'docs/guides/js/installing-correctly.md'
    elif base_path == 'guides/helpbar-user-content':
        return 'docs/guides/helpbar/user-generated-content.md'
    elif base_path in ['overview', 'introduction']:
        return None  # These are generated files
    else:
        return 'docs/' + base_path + '.md'

def verify_migration():
    """Comprehensive bidirectional verification"""

    original_files = get_all_original_files()
    migrated_files = get_all_migrated_files()

    print("=" * 80)
    print("EXHAUSTIVE MIGRATION VERIFICATION")
    print("=" * 80)

    print(f"\nOriginal files found: {len(original_files)}")
    print(f"Migrated files found: {len(migrated_files)}")

    # Phase 1: Check every original file has a migrated equivalent
    print(f"\n{'='*50}")
    print("PHASE 1: ORIGINAL → MIGRATED VERIFICATION")
    print(f"{'='*50}")

    missing_migrations = []
    found_migrations = []

    for orig_file in original_files:
        expected_migrated = get_expected_migrated_path(orig_file)

        if expected_migrated is None:
            print(f"⚪ SKIP: {orig_file} (not meant to be migrated)")
            continue

        if os.path.exists(expected_migrated):
            found_migrations.append((orig_file, expected_migrated))
            print(f"✅ {orig_file} → {expected_migrated}")
        else:
            missing_migrations.append((orig_file, expected_migrated))
            print(f"❌ MISSING: {orig_file} → {expected_migrated}")

    # Phase 2: Check every migrated file has an original source
    print(f"\n{'='*50}")
    print("PHASE 2: MIGRATED → ORIGINAL VERIFICATION")
    print(f"{'='*50}")

    orphaned_files = []
    valid_migrations = []

    for migrated_file in migrated_files:
        expected_original = get_original_source_path(migrated_file)

        if expected_original is None:
            print(f"⚪ GENERATED: {migrated_file} (no original source expected)")
            continue

        if os.path.exists(expected_original):
            valid_migrations.append((expected_original, migrated_file))
            print(f"✅ {migrated_file} ← {expected_original}")
        else:
            orphaned_files.append((migrated_file, expected_original))
            print(f"❌ ORPHANED: {migrated_file} (expected source: {expected_original})")

    # Summary
    print(f"\n{'='*50}")
    print("COMPREHENSIVE SUMMARY")
    print(f"{'='*50}")

    print(f"✅ Successfully migrated: {len(found_migrations)}")
    print(f"❌ Missing migrations: {len(missing_migrations)}")
    print(f"✅ Valid migrated files: {len(valid_migrations)}")
    print(f"❌ Orphaned files: {len(orphaned_files)}")

    if missing_migrations:
        print(f"\n🚨 CRITICAL: {len(missing_migrations)} ORIGINAL FILES NOT MIGRATED:")
        for orig, expected in missing_migrations:
            if os.path.exists(orig):
                with open(orig, 'r') as f:
                    lines = len(f.readlines())
                print(f"   • {orig} ({lines} lines) → {expected}")
            else:
                print(f"   • {orig} → {expected}")

    if orphaned_files:
        print(f"\n🚨 CRITICAL: {len(orphaned_files)} ORPHANED FILES (no original source):")
        for migrated, expected_orig in orphaned_files:
            print(f"   • {migrated} (expected: {expected_orig})")

    # Final verdict
    total_issues = len(missing_migrations) + len(orphaned_files)
    if total_issues == 0:
        print(f"\n🎉 MIGRATION VERIFICATION: ✅ PERFECT")
        print("All original files migrated, all migrated files have sources.")
    else:
        print(f"\n💥 MIGRATION VERIFICATION: ❌ FAILED")
        print(f"Found {total_issues} critical issues requiring immediate attention.")

    return total_issues == 0

if __name__ == "__main__":
    verify_migration()