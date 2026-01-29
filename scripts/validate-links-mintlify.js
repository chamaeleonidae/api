#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

/**
 * Validate internal links in Mintlify MDX files
 * Usage: node validate-links-mintlify.js
 */

const DOCS_DIR = path.join(__dirname, '..', 'mintlify-docs');

// Extract all internal links from markdown content
function extractLinks(content, filePath) {
  const links = [];
  const linkRegex = /\[([^\]]+)\]\(([^)]+)\)/g;

  let match;
  while ((match = linkRegex.exec(content)) !== null) {
    const linkText = match[1];
    const linkUrl = match[2];

    // Only check internal links (not external URLs)
    if (!linkUrl.startsWith('http://') && !linkUrl.startsWith('https://') && !linkUrl.startsWith('mailto:')) {
      links.push({
        text: linkText,
        url: linkUrl,
        source: filePath
      });
    }
  }

  return links;
}

// Get all MDX files
function getAllMdxFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);

  files.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      getAllMdxFiles(filePath, fileList);
    } else if (file.endsWith('.mdx')) {
      fileList.push(filePath);
    }
  });

  return fileList;
}

// Check if a file exists for a given link
function validateLink(link, existingFiles) {
  let url = link.url;

  // Remove anchor if present
  const anchorIndex = url.indexOf('#');
  if (anchorIndex !== -1) {
    url = url.substring(0, anchorIndex);
  }

  // If it's just an anchor (same-page link), it's valid
  if (url === '' || url.startsWith('#')) {
    return { valid: true, reason: 'same-page anchor' };
  }

  // Convert to absolute path
  let targetPath;
  if (url.startsWith('/')) {
    // Root-relative path
    targetPath = path.join(DOCS_DIR, url + '.mdx');
  } else {
    // Relative to source file
    const sourceDir = path.dirname(link.source);
    targetPath = path.join(sourceDir, url + '.mdx');
  }

  // Normalize path
  targetPath = path.normalize(targetPath);

  // Check if file exists
  if (existingFiles.has(targetPath)) {
    return { valid: true, reason: 'file exists' };
  }

  return { valid: false, reason: 'file not found', expected: targetPath };
}

function main() {
  console.log('Validating internal links in Mintlify documentation...\n');

  const mdxFiles = getAllMdxFiles(DOCS_DIR);
  const existingFilesSet = new Set(mdxFiles);

  console.log(`Found ${mdxFiles.length} MDX files\n`);

  let totalLinks = 0;
  let validLinks = 0;
  let brokenLinks = [];

  mdxFiles.forEach(filePath => {
    const content = fs.readFileSync(filePath, 'utf8');
    const links = extractLinks(content, filePath);

    totalLinks += links.length;

    links.forEach(link => {
      const validation = validateLink(link, existingFilesSet);

      if (validation.valid) {
        validLinks++;
      } else {
        brokenLinks.push({
          ...link,
          ...validation
        });
      }
    });
  });

  console.log('='.repeat(60));
  console.log(`Validation complete:`);
  console.log(`  Total links: ${totalLinks}`);
  console.log(`  Valid links: ${validLinks}`);
  console.log(`  Broken links: ${brokenLinks.length}`);
  console.log('='.repeat(60));

  if (brokenLinks.length > 0) {
    console.log('\n⚠️  Broken links found:\n');

    brokenLinks.forEach((link, idx) => {
      const relativeSrc = path.relative(DOCS_DIR, link.source);
      console.log(`${idx + 1}. ${relativeSrc}`);
      console.log(`   Link: "${link.text}" → ${link.url}`);
      console.log(`   Issue: ${link.reason}`);
      if (link.expected) {
        console.log(`   Expected: ${path.relative(DOCS_DIR, link.expected)}`);
      }
      console.log('');
    });

    process.exit(1);
  } else {
    console.log('\n✅ All internal links are valid!\n');
    process.exit(0);
  }
}

if (require.main === module) {
  main();
}

module.exports = { extractLinks, validateLink, getAllMdxFiles };
