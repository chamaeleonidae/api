# Pagination

Pagination is a way to handle the structural inability to return all the results in a single HTTP request. For example, you may want to access the latest 2000 records from a total of 1 million.

---

Unless noted otherwise, any endpoint where you **list models** (e.g. list users, tours, etc.) supports the following pagination parameters.

| param | - | description |
|---|---|---|
| limit | optional | Defaults to `50` with a maximum of `500` |
| before | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| before | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |
