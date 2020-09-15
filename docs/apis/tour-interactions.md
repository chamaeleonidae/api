# Tour Interactions

**A Tour Interaction is a state object which contains the current view of a Tour for a specific User Profile.**

------



With the Chameleon API, you can list Tour Interactions that follow the specified parameters.

## Schema :id=schema

| Property      | Type      | Description                                                  |
| ------------- | --------- | ------------------------------------------------------------ |
| `id`          | ID        | The Chameleon ID                                             |
| `created_at`  | timestamp | When this happened or when this was added to the Database    |
| `updated_at`  | timestamp | The last time any property was updated                       |
| `state`       | string    | The current state of this Tour Interaction: One of `started`, `completed`, `exited`, or `displayed` |
| `tour_id`     | ID        | The Chameleon ID of the Tour                                 |
| `group_id`    | ID        | The Chameleon ID of the parent Experience that triggered this Tour Interaction to begin |
| `group_kind`  | string    | The kind of parent Experience that triggered this Tour Interaction to begin: One of `link`, `api_js`, `launcher`, `experiment`, or `campaign` |
| `defer_count` | number    | The number of times this Tour was snoozed until later        |
| `defer_until` | timestamp | The timestamp of when the snoozed ends                       |
| `goal_at`     | timestamp | The timestamp of when the configured Goal was met            |
| `profile`     | object    | An expandable [Profile](https://github.com/chamaeleonidae/api/blob/master/docs/apis/apis/profiles.md) model |

## List Tour Interactions :id=tour-interactions-index

#### HTTP Request

`GET` to `https://api.trychameleon.com/v3/analyze/interactions`

| param          | -        | description                                                  |
| -------------- | -------- | ------------------------------------------------------------ |
| id             | required | The Chameleon ID of the Tour                                 |
| limit          | optional | Defaults to `50` with a maximum of `500`                     |
| before         | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| before         | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |
| expand         | optional | Object that specifies relationships to include/exclude.      |
| expand.profile | optional | use values of `all` or `none` control the properties present in the `profile`. Defaults to a minimal representation |

#### HTTP Response

```
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

