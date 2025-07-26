# Pagination

**Pagination is a way to handle the structural inability to return all the results in a single HTTP request. For example, you may want to access the latest 2000 records from a total of 1 million.**

---

Unless noted otherwise, any endpoint where you **list models** (e.g. list Segments, Tours, etc.) supports the following pagination parameters.

| param | - | description |
|---|---|---|
| `limit` | optional | Defaults to `50` with a maximum of `500` |
| `before` | optional | Used when paginating, use directly from the `cursor` object from the previous response. Can also be given as a timestamp to get only `limit` items that were created before this time |
| `after`  | optional | Read as "created `after`" and can be given as a timestamp or ID to get only `limit` items that were created after this time |

By default, all models are returned with the **most recently created first** (aka descending order). The `before` and `after` parameters apply to that ordering.


## Examples

### Get up to 74 results created within the last 25 hours

```json
{
  "after": "2029-04-06T11:18:00Z",
  "limit": 74
}
```

### Get results created within the last 25 hours but not within the last hour

```json
{
  "before": "2029-04-07T11:18:00Z",
  "after": "2029-04-06T11:18:00Z"
}
```
