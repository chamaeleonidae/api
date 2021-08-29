# Tags

**A Tag is a grouping of Experiences based on a readable name (i.e. `"Upsell"`, `"Feature"` etc.)**

Tags are:

- Used to Search and Filter experiences in the [Chameleon Dashboard](https://app.trychameleon.com).
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


```json
{
  "id": "5f3c4232c712de665632a5f1",
  "uid": "new_feature",
  "name": "New Feature",
  "description": "Any feature announcement",
  "models_count": 3,
  "disabled_at": null,
  "last_seen_at": "2029-04-07T12:18:00Z"
}
```
