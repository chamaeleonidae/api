# Authentication

**Authentication is necessary to access the Chameleon API. To authenticate, you will need to retrieve an account-specific secret token.**

---

## Basics

Every request uses the base URL of `api.trychameleon`, is authenticated with either the `X-Account-Secret` header or `account_secret` parameter and uses `https://`. Endpoints return singular/plural top-level resource names depending on the requested resource.
Your secret token can be [generated here](https://app.chameleon.io/settings/tokens). All tokens are account-specific and can only be downloaded once. Make sure you keep your secret token secure. Do not share it in public accessible areas, as it represents the right to access your data.

To check your Account Secret token simply make this request:

- `curl -H "X-Account-Secret: ACCOUNT_SECRET" https://api.chameleon.io`
- `curl https://api.chameleon.io?account_secret=ACCOUNT_SECRET`
- `curl -X POST -d '{"account_secret":"ACCOUNT_SECRET"}' https://api.chameleon.io`

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

## Versioning :id=version

The current API version is `v3` and each API has an environment name included in the URL. For example:

- `https://api.chameleon.io/v3/edit/segments` operates in the Edit environment.
- `https://api.chameleon.io/v3/observe/hooks/event` operates in the Observe environment.
- `https://api.chameleon.io/v3/analyze/profiles` operates in the Analyze environment.


## IP Addresses :id=ip-addresses

Chameleon will use a defined set of IP Addresses to send webhooks and any other traffic **from** Chameleon.
Consider the list below to be static; any updates will be posted to our [Status Page](https://status.chameleon.io).

```text
34.206.31.185
54.198.191.211
54.211.111.28
54.237.132.170
```


> Note: Traffic into Chameleon's services will not adhere to this list and will mostly resolve to [Fastly](https://www.fastly.com/).
