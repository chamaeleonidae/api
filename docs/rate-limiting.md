# Rate limiting

Rate limiting is crucial to the timely handling of all critical requests. Chameleon sets very high limits on the number of requests total and the amount of concurrency we support.
At this time we enforce rate limiting only in situations where the API is being abused in some way

When enforcing Rate limiting we give a `X-Ratelimit-Wait` header with the number of seconds until requests can proceed without further rate limiting
