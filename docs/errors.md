# Errors

The Chameleon APIs here are robust with 99.99% uptime and extensive monitoring. That being said, you can check our [Statuspage](https://status.trychameleon.com) or reference the errors found here for more information.

#### HTTP Status 403: Account token is not valid or has been revoked

```json
{
  "status": 403,
  "messages": []
}
```

#### HTTP Status 404: Endpoint not found

404's happen fo a couple of reasons:

 - The URL was not pasted correctly from these docs. URLs have an environment specifier directly after the version, make sure to include this
 - A resource/collection you tried to access is not found for this Secret token

```json
{
  "status": 404,
  "messages": []
}
```

#### HTTP Status 429: Too many requests

Rate limiting has been exceeded.

See also [Rate limiting](rate-limiting.md)

- Headers

```
X-Ratelimit-Wait: 120
```

- Body

```json
{
  "status": 429,
  "messages": ["Please wait for 120 more seconds before retrying your request"]
}
```

#### HTTP Status 500: Server error

An Error occurred that we had not otherwise planned on receiving. Typically these issues stem from downstream issues such as when a databse is in the middle of failing over, an External dependency cannot be met temporarily or less often our code is not working

```json
{
  "status": 500,
  "messages": []
}
```

#### HTTP Status 503: Server not available

Unexpected maintenence or the inability to shen enough load with rate-limiting

```json
{
  "status": 503,
  "messages": []
}
```