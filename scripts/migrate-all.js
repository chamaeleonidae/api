#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { convertDocsifyToDocusaurus } = require('./convert-docsify-to-docusaurus');

/**
 * Bulk migrate all markdown files from Docsify to Docusaurus
 * Usage: node migrate-all.js
 */

const DOCS_DIR = path.join(__dirname, '..', 'docs');
const OUTPUT_DIR = path.join(__dirname, '..', 'docusaurus-site', 'docs');

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
  const outputFile = path.join(OUTPUT_DIR, relativePath);

  // Special handling for README.md -> index.md
  const finalOutputFile = outputFile.replace(/README\.md$/, 'index.md');

  try {
    const content = fs.readFileSync(inputFile, 'utf8');
    const filename = path.basename(inputFile);
    let converted = convertDocsifyToDocusaurus(content, filename);

    // Special handling for README/index: add slug frontmatter
    if (filename === 'README.md') {
      converted = converted.replace(
        /^---\n(.*)\n---/s,
        (match, frontmatter) => {
          if (!frontmatter.includes('slug:')) {
            return `---\n${frontmatter}\nslug: /\n---`;
          }
          return match;
        }
      );
    }

    // Ensure output directory exists
    const outputDir = path.dirname(finalOutputFile);
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }

    fs.writeFileSync(finalOutputFile, converted, 'utf8');
    console.log(`✓ ${relativePath} -> ${path.relative(path.join(__dirname, '..'), finalOutputFile)}`);
    return { success: true, file: relativePath };
  } catch (error) {
    console.error(`✗ ${relativePath}: ${error.message}`);
    return { success: false, file: relativePath, error: error.message };
  }
}

function main() {
  console.log('Starting bulk migration from Docsify to Docusaurus...\n');

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

  process.exit(failed.length > 0 ? 1 : 0);
}

if (require.main === module) {
  main();
}

module.exports = { migrateFile, getAllMarkdownFiles };
