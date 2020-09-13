# Rate limiting

Rate limiting is crucial to the timely handling of all critical requests. Chameleon sets very high limits on the number of requests total and the amount of concurrency we support.
At this time, we only enforce rate limiting for [User Profile Searching](apis/profiles-search.md) with `max_concurrent` or in situations where the API is being abused in some way.

> When enforcing Rate limiting, both a header and a response body will give you information about the violation
> The `max_concurrent` strategy will queue for up to 4 seconds to allow other concurrent requests to complete. If no request completes during that initial 4 second wait, a 429 response will be sent.

| Strategy | Header | Example value | description |
|---|---|---|---|
| max_concurrent | `X-Ratelimit-Limit` | 4 | Up to N requests can be "running" at the same time. Wait for at least 1 request to complete before retrying. |
| bucket | `X-Ratelimit-Wait` | 12 | Up to N requests can have started within the time window. Pause for N seconds before retrying your request. |

When Limiting based on a **total number of requests**, the bucket window expires after N seconds. We give a `X-Ratelimit-Wait` header with N number of seconds. This is the number of seconds to pause for until requests can proceed without immediate rate limiting.
When Limiting based on a **maximum concurrent requests**, we subtract and add from an N-sized bucket. We give a `X-RateLimit-Limit` header with N number of current requests when that limit is reached. Please wait until at least one of the outstanding requests finishes


#### HTTP Response

```text
X-Ratelimit-Wait: 12
```

```json
{
  "code": 429,
  "messages": ["Rate Limited: Please refer to the API docs https://developers.trychameleon.com/#/concepts/rate-limiting for more information"],
  "wait": 12
}
```

```text
X-Ratelimit-Limit: 4
```

```json
{
  "code": 429,
  "messages": ["Rate Limited: Please refer to the API docs https://developers.trychameleon.com/#/concepts/rate-limiting for more information"],
  "limit": 4
}
```
