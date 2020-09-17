# Companies (Incoming Webhook)

**Send Company data to Chameleon from services like Customer.io, Heap, Zapier or from you own backend.** Looking for the [JavaScript API](js/profiles.md?id=company)?

------

A Company that does not yet exist by `uid` will first be created and then updated with the other data included in this request.

> Company data updates are processed synchronously on the application server.



## Create/Update a Company

- When you are creating the Company, simply send the `uid` and any other properties pertinent to that company.
- When you are updating the Company, simply send the Chameleon `id` field or use the `uid` and any other properties pertinent to that company.



#### HTTP Request

```
POST https://api.trychameleon.com/v3/observe/hooks/companies
# OR
POST https://api.trychameleon.com/v3/observe/hooks/:account_secret/companies
```

| param   | -        | description                                                  |
| ------- | -------- | ------------------------------------------------------------ |
| id      | optional | The Chameleon ID of the Company                              |
| uid     | optional | The Company Identifier (typically the Database ID from your backend) |
| *others | optional | All other properties will be stored on the Company           |

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

- Up to a total of 768 bytes are stored for each scalar value where each Array item and each Hash value can reach this limit.
- See the full page on [Limits](concepts/normalization.md?id=limits) for more information.



## Normalization

- Property names are normalized to lower case and underscored i.e. `planName` => `plan_name`.
- See the full page on [Normalization](concepts/normalization.md?id=properties) for more information.

