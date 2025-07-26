# Tours

**A Tour is a sequence of steps that shows to your end-users when they meet all of the predefined matching criteria, including:**

- **First step URL (on the right page) - required**
- **Segmentation matches (User is the right person) - required but can be to match All Users**
- **Element appears on the page - optional**
- **Element must be clicked on or hovered over - optional**
- **etc.**

*To know more about Tours, you can visit our [product documentation](https://help.chameleon.io/en/collections/74747-tours).*

------



With the Chameleon API for Tours, you can:

- List all the existing  Tours according to the indicated parameters.
- Retrieve a single  Tour.



## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `archived_at` | timestamp | The time when this was archived |
| `name` | string | The name given by an administrator of Chameleon |
| `style` | string | The delivery method of this Tour: `auto` (triggers automatically based on conditions) or `manual` (requires manual triggering via URL or API) |
| `position` | number | The order that these appear in lists (starting from 0) |
| `tour_link_url` | string | When `style=manual` this URL is loaded to start the Tour |
| `experiment_at` | timestamp | When [Experimentation](https://help.chameleon.io/en/articles/1069709-a-b-testing-chameleon-tours) was turned on. |
| `experiment_range` | string | The range of `Profile#percent` that will be included in the experiment |
| `segment_id` | ID | The Chameleon ID of the configured [Segment](apis/segments.md?id=schema) |
| `published_at` | timestamp | The time this was most recently published |
| `tag_ids` | array&lt;ID&gt; | The Chameleon IDs of the [Tags](apis/tags.md) attached to this model |
| `rate_unlimit_at` | timestamp | This item is excluded from [Rate limiting](https://help.chameleon.io/en/articles/3513345-rate-limiting-experiences) |
| `stats` | object | Aggregated statistics for this model (all-time) |
| `stats.started_count` | number | Number of your end-users who saw this |
| `stats.last_started_at` | timestamp | Most recent time any user saw this |
| `stats.completed_count` | number | Number of your end-users who completed/finished this |
| `stats.last_completed_at` | timestamp | Most recent time any user completed/finished this |
| `stats.exited_count` | number | Number of your end-users who dismissed/exited this |
| `stats.last_exited_at` | timestamp | Most recent time any user dismissed/exited this |


## List Tours :id=campaigns-index

List all the  Tours that follow the specified parameters.

#### HTTP Request

```
GET https://api.chameleon.io/v3/edit/tours
```

| param  | -        | description                                                  |
| ------ | -------- | ------------------------------------------------------------ |
| `limit`  | optional | Defaults to `50` with a maximum of `500`                     |
| `before` | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| `before` | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |
| `after`  | optional | Read as "created `after`" and can be given as a timestamp or ID to get only `limit` items that were created after this time |

#### HTTP Response

```json
{
  "tours": [
    {
      "id": "5f3c4232c712de665632a6d5",
      "created_at": "2024-03-01T14:20:00.000Z",
      "updated_at": "2024-04-07T12:18:00.000Z",
      "archived_at": null,
      "name": "Dashboard Onboarding Tour",
      "style": "auto",
      "position": 1,
      "tour_link_url": null,
      "experiment_at": "2024-03-15T10:00:00.000Z",
      "experiment_range": "0,50",
      "segment_id": "5f3c4232c712de665632a6d9",
      "published_at": "2024-03-05T09:00:00.000Z",
      "tag_ids": ["5f3c4232c712de665632a6f5", "5f3c4232c712de665632a6f6"],
      "stats": {
        "started_count": 1247,
        "last_started_at": "2024-04-07T11:30:00.000Z",
        "completed_count": 892,
        "last_completed_at": "2024-04-07T11:15:00.000Z",
        "exited_count": 355,
        "last_exited_at": "2024-04-07T10:45:00.000Z"
      },
      "rate_unlimit_at": null
    },
    {
      "id": "5f3c4232c712de665632a2a1",
      "created_at": "2024-02-15T16:45:00.000Z",
      "updated_at": "2024-03-20T13:22:00.000Z",
      "archived_at": null,
      "name": "Feature Announcement - New Analytics",
      "style": "manual",
      "position": 2,
      "tour_link_url": "https://app.example.com/tours/feature-announcement",
      "experiment_at": null,
      "experiment_range": null,
      "segment_id": "5f3c4232c712de665632a6e1",
      "published_at": "2024-02-20T08:00:00.000Z",
      "tag_ids": ["5f3c4232c712de665632a6f7"],
      "stats": {
        "started_count": 456,
        "last_started_at": "2024-03-19T15:20:00.000Z",
        "completed_count": 387,
        "last_completed_at": "2024-03-19T14:55:00.000Z",
        "exited_count": 69,
        "last_exited_at": "2024-03-19T16:10:00.000Z"
      },
      "rate_unlimit_at": "2024-04-01T00:00:00.000Z"
    }
  ],
  "cursor": {
    "limit": 2,
    "before": "5f3c4232c712de665632a2a1"
  }
}
```

## Update a Tour :id=campaigns-update

Update a single Tour to change the [Environments](apis/urls.md) or to Publish it.

#### HTTP Request

```
PATCH https://api.chameleon.io/v3/edit/tours/:id
```

| param           | -        | description                                                                                     |
|-----------------|----------|-------------------------------------------------------------------------------------------------|
| `id`            | required | A Tour ID to update                                                                             |
| `urls_group_id` | optional | An [Environments](apis/urls.md) ID prefixed with `+` to add or or `-` to remove the Environment |
| `published_at`  | optional | The published time of this Tour (set to now to trigger a publish)                               |


To **Publish** the Tour send the current timestamp in `iso8601` format

```json
{
  "published_at": "2029-04-07T12:18:00Z"
}
```

To **Unpublish** the Tour set the `published_at` to `null`

```json
{
  "published_at": null
}
```

To **add** the `5e3c4232c712de666d55632a` Environment use a `+` prefix

```json
{
  "url_group_id": "+5e3c4232c712de666d55632a"
}
```


To **remove** the `5e3c4232c712de666d55632a` Environment use a `-` prefix

```json
{
  "url_group_id": "-5e3c4232c712de666d55632a"
}
```


## Filtering by Segment :id=filter-segment

See [Listing Related models](apis/segments.md?id=segment-experiences-index)

## Retrieve a Tour :id=campaigns-show

Retrieve a single Tour.

#### HTTP Request

```
GET https://api.chameleon.io/v3/edit/tours/:id
```

| param | -        | description         |
| ----- | -------- | ------------------- |
| `id`    | required | A Tour ID to lookup |

```json
{
  "tour": {
    "id": "5f3c4232c712de665632a6d5",
    "created_at": "2024-03-01T14:20:00.000Z",
    "updated_at": "2024-04-07T12:18:00.000Z",
    "archived_at": null,
    "name": "Dashboard Onboarding Tour",
    "style": "auto",
    "position": 1,
    "tour_link_url": null,
    "experiment_at": "2024-03-15T10:00:00.000Z",
    "experiment_range": "0,50",
    "segment_id": "5f3c4232c712de665632a6d9",
    "published_at": "2024-03-05T09:00:00.000Z",
    "tag_ids": ["5f3c4232c712de665632a6f5", "5f3c4232c712de665632a6f6"],
    "stats": {
      "started_count": 1247,
      "last_started_at": "2024-04-07T11:30:00.000Z",
      "completed_count": 892,
      "last_completed_at": "2024-04-07T11:15:00.000Z",
      "exited_count": 355,
      "last_exited_at": "2024-04-07T10:45:00.000Z"
    },
    "rate_unlimit_at": null
  }
}
```
