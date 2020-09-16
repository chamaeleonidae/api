# Errors

**The Chameleon API is robust with 99.99% uptime and extensive monitoring. In case you are facing any error, you can check our [Status Page](https://status.trychameleon.com) or make use of the following error reference to have more information.**

---

## HTTP Status 403
Account token is not valid or has been revoked

```json
{
  "code": 403,
  "messages": ["Unauthorized: Please check your Chameleon Account Secret"]
}
```

## HTTP Status 404

Endpoint or Resource not found

404's happen fo a couple of reasons:

 - The URL was not pasted correctly from these docs. URLs have an environment specifier directly after the version, make sure to include this
 - A resource/collection you tried to access is not found for this Secret token

```json
{
  "code": 404,
  "messages": ["Endpoint not found: Please recheck with the API docs https://developers.trychameleon.com"]
}
```

## HTTP Status 429

You have made too many requests and exceeded your Rate limit.

See also [Rate limiting](rate-limiting.md)

- Headers

```
X-Ratelimit-Wait: 114
```

- Body

```json
{
  "code": 429,
  "messages": ["Rate Limited: Please refer to the API docs https://developers.trychameleon.com/#/concepts/rate-limiting for more information"],
  "wait": 14
}
```

## HTTP Status 500

Server error

An Internal server error occurred (one that we otherwise had no planned on receiving). Typically these issues stem from downstream issues such as when a database is in the middle of failing over, an External dependency cannot be met temporarily or less often our code is not working

```json
{
  "code": 500,
  "messages": []
}
```

## HTTP Status 503

Server not available or backend didn't respond in time -- possibly not a JSON response depending on the origin of the 503

Unexpected maintenance, API downtime or the inability to shed enough load with [Rate limiting](rate-limiting.md)

```json
{
  "code": 503,
  "messages": []
}
```

## HTTP Status 504

The Server contacted or proxied your request to a different Service which took too long to respond

This can happen when a request is too complex or the system load is too high. You may retry your request again after a suitable delay.

```json
{
  "code": 504,
  "messages": ["Internal timeout: An internal operation took too long."]
}
```
