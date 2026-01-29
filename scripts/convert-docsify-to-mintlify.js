#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

/**
 * Convert Docsify markdown to Mintlify MDX
 * Usage: node convert-docsify-to-mintlify.js <input-file> <output-file>
 */

function convertDocsifyToMintlify(content, filename) {
  let result = content;

  // Pattern 1: Remove Docsify heading anchors (:id=)
  // Mintlify auto-generates anchors from heading text
  // Example: ## Schema :id=schema -> ## Schema
  result = result.replace(/^(#{1,6})\s+(.+?)\s+:id=([a-z0-9-_]+)\s*$/gim, '$1 $2');

  // Pattern 2: Convert same-page anchor links
  // Example: [link](?id=anchor) -> [link](#anchor)
  result = result.replace(/\]\(\?id=([a-z0-9-_]+)\)/gi, '](#$1)');

  // Pattern 3: Convert cross-file anchor links with Docsify :id= format
  // Example: [link](apis/search.md?id=rest) -> [link](/apis/search#rest)
  // Also handle: [link](/apis/search.md?id=rest) -> [link](/apis/search#rest)
  result = result.replace(/\]\((\/?)([a-z0-9/\-_]+)\.md\?id=([a-z0-9-_]+)\)/gi, (match, leadingSlash, file, anchor) => {
    // If already has leading slash, keep it; otherwise add it
    const prefix = leadingSlash || '/';
    return `](${prefix}${file}#${anchor})`;
  });

  // Pattern 4: Convert cross-file links without anchors
  // Example: [link](apis/profiles.md) -> [link](/apis/profiles)
  // Also handle: [link](/apis/profiles.md) -> [link](/apis/profiles)
  result = result.replace(/\]\((\/?)([a-z0-9/\-_]+)\.md\)/gi, (match, leadingSlash, file) => {
    const prefix = leadingSlash || '/';
    return `](${prefix}${file})`;
  });

  // Pattern 5: Handle relative directory links
  // Example: [link](../concepts/auth.md) -> [link](/concepts/auth)
  result = result.replace(/\]\((\.\.\/[a-z0-9/\-_]+)\.md\)/gi, (match, file) => {
    // Convert ../ paths to root-relative
    const normalized = file.replace(/\.\.\//g, '');
    return `](/${normalized})`;
  });

  // Extract title from first # heading
  const titleMatch = result.match(/^#\s+(.+)$/m);
  const title = titleMatch ? titleMatch[1].trim() : filename.replace(/\.mdx?$/, '');

  // Extract description (first paragraph after title)
  const descMatch = result.match(/^#[^\n]+\n\n(.+?)(?:\n\n|$)/s);
  const description = descMatch ? descMatch[1].replace(/\*\*/g, '').substring(0, 160) : '';

  // Add frontmatter
  const frontmatter = `---
title: "${title}"
description: "${description}"
---

`;

  // Remove existing frontmatter if present, we'll add our own
  // Only match if both opening and closing --- are at start of line
  result = result.replace(/^---\n[\s\S]+?\n---\n*/m, '');

  return frontmatter + result;
}

function main() {
  const args = process.argv.slice(2);

  if (args.length !== 2) {
    console.error('Usage: node convert-docsify-to-mintlify.js <input-file> <output-file>');
    process.exit(1);
  }

  const [inputFile, outputFile] = args;

  if (!fs.existsSync(inputFile)) {
    console.error(`Error: Input file "${inputFile}" does not exist`);
    process.exit(1);
  }

  const content = fs.readFileSync(inputFile, 'utf8');
  const filename = path.basename(inputFile);
  const converted = convertDocsifyToMintlify(content, filename);

  // Ensure output directory exists
  const outputDir = path.dirname(outputFile);
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  // Output as .mdx
  const mdxOutput = outputFile.replace(/\.md$/, '.mdx');
  fs.writeFileSync(mdxOutput, converted, 'utf8');
  console.log(`✓ Converted ${inputFile} -> ${mdxOutput}`);
}

if (require.main === module) {
  main();
}

module.exports = { convertDocsifyToMintlify };
