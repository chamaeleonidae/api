# Authentication

Every request is to `api.trychameleon`, authenticated with the `X-Account-Secret` header with a Secret token [generated here](https://app.trychameleon.com/setup/integrations/api) and returns resource-specific keyed JSON. All tokens are generated per-user and can only be downloaded once. All APIs are accessed over SSL/HTTPS.

To check your Secret token simply make this request:

`curl -H "X-Account-Secret: ACCOUNT_SECRET" https://api.trychameleon.com`

To receive:

```json
{
  "account": {
    "id": "5f3c4232c712de665632a6d4"
  }
}
```