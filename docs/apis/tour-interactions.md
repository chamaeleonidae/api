# Tour Interactions

**A Tour Interaction is a state object which contains the current view of a Tour for a specific User Profile.**

------



With the Chameleon API, you can list Tour Interactions that follow the specified parameters.

## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `state` | string | The current state of this Tour Interaction: One of `started`, `completed`, `exited`, or `displayed` |
| `tour_id` | ID | The Chameleon ID of the [Tour](apis/tours.md) |
| `group_id` | ID | The Chameleon ID of the parent Experience that triggered this Tour Interaction to begin (Launcher, Tour etc.) |
| `group_kind` | string | The kind of parent Experience that triggered this Tour Interaction to begin: One of `link`, `api_js`, `launcher`, `experiment`, or `campaign` |
| `defer_count` | number | The number of times this Tour was snoozed until later |
| `defer_until` | none | The timestamp of when the snoozed ends |
| `goal_at` | timestamp | The timestamp of when the configured Goal was met |
| `profile` | object | An expandable [Profile](apis/profiles.md) model |
| `profile.company` | none | An expandable [Company](apis/companies.md) model embedded in the profile |

## List Tour Interactions :id=tour-interactions-index

#### HTTP Request

```
GET  https://api.trychameleon.com/v3/analyze/interactions
```

| param          | -        | description                                                  |
| -------------- | -------- | ------------------------------------------------------------ |
| `id`             | required | The Chameleon ID of the Tour                                 |
| `limit`          | optional | Defaults to `50` with a maximum of `500`                     |
| `before`         | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| `before`         | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |
| `after`          | optional | Read as "created `after`" and can be given as a timestamp or ID to get only `limit` items that were created after this time |
| `order`          | optional | One of `created_at` or `updated_at`. Defaults to `created_at` (the ID encodes this information). |
| `expand`         | optional | Object that specifies relationships to include/exclude. Supported keys are `profile` and `company`      |
| `expand.profile` | optional | use values of `all`, `min` or `skip` to control the properties present in the `profile`. Defaults to `min` |
| `expand.company` | optional | use values of `all`, `min` or `skip` to control the properties present in the `company`. Defaults to `min` |

#### Using the `expand` parameter

```
# As a URL parameter
expand[profile]=all&expand[company]=skip

# In the Reqeust body
{"expand":{"profile":"all","company":"skip"}}
```

Notes:
- A `profile` key will always be present with an object value. The `company` (embedded within `profile`) will be missing when the User Profile is not attached to a Company, otherwise it will be an object.
- The combination of `before` and `after` can be used to limit pagination to "stop" at your most recently cached Tour Interaction (send the max ID from your last import as the `after` parameter).


#### HTTP Response

```json
{
  "interactions": [
    {
      "id": "5f3c4232c712de665632a6d5",
      "updated_at": "2029-04-07T11:18:00Z",
      "tour_id": "5f3c4232c712de665632a6d6",
      "state": "completed",
      "goal_at": "2029-04-07T12:18:00Z",
      "profile": {
        "id": "5f3c4232c712de665632a6d5",
        "uid": "55232",
        ...
      },
      ...
    },
    {
      "id": "5f3c4232c712de665632a2a3",
      "updated_at": "2029-04-07T11:18:00Z",
      "tour_id": "5f3c4232c712de665632a6d6",
      "state": "started",
      "goal_at": "2029-04-07T12:18:00Z",
      "profile": {
        "id": "5f3c4232c712de665632a6d8",
        "uid": "55233",
        ...
      },
      ...
    },
    ...
  ],
  "cursor": {
    "limit": 50,
    "before": "5f3c4232c712de665632a2a3"
  }
}
```

