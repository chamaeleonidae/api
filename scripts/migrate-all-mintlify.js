#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { convertDocsifyToMintlify } = require('./convert-docsify-to-mintlify');

/**
 * Bulk migrate all markdown files from Docsify to Mintlify
 * Usage: node migrate-all-mintlify.js
 */

const DOCS_DIR = path.join(__dirname, '..', 'docs');
const OUTPUT_DIR = path.join(__dirname, '..', 'mintlify-docs');

function getAllMarkdownFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);

  files.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      getAllMarkdownFiles(filePath, fileList);
    } else if (file.endsWith('.md') && !file.startsWith('_')) {
      // Skip files starting with _ (like _sidebar.md)
      fileList.push(filePath);
    }
  });

  return fileList;
}

function migrateFile(inputFile) {
  const relativePath = path.relative(DOCS_DIR, inputFile);
  let outputFile = path.join(OUTPUT_DIR, relativePath);

  // Special handling for README.md -> introduction.mdx
  if (path.basename(inputFile) === 'README.md') {
    outputFile = path.join(OUTPUT_DIR, 'introduction.mdx');
  } else {
    // Change .md to .mdx
    outputFile = outputFile.replace(/\.md$/, '.mdx');
  }

  try {
    const content = fs.readFileSync(inputFile, 'utf8');
    const filename = path.basename(inputFile);
    const converted = convertDocsifyToMintlify(content, filename);

    // Ensure output directory exists
    const outputDir = path.dirname(outputFile);
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }

    fs.writeFileSync(outputFile, converted, 'utf8');
    console.log(`✓ ${relativePath} -> ${path.relative(path.join(__dirname, '..'), outputFile)}`);
    return { success: true, file: relativePath };
  } catch (error) {
    console.error(`✗ ${relativePath}: ${error.message}`);
    return { success: false, file: relativePath, error: error.message };
  }
}

function main() {
  console.log('Starting bulk migration from Docsify to Mintlify...\n');

  const markdownFiles = getAllMarkdownFiles(DOCS_DIR);
  const results = markdownFiles.map(migrateFile);

  const successful = results.filter(r => r.success).length;
  const failed = results.filter(r => !r.success);

  console.log('\n' + '='.repeat(60));
  console.log(`Migration complete: ${successful}/${results.length} files converted`);

  if (failed.length > 0) {
    console.log('\nFailed files:');
    failed.forEach(f => console.log(`  - ${f.file}: ${f.error}`));
  }

  console.log('\nNext steps:');
  console.log('1. Update mint.json with complete navigation structure');
  console.log('2. Run: mintlify dev');
  console.log('3. Test all pages and links');

  process.exit(failed.length > 0 ? 1 : 0);
}

if (require.main === module) {
  main();
}

module.exports = { migrateFile, getAllMarkdownFiles };
