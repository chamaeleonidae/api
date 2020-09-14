# Authentication
---

## Basics

Every request uses the base URL of `api.trychameleon`, is authenticated with either the `X-Account-Secret` header or `account_secret` parameter and uses `https://`. Endpoints return singular/plural top-level resource names depending on the requested resource. Your Secret token can be [generated here](https://app.trychameleon.com/setup/integrations/api). All tokens are Account-specific but can only be downloaded once.

To check your Account Secret token simply make this request:

- `curl -H "X-Account-Secret: ACCOUNT_SECRET" https://api.trychameleon.com`
- `curl https://api.trychameleon.com?account_secret=ACCOUNT_SECRET`
- `curl -X POST -d {"account_secret":"ACCOUNT_SECRET"} https://api.trychameleon.com`

To receive:

```json
{
  "account": {
    "id": "5f3c4232c712de665632a6d4"
  },
  "user": {
    "id": "5f3c4232c712de665632a6d9"
  }
}
```

## Versioning

The current API version is `v3` and each API has an environment name included in the URL. For example:

- `https://api.trychameleon.com/v3/edit/segments` operates in the Edit environment.
- `https://api.trychameleon.com/v3/observe/hooks/event` operates in the Observe environment.
- `https://api.trychameleon.com/v3/analyze/profiles` operates in the Analyze environment.
