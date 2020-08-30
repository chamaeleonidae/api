# Incoming Webook: Companies

Send Company data **into Chameleon**  from services like Customer.io, Heap, Zapier or from you own backend

Company data updates are processed synchronously on the application server

## Create/Update a Company

#### HTTP Request
`POST` to `https://api.trychameleon.com/v3/observe/hooks/companies`

| param | - | description |
|---|---|---|
| id | optional | The Chameleon ID of the Company |
| uid | optional | The Company Identifier (typically the Database ID from your backend) |
| *others | optional | All other properties will be stored on the Company |

```json
{
  "uid": "18821",
  "domain": "chmln.co",
  "name": "Leon Inc.",
  "plan": "Growth",
  "clv": "24920",
  "last_action_at": "2029-04-07T12:18:00Z",
   ...
}
```

#### HTTP Response

```json
{
  "company": {
    "id": "5f3c4232c712de665632a2a3"
  }
}
```

## Limits

- Up to a total of 768 bytes are stored for each scalar value where each Array item and each Hash value can reach this limit
- See the full page on [Limits](concepts/normalization.md?id=limits) for more info

## Normalization

- Property names are normalized to lower case and underscored i.e. `planName` => `plan_name`
- See the full page on [Normalization](concepts/normalization.md?id=properties) for more info
