#!/bin/bash

echo "=== Migration Content Validation ==="
echo

# Function to compare file lengths
compare_files() {
    local orig_dir="$1"
    local new_dir="$2"
    local file_pattern="$3"

    echo "Checking $orig_dir -> $new_dir ($file_pattern)"
    echo "----------------------------------------"

    for orig_file in docs/$orig_dir/*.md; do
        if [[ -f "$orig_file" ]]; then
            basename=$(basename "$orig_file" .md)
            new_file="$new_dir/${basename}.mdx"

            if [[ -f "$new_file" ]]; then
                orig_lines=$(wc -l < "$orig_file")
                new_lines=$(wc -l < "$new_file")

                # Allow some variance for component conversion
                threshold=$((orig_lines * 80 / 100))  # 80% threshold

                if [[ $new_lines -lt $threshold ]]; then
                    echo "⚠️  $basename: $orig_lines → $new_lines lines (POTENTIAL TRUNCATION)"
                else
                    echo "✅ $basename: $orig_lines → $new_lines lines"
                fi
            else
                echo "❌ $basename: MISSING MIGRATION"
            fi
        fi
    done
    echo
}

# Check all directories
compare_files "concepts" "concepts" "*.mdx"
compare_files "apis" "apis" "*.mdx"
compare_files "js" "js" "*.mdx"
compare_files "webhooks" "webhooks" "*.mdx"
compare_files "guides" "guides" "*.mdx"

echo "=== Summary ==="
echo "Files needing attention will show ⚠️ or ❌"