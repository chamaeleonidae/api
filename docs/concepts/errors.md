# Errors

**The Chameleon API is robust with 99.99% uptime and extensive monitoring. In case you are facing any error, you can check our [Status Page](https://status.chameleon.io) or make use of the following error reference to have more information.**

---

## HTTP 403 Forbidden :id=code-403

**Account token is not valid or has been revoked**

```json
{
  "code": 403,
  "messages": ["Unauthorized: Please check your Chameleon Account Secret"]
}
```

## HTTP 404 Not Found :id=code-404

**Endpoint or Resource not found**

404 errors happen for a couple of reasons:

 - The URL was not pasted correctly from these docs. URLs have an environment specifier directly after the version, make sure to include this
 - A resource/collection you tried to access is not found for this Secret token

```json
{
  "code": 404,
  "messages": ["Endpoint not found: Please recheck with the API docs https://developers.chameleon.io"]
}
```

## HTTP 409 Conflict :id=code-409

**Conflicting state of the Resource**

 - The Tour is not live when trying to create a Delivery
 - The specified update is not compatible with the current state of the Model
 - The Delivery has already been triggered when the `until` time is updated

```json
{
  "code": 409,
  "messages": ["Conflict: Please check the preconditions in the API docs https://developers.chameleon.io"]
}
```

## HTTP 422 Unprocessable Entity :id=code-422

**The request parameters cannot be processed as-is**

 - The parameter that is specifies a timestamp cannot be parsed/interpreted as a timestamp
 - The identifier is missing when looking up a User Profile

```json
{
  "code": 422,
  "messages": ["Unprocessable: Please check the request parameters with the API docs https://developers.chameleon.io"]
}
```

## HTTP 429 Too Many Requests :id=code-429

**You have made too many concurrent or bucketed requests and exceeded your rate limit.**

See also [Rate limiting](concepts/rate-limiting.md)

- Headers

```
X-Ratelimit-Wait: 114
X-Ratelimit-Limit: 2
```

- Body

```json
{
  "code": 429,
  "messages": ["Rate Limited: Please refer to the API docs https://developers.chameleon.io/#/concepts/rate-limiting for more information"],
  "wait": 14
}
```

## HTTP 500 Internal Server Error :id=code-500

**Server error**

An internal server error occurred (one that we otherwise had not planned on receiving). Typically these issues stem from downstream issues such as when a database is in the middle of failing over, an External dependency cannot be met temporarily or less often our code is not working

```json
{
  "code": 500,
  "messages": ["Internal server error: Please retry later"]
}
```

## HTTP 503 Service Unavailable :id=code-503

**Server not available or backend didn't respond in time**

Possibly not a JSON response depending on the origin of the 503.

Unexpected maintenance, API downtime or the inability to shed enough load with [Rate limiting](rate-limiting.md)

```json
{
  "code": 503,
  "messages": []
}
```

## HTTP 504 Gateway Timeout :id=code-504

**The server contacted or proxied your request to a different service which took too long to respond**

This can happen when a request is too complex or the system load is too high. You may retry your request again after a suitable delay.

```json
{
  "code": 504,
  "messages": ["Internal timeout: An internal operation took too long."]
}
```
