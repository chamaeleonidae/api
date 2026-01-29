#!/usr/bin/env python3

import re
from pathlib import Path

# Mapping of heading text to the anchor ID that should be used
ANCHOR_MAPPINGS = {
    "## `Search` bar Schema": "schema",
    "## `SearchGroups` Schema": "schema-search-groups",
    "## `SearchPage` Schema": "schema-search-page",
    "## `SearchLabelTheme` Schema": "schema-search-label-themes",
    "## List all HelpBars": "searches-index",
    "## Create / Update your HelpBar": "searches-create",
    "## `SearchItem` Schema": "schema-search-items",
    "## `SearchLabel` Schema": "schema-search-labels",
    "## List all Search Items": "search-items-index",
    "## Create / Update your `SearchItem`s": "search-items-create",
    "## Batch Update your `SearchItem`s": "search-items-batch-update",
    "## Delete a `SearchItem`s": "search-items-destroy",
    "## Bulk Delete a `SearchItem`s": "search-items-bulk-destroy",
    "## `SearchAction` Schema": "schema-search-actions",
    "## `SearchAction` with `kind=url` Schema": "schema-search-action-url",
    "## `SearchAction` with `kind=navigate` Schema": "schema-search-action-navigate",
    "## `SearchAction` with `kind=event` Schema": "schema-search-action-event",
    "## `SearchAction` with `kind=identify` Schema": "schema-search-action-identify",
    "## `SearchAction` with `kind=tour` Schema": "schema-search-action-tour",
    "## `SearchAction` with `kind=survey` Schema": "schema-search-action-survey",
    "## `SearchAction` with `kind=script` Schema": "schema-search-action-script",
    "## `SearchAction` with `kind=function` Schema": "schema-search-action-function",
    "## `SearchAction` with `kind=airtable` Schema": "schema-search-action-airtable",
    "## `SearchAction` with `kind=arcade` Schema": "schema-search-action-arcade",
    "## `SearchAction` with `kind=calendly` Schema": "schema-search-action-calendly",
    "## `SearchAction` with `kind=chili_piper` Schema": "schema-search-action-chili_piper",
    "## `SearchAction` with `kind=embed` Schema": "schema-search-action-embed",
    "## `SearchAction` with `kind=figma` Schema": "schema-search-action-figma",
    "## `SearchAction` with `kind=google` Schema": "schema-search-action-google",
    "## `SearchAction` with `kind=helpscout` Schema": "schema-search-action-helpscout",
    "## `SearchAction` with `kind=hubspot_lists` Schema": "schema-search-action-hubspot_lists",
    "## `SearchAction` with `kind=intercom` Schema": "schema-search-action-intercom",
    "## `SearchAction` with `kind=livestorm` Schema": "schema-search-action-livestorm",
    "## `SearchAction` with `kind=loom` Schema": "schema-search-action-loom",
    "## `SearchAction` with `kind=navattic` Schema": "schema-search-action-navattic",
    "## `SearchAction` with `kind=pitch` Schema": "schema-search-action-pitch",
    "## `SearchAction` with `kind=typeform` Schema": "schema-search-action-typeform",
    "## `SearchAction` with `kind=zendesk` Schema": "schema-search-action-zendesk",
    "### JS API type definitions": "search-js-types",
    "## Search Item Importing via CSV (`SearchImport`)": "schema-search-imports",
    "## Create a Search Import": "search-imports-create",
    "## Get a Search Import": "search-imports-show",
    "## Trigger HelpBar": "trigger-search-api",
}

def add_anchors(file_path):
    """Add HTML anchor tags before headings that need them"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified = False
    new_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this line is a heading that needs an anchor
        line_stripped = line.strip()
        if line_stripped in ANCHOR_MAPPINGS:
            anchor_id = ANCHOR_MAPPINGS[line_stripped]
            # Check if there's already an anchor on the previous line
            if i > 0 and '<a id=' in new_lines[-1]:
                # Already has an anchor, skip
                new_lines.append(line)
            else:
                # Add the anchor
                new_lines.append(f'<a id="{anchor_id}"></a>\n')
                new_lines.append(line)
                modified = True
                print(f"Added anchor #{anchor_id} for: {line_stripped}")
        else:
            new_lines.append(line)

        i += 1

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return True
    return False

def main():
    file_path = Path('/Users/maxwellrand/Desktop/Chameleon/dev/api/mintlify-docs/apis/search.mdx')

    print(f"Adding anchor tags to {file_path.name}...\n")

    if add_anchors(file_path):
        print(f"\n✅ Successfully added anchor tags to {file_path.name}")
    else:
        print(f"\n✅ No changes needed for {file_path.name}")

if __name__ == '__main__':
    main()
