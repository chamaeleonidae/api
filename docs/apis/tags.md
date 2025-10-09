# Tags

**A Tag is a grouping of Experiences based on a readable name (i.e. `"Upsell"`, `"Feature"` etc.)**

Tags are:

- Used to Search and Filter Experiences in the [Chameleon Dashboard](https://app.chameleon.io).
- Used to define [Rate Limit Groups](apis/limit-groups.md) of Experiences that are limited to a particular rate limit (i.e. 2 per week, 3 per month etc.).
- [Normalized](concepts/normalization.md?id=tags) with the typical rules.

------


## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `uid` | string | The [normalized](concepts/normalization.md?id=tags) name. Or an external ID |
| `name` | string | The original text entered for the Tag |
| `description` | string | The display description |
| `models_count` | number | The number of [Experiences](apis/overview.md) attached to this Tag |
| `disabled_at` | timestamp | A timestamp indicating that this tag should no longer be displayed in the UI |
| `last_seen_at` | timestamp | This last time this Tag was added or removed from an Experience |



## Listing all Tags :id=tags-index

#### HTTP Request

```
GET https://api.chameleon.io/v3/edit/tags
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
  "tags": [
    {
      "id": "5f3c4232c712de665632a5f1",
      "uid": "new_features",
      "name": "New Features 🎉",
      "description": "Any feature announcement",
      "models_count": 3,
      "disabled_at": null,
      "last_seen_at": "2029-04-07T12:18:00Z"
    },
    {
      "id": "5f3c4232c712de665632a5f2",
      "uid": "01_onboarding",
      "name": "01 Onboarding 🚧",
      "description": "Any onboarding prompt",
      "models_count": 12,
      "disabled_at": null,
      "last_seen_at": "2029-04-09T12:19:00Z"
    },
    ...
  ],
  "cursor": {
    "limit": 50,
    "before": "5c4950c34733cc0004d5bfd2"
  }
}
```

## Filtering by Segment :id=filter-segment

See [Listing Related models](apis/segments.md?id=segment-experiences-index)


## Retrieve a Tag :id=tags-show

#### HTTP Request

```
GET https://api.chameleon.io/v3/edit/tags/:id
```

| param | -        | description                         |
|-------|----------|-------------------------------------|
| `id`  | required | The Chameleon ID of the Tag to show |

#### HTTP Response

```json
{
  "tag": {
    "id": "5f3c4232c712de665632a5f2",
    "uid": "01_onboarding",
    "name": "01 Onboarding 🚧",
    "description": "Any onboarding prompt",
    "models_count": 12,
    "disabled_at": null,
    "last_seen_at": "2029-04-09T12:19:00Z",
    ...
  }
}
```


## Bulk tag operations :id=tags-bulk

Apply multiple tag operations across multiple Experiences (Tours, Microsurveys, Tooltips, Launchers) in a single request. This endpoint is optimized for bulk updates.

**Check out [this guide](guides/scripts/bulk-tagging.md) with specific examples**

> A Tour, Microsurvey, and Embed is `model_type=Campaign` when used in this API

- Tags names are automatically [normalized](concepts/normalization.md?id=tags) when created
- If a tag name is provided that doesn't exist, it will be created automatically
- Multiple operations on the same model are applied in order
- When using `tag_names` array, the model's tags are set to exactly the specified list (tags not in the list are removed)
- Tag counts (`models_count`) are updated automatically
- The `last_seen_at` timestamp is updated for all affected tags

#### HTTP Request

```
POST https://api.chameleon.io/v3/edit/tags/bulk
```

| param     | -        | description                                  |
|-----------|----------|----------------------------------------------|
| `updates` | required | An array of tag update operations to perform |

Each update operation can use one of three formats:

**1. Individual tag operations by ID** - Add or remove a specific tag using its Chameleon ID:

| Property     | Type   | Description                                                                                                                 |
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------|
| `model_id`   | ID     | The Chameleon ID of the model to update                                                                                     |
| `model_type` | string | The type of model: `Campaign`, `Tooltip`, `List` (Microsurveys and Embeddables are considered a Campaign here)              |
| `tag_id`     | string | The tag ID prefixed with `+` to add or `-` to remove (e.g., `"+5f3c4232c712de665632a5f1"` or `"-5f3c4232c712de665632a5f1"`) |

**2. Individual tag operations by name** - Create (if needed) and add or remove a tag by name:

| Property     | Type   | Description                                                                                                    |
|--------------|--------|----------------------------------------------------------------------------------------------------------------|
| `model_id`   | ID     | The Chameleon ID of the model to update                                                                        |
| `model_type` | string | The type of model: `Campaign`, `Tooltip`, `List` (Microsurveys and Embeddables are considered a Campaign here) |                                      |
| `tag_name`   | string | The tag name prefixed with `+` to add or `-` to remove (e.g., `"+Feature"` or `"-Bug"`)                        |

**3. Set exact tags by names** - Replace all tags on a model with the specified set:

| Property     | Type                | Description                                                                                                    |
|--------------|---------------------|----------------------------------------------------------------------------------------------------------------|
| `model_id`   | ID                  | The Chameleon ID of the model to update                                                                        |
| `model_type` | string              | The type of model: `Campaign`, `Tooltip`, `List` (Microsurveys and Embeddables are considered a Campaign here) |                                                     |
| `tag_names`  | array&lt;string&gt; | Array of tag names to set (creates tags if needed). The model's tags will be set to exactly this list          |

#### HTTP Response

Returns an array of updated models with their final tag state:

```json
{
  "updates": [
    {
      "model_id": "5f3c4232c712de665632a3b1",
      "model_type": "Campaign",
      "tag_ids": ["5f3c4232c712de665632a5f1", "5f3c4232c712de665632a5f2"]
    },
    {
      "model_id": "5f3c4232c712de665632a3b2",
      "model_type": "Tooltip",
      "tag_ids": ["5f3c4232c712de665632a5f1"]
    }
  ]
}
```

#### Examples

**Add multiple tags to different models:**

```json
{
  "updates": [
    {
      "model_id": "5f3c4232c712de665632a3b1",
      "model_type": "Campaign",
      "tag_id": "+5f3c4232c712de665632a5f1"
    },
    {
      "model_id": "5f3c4232c712de665632a3b1",
      "model_type": "Campaign",
      "tag_id": "+5f3c4232c712de665632a5f2"
    },
    {
      "model_id": "5f3c4232c712de665632a3b2",
      "model_type": "Tooltip",
      "tag_name": "+NewFeature"
    }
  ]
}
```

**Remove tags from a model:**

```json
{
  "updates": [
    {
      "model_id": "5f3c4232c712de665632a3b1",
      "model_type": "Campaign",
      "tag_id": "-5f3c4232c712de665632a5f1"
    }
  ]
}
```

**Set exact tags on a model:**

```json
{
  "updates": [
    {
      "model_id": "5f3c4232c712de665632a3b1",
      "model_type": "Campaign",
      "tag_names": ["Feature", "Onboarding", "Priority"]
    }
  ]
}
```

This will remove any tags not in the list and add any tags that are in the list but not currently on the model. Tags are created automatically if they don't exist.

**Mix operation types:**

```json
{
  "updates": [
    {
      "model_id": "5f3c4232c712de665632a3b1",
      "model_type": "Campaign",
      "tag_names": ["Feature", "Enhancement"]
    },
    {
      "model_id": "5f3c4232c712de665632a3b2",
      "model_type": "Tooltip",
      "tag_id": "+5f3c4232c712de665632a5f1"
    },
    {
      "model_id": "5f3c4232c712de665632a3b3",
      "model_type": "Campaign",
      "tag_name": "+Bug"
    }
  ]
}
```
