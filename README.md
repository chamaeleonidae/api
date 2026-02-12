# Chameleon API Docs

Documentation for the Chameleon API, hosted at [developers.chameleon.io](https://developers.chameleon.io).

## Local Development

Documentation is built with [Mintlify](https://mintlify.com). To run locally:

```bash
# Install Mintlify CLI
npm install -g mintlify

# Start local dev server
cd mintlify-docs
mintlify dev
```

This starts a local server at http://localhost:3000.

## Making Changes

1. Edit `.mdx` files in `mintlify-docs/`
2. Update `mint.json` for navigation changes
3. Commit and push to `main` - Mintlify auto-deploys
