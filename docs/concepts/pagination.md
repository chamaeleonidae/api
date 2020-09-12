# Pagination / Filtering

Pagination is simply a way to handle structural inability to return all results in a single HTTP request. For example, ou may want to access the latest 2000 records of 1 million)

As a general rule any endpoint where you "List models" supports these pagination parameters (unless otherwise noted).

| param | - | description |
|---|---|---|
| limit | optional | Defaults to `50` with a maximum of `500` |
| before | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| before | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |
