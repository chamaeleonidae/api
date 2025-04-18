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
POST https://api.chameleon.io/v3/observe/hooks/companies
# OR
POST https://api.chameleon.io/v3/observe/hooks/:account_secret/companies
```

| param   | -        | description                                                          |
|---------|----------|----------------------------------------------------------------------|
| `id`    | optional | The Chameleon ID of the Company                                      |
| `uid`   | optional | The Company Identifier (typically the Database ID from your backend) |
| *others | optional | All other properties will be stored on the Company                   |

```json
{
  "uid": "18821",
  "domain": "chmln.co",
  "name": "Leon Inc.",
  "plan": "Growth",
  "clv": 24920,
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


### Limits

- Up to a total of 768 bytes are stored for each scalar value where each Array item and each Hash value can reach this limit.
- See the full page on [Normalization](concepts/normalization.md?id=limits) for more information on these limits.

### Normalization

- Property names are normalized to lower case and underscored i.e. `companyName` => `company_name`.
- See the full page on [Normalization](concepts/normalization.md?id=properties) for more information on how properties are normalized.


## Bulk Create/Update Companies :id=companies-bulk

- When sending a bulk create/update, send an array of Company objects as the `companies` parameter
- For each Company, send the Company ID as `uid` and any other properties pertinent to that Company.

#### HTTP Request

```
POST https://api.chameleon.io/v3/observe/hooks/companies/batch
# OR
POST https://api.chameleon.io/v3/observe/hooks/:account_secret/companies/batch
```

| param              | -                    | description                                                                                                                              |
|--------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `companies`        | array&lt;Company&gt; | The list of Companies to update; each item has the same schema as the [Single Company update](webhooks/companies.md?id=companies-update) |
| `on_model_missing` | optional        m    | The treatment of Companies not previously sent to Chameleon. Defaults to `create`. One of `create`, `ignore`                             |

```json
{
  "companies": [
    {
      "uid": 18821,
      "domain": "acme.ai",
      "last_import_at": "2029-04-07T12:18:00Z",
      "number_of_employees": 73,
      ...
    },
    {
      "uid": 28421,
      "domain": "highlighter.com",
      "last_import_at": "2029-04-02T16:11:06Z",
      "number_of_employees": 42,
      ...
    },
    ...
  ]
}
```


#### HTTP Response

```json
{
  "batch": {
    "id": "7f332c712de6c4265632a32a"
  }
}
```

#### HTTP Response error

When the 930th item had no value for the `uid` key

Note: The status code will be the normal 202 for (Accepted for processing)

```json
{
  "batch": {
    "id": "7f332c712de6c4265632a32a"
  },
  "errors": [
    {
      "code": 422,
      "index": 929,
      "message": "No identifier found for the 930th item. Pass your Company ID as the `uid` parameter"
    }
  ]
}
```

## Limits

- The size of each batch request is limited to 16mb
- As with the [Single Company update](webhooks/companies.md?id=companies-update), up to a total of 768 bytes are stored for each scalar value where each Array item and each Hash value can reach this limit.
- See the full page on [Normalization](concepts/normalization.md?id=limits) for more information on these limits.

#### Examples

> Either set the number of items per batch to _10,000_ OR to approximate the number of
> items per batch (based on the average payload size), divide (16777216 / "Average characters in JSON payload per item") * 0.95

With the following update, you can send approximately _257,000 Companies_ per batch request

```json
{
  "uid": "20ee87e2-f144-4611-8c24-e41549573fa9",
  "plan": "bronze"
}
```

With the following update, you can send approximately _47,000 Companies_ per batch request

```json
{
  "uid": "20ee87e2-f144-4611-8c24-e41549573fa9",
  "domain": "acme.ai",
  "company_name": "Jane",
  "last_name": "Chameleon",
  "last_login": "2029-04-29T09:00:00.000Z",
  "subscription_type": "platinum",
  "buyer_role": "CRO",
  "plan": "longer than normal plan name",
  "industry": "SaaS",
  "number_of_employees": 70,
  "founded_year": 2029,
  "annual_revenue": 57000000
}
```

#### HTTP Response error

When the request was larger than 16mb. The status code will be 413 (Request too large)

```json
{
  "code": 413,
  "messages": ["Each batch must be less than 16mb, try splitting the batch in half"]
}
```
