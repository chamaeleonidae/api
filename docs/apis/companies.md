# Companies

**Companies represent your *accounts*: real customers who were identified to Chameleon. They can store complex (semi-arbitrary) properties.**

> For a full list of your User / Company Properties see the [Properties API](apis/properties.md)

---

## Schema :id=schema

#### Fully-expanded [Company](apis/companies.md) when listed directly or embedded with `expand` param specified properly

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `uid` | string | The external ID that came from your backend system |
| `*any options` | mixed | Any other options you have sent as Custom Properties will show up here too |


#### Non-expanded [Company](apis/companies.md) when embedded in another (i.e. Microsurvey response)

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `uid` | string | The external ID that came from your backend system |


## Create / Update a Company :id=companies-create

See the [Companies Webhook](webhooks/companies.md) for sending User data to Chameleon


## Retrieve a Company :id=companies-show

Retrieve a single Company.

#### HTTP Request

```
GET https://api.chameleon.io/v3/analyze/companies/:id
# OR
GET https://api.chameleon.io/v3/analyze/company?uid=:uid
```

| param | -        | description                                                  |
| ----- | -------- | ------------------------------------------------------------ |
| `id`    | optional | The Chameleon ID of the Company                         |
| `uid`   | optional | The Company identifier (typically the Database ID from your backend) |


```json
{
  "company": {
    "id": "5f3c4232c712de665632a2a1",
    "created_at": "2024-01-10T08:00:00.000Z",
    "updated_at": "2024-04-07T12:38:00.000Z",
    "uid": "company_abc123",
    "name": "Acme Corporation",
    "domain": "acmecorp.com",
    "plan": "enterprise",
    "subscription_status": "active",
    "clv_amount": 45000.00,
    "yearly_spend_base_amount": 12000.00,
    "users_count": 127,
    "tours_published_count": 8,
    "surveys_published_count": 3,
    "lists_published_count": 2,
    "tooltips_published_count": 15,
    "segments_count": 12,
    "searches_count": 5,
    "searches_published_count": 3,
    "search_groups_count": 2,
    "search_group_integrations": ["chameleon", "salesforce"],
    "search_items_count": 23,
    "alert_groups_count": 2,
    "limit_groups_count": 1,
    "url_groups_count": 4,
    "events_published_count": 6,
    "agent_runs_published_count": 0,
    "signup_source": "sales_team",
    "customer_stripe_url": "https://dashboard.stripe.com/customers/cus_ExampleCustomer123",
    "link_customers": "https://app.chameleon.io/customers/company_abc123",
    "link_intercom": "https://app.intercom.com/a/apps/example/companies/company_abc123/users",
    "mtus_included_count": 10000,
    "elements_sampling_rate": 1.0,
    "rights": ["ai_experiences", "attached_elements", "demos_consented", "experiment", "publish", "secure_mode", "themes", "users_unlimited", "webhook_all"],
    "revision": "v9",
    "product_features": ["advanced_analytics", "custom_branding"],
    "configs_content_enabled": "typeform",
    "configs_dest_enabled": "segment",
    "first_experience_published_at": "2024-01-15T10:00:00.000Z",
    "last_experience_published_at": "2024-03-28T14:30:00.000Z",
    "last_invoice_paid_at": "2024-04-01T09:00:00.000Z",
    "last_invoice_paid_amount": 1000.00,
    "subscription_interval": "monthly",
    "subscription_started_at": "2024-01-10T08:00:00.000Z"
  }
}
```

## List Companies :id=companies-index

List all Companies.

#### HTTP Request

```
GET|POST https://api.chameleon.io/v3/analyze/companies
```

| param  | -        | description                                                  |
| ------ | -------- | ------------------------------------------------------------ |
| `limit`  | optional | Defaults to `50` with a maximum of `500`                     |
| `before` | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| `before` | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |
| `after`  | optional | Read as "created `after`" and can be given as a timestamp or ID to get only `limit` items that were created after this time |
| `expand`         | optional | Object that specifies relationships to include/exclude. Supported keys are `company`      |
| `expand.company` | optional | use values of `all`, `min` to control the properties present in the `company`. Defaults to `all` |

#### Using the `expand` parameter

```
# As a URL parameter
expand[profile]=min&expand[company]=skip

# In the Request body
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
      "domain": "chameleon.io",
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


### Search Companies :id=companies-search

Searching Companies through the Chameleon API allows you to:

- Search for a company by `id` and `uid`

> *Note: [Rate Limiting](concepts/rate-limiting.md) applies according to the table below.*

| endpoint           | Maximum concurrent requests |
|--------------------| --------------------------- |
| `/companies`       | 2                           |


#### Examples :id=companies-search-examples

All of these examples are based directly on the full schema of [Segmentation Filter Expressions](concepts/filters.md).

Each example below is showing the value for the `filters` key in the JSON request body:

```json
{
  "filters": [
    ...
  ]
}
```

##### Companies that have a specific uid

Find the company with the `uid` of `123`:

```json
{
  "filters": [
    {
      "kind": "property",
      "prop": "uid",
      "op": "eq",
      "value": "123"
    }
  ]
}
```

```bash
curl -H "X-Account-Secret: ACCOUNT_SECRET" \
     -H "Content-Type: application/json" \
     -X POST \
     -d '{"filters":[{"kind":"property","prop":"uid","op":"eq","value":"123"}]}' \
     https://api.chameleon.io/v3/analyze/companies
```

## Delete a Company :id=companies-delete

When deleting a company, the company record itself is deleted and company is removed from all profiles associated with it. 
The associated profiles can also be removed by passing `cascade=profiles` with the request.

| param.  | -        | description                                                          |
| ------- | -------- | -------------------------------------------------------------------- |
| `id`    | optional | The Chameleon ID of the [Company](apis/companies.md)                 |
| `uid`   | optional | The Company identifier (typically the Database ID from your backend) |


#### HTTP Request

Either `id` or `uid` is required.

```
DELETE https://api.chameleon.io/v3/edit/companies/:id
# OR
DELETE https://api.chameleon.io/v3/edit/company?uid=:uid
```

#### HTTP Response

The endpoint returns `id` of the Deletion record.
The Deletion is an internal Chameleon record that can be referenced as proof of initiating this request.
   
```json
{
  "deletion": {
    "id": "5f3c4232c712de665632a6d5"
  }
}
```

### Deleting a company and all profiles associated with it
Deleting a company and all profiles associated with it can be done by passing `cascade=profiles`:

```
DELETE https://api.chameleon.io/v3/edit/companies/:id?cascade=profiles
# OR
DELETE https://api.chameleon.io/v3/edit/company?uid=:uid&cascade=profiles
```

#### HTTP Response

When cascade deletion is requested, the endpoint also returns deletion ids of all the profiles associated with the company under `deletions` key. 

```json
{
  "deletion": {
    "id": "5f3c4232c712de665632a6d5"
  },
  "deletions": [
    { "id":  "5f3c4232c712de665632a6d6" },
    { "id":  "5f3c4232c712de665632a6d7" },
    { "id":  "5f3c4232c712de665632a6d8" }
  ]
}
```
