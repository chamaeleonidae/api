# Microsurveys

**Chameleon Microsurveys are a primary *question* step that allows you to get immediate and contextual user feedback.** 

*To know more about Surveys, you can visit our [product documentation](https://help.trychameleon.com/en/collections/1752073-surveys).*

------



With the Chameleon Microsurveys API, you can:

- List all microsurveys that follow your indicated parameters.
- Retrieve a single microsurvey using its `id`.



## Schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `name` | string | The name given by an administrator of Chameleon |
| `position` | number | The order that these appear in lists (starting from 0) |
| `segment_id` | ID | The Chameleon ID of the configured [Segment](apis/segments.md?id=schema) |
| `published_at` | timestamp | The time this was most recently published |
| `rate_unlimit_at` | timestamp | This item is excluded from [Rate limiting](https://help.trychameleon.com/en/articles/3513345-rate-limiting-experiences) |
| `stats` | object | Aggregated statistics for this model (all-time) |
| `stats.started_count` | number | Number of your end-users who saw this |
| `stats.last_started_at` | timestamp | Most recent time any user saw this |
| `stats.completed_count` | number | Number of your end-users who completed/finished this |
| `stats.last_completed_at` | timestamp | Most recent time any user completed/finished this |
| `stats.exited_count` | number | Number of your end-users who dismissed/exited this |
| `stats.last_exited_at` | timestamp | Most recent time any user dismissed/exited this |

## List Microsurveys

List all Microsurveys that follow your indicated parameters.

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/surveys
```

| param  | -        | description                                                  |
| ------ | -------- | ------------------------------------------------------------ |
| limit  | optional | Defaults to `50` with a maximum of `500`                     |
| before | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| before | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |



#### HTTP Response

```json
{
  "surveys": [
    {
      "id": "5f3c4232c712de665632a6d5",
      "name": "Task #2 completion CES",
      "position": 1,
      "published_at": "2029-04-07T12:18:00Z",
       ...
    },
    {
      "id": "5f3c4232c712de665632a2a3",
      "name": "Admin account setup #1 completion question",
      "position": 0,
      "published_at": "2029-04-07T12:38:00Z",
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



## Filtering by Segment :id=filter-segment

See [Listing Related Models](apis/segments.md?id=segment-experiences-index).

## Retrieve a Microsurvey

Retrieve a single Microsurvey.

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/surveys/:id
```


| param | -        | description                |
| ----- | -------- | -------------------------- |
| id    | required | A Microsurvey ID to lookup |

```json
{
  "survey": {
    "id": "5f3c4232c712de665632a2a1",
    "name": "Admin Self-serve menu",
    "position": 0,
    "published_at": "2029-04-07T12:38:00Z",
    ...
  }
}
```
