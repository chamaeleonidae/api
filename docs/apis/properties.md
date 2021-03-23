# Properties

**Properties track the specific data sent to Chameleon via custom data properties to [User Profiles](apis/profiles.md) or [Companies](apis/companies.md).**


## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `name` | string | The name given by an administrator of Chameleon |
| `description` | string | The display description |
| `kind` | string | Type of record this property is associated with: One of `profile`, `event`, or `company` |
| `prop` | string | The normalized property key |
| `integration` | string | The source integration of this property |
| `last_seen_at` | timestamp | The time when this property was last added to / removed from a User Profile. |
| `types` | array | The identified type of property values seen (string, integer etc.) |
| `values` | array | A sample of the most recent values seen for this property (most recent first). |


## Listing Properties :id=properties-index

Retrieve a complete (un-paginated) list of properties for the given `kind` + `integration`.

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/properties
```

| param  | -        | description                                                  |
| ------ | -------- | ------------------------------------------------------------ |
| `kind`        | required | Use a values of either `profile` or `company`                     |
| `integration` | optional | Used to filter properties to only ones created by a specific integration. Omit for "all integrations". |
| `order`       | optional | One of `created_at` or `last_seen_at`, ordered by most recent. Defaults to `created_at`. |


Custom User Profile properties
```json
{
  "kind": "profile",
  "integration": "api",
  "order": "last_seen_at"
}
```

Salesforce Company properties
```json
{
  "kind": "company",
  "integration": "salesforce"
}
```


#### HTTP Response

```json
{
  "properties": [
    {
      "id": "5f3c4232c712de665632a6d9",
      "name": "Monthly plan value (dollars USD)",
      "prop": "plan_cost",
      "types": ["integer"],
      "values": [678, 442, 1218, 239, 394],
      "last_seen_at": "2029-04-07T12:18:00Z"
    },
    {
      "id": "5f3c4232c712de665632a6e2",
      "name": "Lifetime value",
      ...
    },
    ...
  ]
}
```

