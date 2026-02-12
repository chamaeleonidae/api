# Embeddables

**An Embeddable is a persistent, in-app widget that can be embedded directly into your product's UI. Unlike Tours that appear as overlays, Embeddables are rendered inline within your application and remain visible to users as they interact with your product.**

- **URL matching - the page must match the configured URL conditions.**
- **Segmentation matches (User is the right person) - required but can be to match All Users.**
- **Element targeting - Embeddables are rendered relative to a specific element on the page.**



*To know more about Embeddables, feel free to visit our [product documentation](https://help.chameleon.io/en/collections/9028912-embeddables).*

------



With the Chameleon API for Embeddables, you can:

- List all the Embeddables that follow a specified set of parameters.
- Retrieve a single Embeddable based on the `id`.
- Update an Embeddable to change Environments or publish/unpublish it.



## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `archived_at` | timestamp | The time when this was archived |
| `name` | string | The name given by an administrator of Chameleon |
| `description` | string | The internal description for this Embeddable |
| `style` | string | The delivery method of this Embeddable: One of `auto` or `manual` |
| `position` | number | The order that these appear in lists (starting from 0) |
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


## List Embeddables :id=embeddables-index

List all the Embeddables that follow a specified set of parameters.

#### HTTP Request

```
GET https://api.chameleon.io/v3/edit/embeds
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
  "embeds": [
    {
      "id": "5f3c4232c712de665632a6d5",
      "name": "Feature Announcement Banner",
      "style": "auto",
      "position": 1,
      "published_at": "2029-04-07T12:18:00Z",
       ...
    },
    {
      "id": "5f3c4232c712de665632a2a1",
      "name": "Upgrade Prompt Card",
      "style": "auto",
      "position": 0,
      "published_at": "2029-04-07T12:38:00Z",
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

## Update an Embeddable :id=embeddables-update

Update a single Embeddable to change its properties or to Publish it.

#### HTTP Request

```
PATCH https://api.chameleon.io/v3/edit/embeds/:id
```

| param          | -        | description                                                                                      |
|----------------|----------|--------------------------------------------------------------------------------------------------|
| `id`           | required | An Embeddable ID to update                                                                       |
| `url_group_id` | optional | An [Environments](apis/urls.md) ID prefixed with `+` to add or or `-` to remove the Environment  |
| `tag_id`       | optional | A [Tag](apis/tags.md) ID prefixed with `+` to add or or `-` to remove the Tag                    |
| `published_at` | optional | The published time of this Embeddable (set to now to trigger a publish)                          |


To **Publish** the Embeddable send the current timestamp in `iso8601` format

```json
{
  "published_at": "2029-04-07T12:18:00Z"
}
```

To **Unpublish** the Embeddable set the `published_at` to `null`

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

## Retrieve an Embeddable :id=embeddables-show

Retrieve a single Embeddable.

#### HTTP Request

```
GET https://api.chameleon.io/v3/edit/embeds/:id
```

| param | -        | description               |
| ----- | -------- | ------------------------- |
| `id`  | required | An Embeddable ID to lookup |

```json
{
  "embed": {
    "id": "5f3c4232c712de665632a2a1",
    "name": "Feature Announcement Banner",
    "style": "auto",
    "position": 0,
    "published_at": "2029-04-07T12:38:00Z",
    ...
  }
}
```
