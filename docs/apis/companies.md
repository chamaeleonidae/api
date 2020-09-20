# Companies

**Companies represent your *accounts*: real customers who were identified to Chameleon. They can store complex (semi-arbitrary) properties.**

---

## Schema :id=schema

#### Fully-expanded company when listed directly or embedded with `expand` param specified properly

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `uid` | string | The external ID that came from your backend system |
| `*any options` | mixed | Any other options you have sent as Custom Properties will show up here too |


#### Non-expanded company when embedded in another (i.e. Microsurvey response)

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `uid` | string | The external ID that came from your backend system |


## Create / Update a Company :id=companies-create

See the [Companies Webhook](webhooks/companies.md) for sending User data to Chameleon


## List Companies :id=companies-index

List all Companies.

#### HTTP Request

```
GET|POST https://api.trychameleon.com/v3/analyze/companies
```

| param  | -        | description                                                  |
| ------ | -------- | ------------------------------------------------------------ |
| limit  | optional | Defaults to `50` with a maximum of `500`                     |
| before | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| before | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |
| after  | optional | Read as "created `after`" and can be given as a timestamp or ID to get only `limit` items that were created after this time |
| expand         | optional | Object that specifies relationships to include/exclude. Supported keys are `company`      |
| expand.company | optional | use values of `all`, `min` to control the properties present in the `company`. Defaults to `all` |

#### Using the `expand` parameter

```
# As a URL parameter
expand[profile]=min&expand[company]=skip

# In the Reqeust body
{"expand":{"profile":"min","company":"skip"}}
```


#### HTTP Response

```json
{
  "companies": [
    {
      "id": "5f3c4232c712de665632a6d5",
      "created_at": "2029-04-07T12:38:00Z",
      "uid": "1868",
      "domain": "example.com",
      "plan": "custom-92",
      "clv": 231902.42,
      ...
    },
    {
      "id": "5f3c4232c712de665632a2a1",
      "created_at": "2029-04-07T12:38:00Z",
      "uid": "2015",
      "domain": "trychameleon.com",
      "plan": "custom-12",
      "clv": 39102.17,
      ...
    },
    ...
  ],
  "cursor": {
    "limit": 50,
    "before": "5f3c4232c712de665632a2a1"
  }
}
```

## Retrieve a Company :id=companies-show

Retrieve a single Company.

#### HTTP Request

```
GET https://api.trychameleon.com/v3/analyze/companies/:id
# OR
GET https://api.trychameleon.com/v3/analyze/company?uid=:uid
```

| param | -        | description                                                  |
| ----- | -------- | ------------------------------------------------------------ |
| id    | optional | The Chameleon ID of the Company                         |
| uid   | optional | The Company identifier (typically the Database ID from your backend) |


```json
{
  "company": {
    "id": "5f3c4232c712de665632a2a1",
    "created_at": "2029-04-07T12:38:00Z",
    "uid": "1868",
    "domain": "example.com",
    "plan": "custom-92",
    "clv": 231902.42,
    ...
  }
}
```
