#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

/**
 * Convert Docsify markdown to Docusaurus markdown
 * Usage: node convert-docsify-to-docusaurus.js <input-file> <output-file>
 */

function convertDocsifyToDocusaurus(content, filename) {
  let result = content;

  // Pattern 1: Convert heading anchors from :id=anchor to {#anchor}
  // Example: ## Heading :id=my-anchor -> ## Heading {#my-anchor}
  result = result.replace(/^(#{1,6})\s+(.+?)\s+:id=([a-z0-9-_]+)\s*$/gim, '$1 $2 {#$3}');

  // Pattern 2: Convert same-page anchor links from ?id=anchor to #anchor
  // Example: [link](?id=anchor) -> [link](#anchor)
  result = result.replace(/\]\(\?id=([a-z0-9-_]+)\)/gi, '](#$1)');

  // Pattern 3: Convert cross-file anchor links from file.md?id=anchor to file#anchor
  // Example: [link](concepts/auth.md?id=section) -> [link](authentication#section)
  result = result.replace(/\]\(([a-z0-9/\-_]+)\.md\?id=([a-z0-9-_]+)\)/gi, (match, file, anchor) => {
    // Extract just the filename without path and extension
    const fileName = file.split('/').pop();
    return `](${fileName}#${anchor})`;
  });

  // Pattern 4: Convert cross-file links without anchors from file.md to file
  // Example: [link](concepts/auth.md) -> [link](authentication)
  // But preserve relative paths like ../
  result = result.replace(/\]\(([a-z0-9/\-_]+)\.md\)/gi, (match, file) => {
    const fileName = file.split('/').pop();
    return `](${fileName})`;
  });

  // Pattern 5: Handle relative directory links
  // Example: [link](../concepts/auth.md) -> [link](../concepts/authentication)
  result = result.replace(/\]\((\.\.\/[a-z0-9/\-_]+)\.md\)/gi, (match, file) => {
    return `](${file})`;
  });

  // Extract title from first # heading if it exists
  const titleMatch = result.match(/^#\s+(.+)$/m);
  const title = titleMatch ? titleMatch[1].replace(/\s+:id=[a-z0-9-_]+\s*$/, '') : filename.replace(/\.md$/, '');

  // Extract the base filename without extension for the id
  const id = path.basename(filename, '.md');

  // Add frontmatter if not present
  if (!result.startsWith('---')) {
    const frontmatter = `---
id: ${id}
title: ${title}
---

`;
    result = frontmatter + result;
  }

  return result;
}

function main() {
  const args = process.argv.slice(2);

  if (args.length !== 2) {
    console.error('Usage: node convert-docsify-to-docusaurus.js <input-file> <output-file>');
    process.exit(1);
  }

  const [inputFile, outputFile] = args;

  if (!fs.existsSync(inputFile)) {
    console.error(`Error: Input file "${inputFile}" does not exist`);
    process.exit(1);
  }

  const content = fs.readFileSync(inputFile, 'utf8');
  const filename = path.basename(inputFile);
  const converted = convertDocsifyToDocusaurus(content, filename);

  // Ensure output directory exists
  const outputDir = path.dirname(outputFile);
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  fs.writeFileSync(outputFile, converted, 'utf8');
  console.log(`✓ Converted ${inputFile} -> ${outputFile}`);
}

if (require.main === module) {
  main();
}

module.exports = { convertDocsifyToDocusaurus };
