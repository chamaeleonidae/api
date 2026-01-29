#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

/**
 * Validate all internal links in migrated Docusaurus documentation
 * Usage: node validate-links.js
 */

const DOCS_DIR = path.join(__dirname, '..', 'docusaurus-site', 'docs');

function getAllMarkdownFiles(dir, fileList = [], baseDir = dir) {
  const files = fs.readdirSync(dir);

  files.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      getAllMarkdownFiles(filePath, fileList, baseDir);
    } else if (file.endsWith('.md')) {
      fileList.push({
        path: filePath,
        relativePath: path.relative(baseDir, filePath),
      });
    }
  });

  return fileList;
}

function extractLinks(content) {
  // Match markdown links: [text](url) or [text](url#anchor)
  const linkRegex = /\[([^\]]+)\]\(([^)]+)\)/g;
  const links = [];
  let match;

  while ((match = linkRegex.exec(content)) !== null) {
    const [, text, url] = match;

    // Only validate internal links (not http/https)
    if (!url.startsWith('http://') && !url.startsWith('https://')) {
      links.push({
        text,
        url,
        line: content.substring(0, match.index).split('\n').length,
      });
    }
  }

  return links;
}

function validateLink(link, currentFile, allFiles) {
  const { url } = link;

  // Extract file path and anchor from URL
  const [filePath, anchor] = url.split('#');

  // Handle same-page anchors (starting with #)
  if (url.startsWith('#')) {
    return { valid: true, type: 'same-page-anchor' };
  }

  // Get the directory of the current file
  const currentDir = path.dirname(currentFile.path);

  // Resolve the target file path
  let targetPath;
  if (filePath.startsWith('/')) {
    // Absolute path from docs root
    targetPath = path.join(DOCS_DIR, filePath.substring(1));
  } else if (filePath.startsWith('../') || filePath.startsWith('./')) {
    // Relative path
    targetPath = path.resolve(currentDir, filePath);
  } else {
    // Relative path without ./
    targetPath = path.resolve(currentDir, filePath);
  }

  // Add .md extension if not present and not a directory
  if (!targetPath.endsWith('.md') && !fs.existsSync(targetPath)) {
    targetPath = targetPath + '.md';
  }

  // Check if target file exists
  const fileExists = allFiles.some(f => f.path === targetPath);

  if (!fileExists && !fs.existsSync(targetPath)) {
    return {
      valid: false,
      type: 'missing-file',
      targetPath,
      message: `Target file not found: ${path.relative(DOCS_DIR, targetPath)}`,
    };
  }

  // If there's an anchor, we could validate it exists in the target file
  // but that's more complex and not critical for this migration
  if (anchor) {
    return { valid: true, type: 'cross-file-anchor', targetPath };
  }

  return { valid: true, type: 'cross-file', targetPath };
}

function main() {
  console.log('Validating internal links in Docusaurus documentation...\n');

  const allFiles = getAllMarkdownFiles(DOCS_DIR);
  console.log(`Found ${allFiles.length} markdown files\n`);

  let totalLinks = 0;
  let validLinks = 0;
  let invalidLinks = [];

  allFiles.forEach(file => {
    const content = fs.readFileSync(file.path, 'utf8');
    const links = extractLinks(content);

    links.forEach(link => {
      totalLinks++;
      const validation = validateLink(link, file, allFiles);

      if (validation.valid) {
        validLinks++;
      } else {
        invalidLinks.push({
          file: file.relativePath,
          line: link.line,
          text: link.text,
          url: link.url,
          ...validation,
        });
      }
    });
  });

  console.log('='.repeat(60));
  console.log(`Total internal links: ${totalLinks}`);
  console.log(`Valid links: ${validLinks} (${((validLinks / totalLinks) * 100).toFixed(1)}%)`);
  console.log(`Invalid links: ${invalidLinks.length}`);
  console.log('='.repeat(60));

  if (invalidLinks.length > 0) {
    console.log('\nInvalid links found:\n');
    invalidLinks.forEach(link => {
      console.log(`  ${link.file}:${link.line}`);
      console.log(`    Text: "${link.text}"`);
      console.log(`    URL: ${link.url}`);
      console.log(`    Error: ${link.message}`);
      console.log('');
    });
    process.exit(1);
  } else {
    console.log('\n✓ All links are valid!');
    process.exit(0);
  }
}

if (require.main === module) {
  main();
}

module.exports = { validateLink, extractLinks };
