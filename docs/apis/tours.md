# Tours

A Tour is a sequence of steps that shows to your end-users when they meet all of the predefined matching criteria
 - First step URL (on the right page) - required
 - Segmentation matches (User is the right person) - required but can be to match All Users
 - Element appears on the page - optional
 - Element must be clicked on or hovered over - optional
 - etc.

## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `name` | string | The name given by an administrator of Chameleon |
| `style` | string | The delivery method of this Tour: One of `auto` or `manual` |
| `position` | number | The order that these appear in lists (starting from 0) |
| `tour_link_url` | string | When `style=manual` this URL is loaded to start the Tour |
| `experiment_at` | timestamp | When [Experimentation](https://help.trychameleon.com/en/articles/1069709-a-b-testing-chameleon-tours) was turned on. |
| `experiment_range` | string | The range of `Profile#percent` that will be included in the experiment |
| `segment_id` | ID | The Chameleon ID of the configured segment |
| `published_at` | timestamp | The time this was most recently published |
| `rate_unlimit_at` | timestamp | This item is excluded from [Rate limiting](https://help.trychameleon.com/en/articles/3513345-rate-limiting-experiences) |
| `stats` | object | Aggregated statistics for this model (all-time) |
| `stats.started_count` | number | Number of your end-users who saw this |
| `stats.last_started_at` | timestamp | Most recent time any user saw this |
| `stats.completed_count` | number | Number of your end-users who completed/finished this |
| `stats.last_completed_at` | timestamp | Most recent time any user completed/finished this |
| `stats.exited_count` | number | Number of your end-users who dismissed/exited this |
| `stats.last_exited_at` | timestamp | Most recent time any user dismissed/exited this |


## List Tours :id=campaigns-index

#### HTTP Request
`GET` to `https://api.trychameleon.com/v3/edit/tours`

| param | - | description |
|---|---|---|
| limit | optional | Defaults to `50` with a maximum of `500` |
| before | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| before | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |

#### HTTP Response

```json
{
  "tours": [
    {
      "id": "5f3c4232c712de665632a6d5",
      "name": "Revamped Dashboard Launch",
      "style": "auto",
      "position": 4,
      "published_at": "2029-04-07T12:18:00Z",
       ...
    },
    {
      "id": "5f3c4232c712de665632a2a1",
      "name": "Growth plan upsell banner 2029-02",
      "style": "auto",
      "position": 3,
      "published_at": "2029-04-07T12:18:00Z",
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

#### Filtering by Segment :id=filter-segment

See [Listing Related models](apis/segments.md?id=segment-experiences-index)

## Show a Tour :id=campaigns-show

Show a single Tour

#### HTTP Request

`GET` to `https://api.trychameleon.com/v3/edit/tours/:id`

| param | - | description |
|---|---|---|
| id | required | A Tour ID to lookup

```json
{
  "tour": {
    "id": "5f3c4232c712de665632a2a1",
    "name": "Growth plan upsell banner 2029-02",
    "style": "auto",
    "position": 3,
    "published_at": "2029-04-07T12:18:00Z",
    ...
  }
}
```

## List Tour Flows :id=tours-index

Coming soon
