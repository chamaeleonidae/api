# Errors

The Chameleon APIs here are robust with 99.99% uptime and extensive monitoring. That being said, you can check our [Statuspage](https://status.trychameleon.com) or reference the errors found here for more information.

## HTTP Status 403 :id=status-403

Account token is not valid or has been revoked

```json
{
  "code": 403,
  "messages": []
}
```

## HTTP Status 404 :id=status-404

Endpoint or Resource not found

404's happen fo a couple of reasons:

 - The URL was not pasted correctly from these docs. URLs have an environment specifier directly after the version, make sure to include this
 - A resource/collection you tried to access is not found for this Secret token

```json
{
  "code": 404,
  "messages": []
}
```

## HTTP Status 429 :id=status-429

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
  "messages": ["Please wait for 114 more seconds before retrying your request"]
}
```

## HTTP Status 500 :id=status-500

Server error

An Error occurred that we had not otherwise planned on receiving. Typically these issues stem from downstream issues such as when a database is in the middle of failing over, an External dependency cannot be met temporarily or less often our code is not working

```json
{
  "code": 500,
  "messages": []
}
```

## HTTP Status 503 :id=status-503

Server not available or backend didn't respond in time

Unexpected maintenance or the inability to shed enough load with [Rate limiting](rate-limiting.md)

```json
{
  "code": 503,
  "messages": []
}
```