# User Profiles (Incoming Webhook)

**Send User Profile data to Chameleon from services like Customer.io, Heap, Zapier, Hightouch, Census or from you own backend.** Looking for the [JavaScript API](js/profiles.md)?

------

A User Profile that does not yet exist by `uid` will first be created and then updated with the other data included in this request.

> Profile data updates are processed synchronously on the application server.

## Create/Update a Profile :id=profiles-update

- When you are **creating** the User Profile, send the User ID as `uid` and any other properties pertinent to that Profile.
- When you are **updating** the User Profile, send the User ID as `uid`, the Email address as `email` or the Chameleon ID as `id` and any other properties pertinent to that Profile.

#### HTTP Request

```
POST https://api.chameleon.io/v3/observe/hooks/profiles
# OR
POST https://api.chameleon.io/v3/observe/hooks/:account_secret/profiles
```

| param         | -        | description                                                                                                       |
|---------------|----------|-------------------------------------------------------------------------------------------------------------------|
| `id`          | optional | The Chameleon ID of the User Profile                                                                              |
| `uid`         | optional | The User Profile Identifier (typically the Database ID from your backend)                                         |
| `email`       | optional | The User Profile Email address (only use this if you send the `email` property from your JavaScript installation) |
| `company_id`  | optional | The Chameleon Company ID that this user is a member of                                                            |
| `company_uid` | optional | The external ID of the Company from your backend system                                                           |
| *others       | optional | All other properties will be stored on the Profile                                                                |

```json
{
  "uid": 18821,
  "email": "leon@chmln.co",
  "first_name": "Leon",
  "role": "admin",
  "last_import_at": "2029-04-07T12:18:00Z",
  "invited_users_count": 4,
   ...
}
```

The user with `uid=18821` is a member of the `uid=931` Company 

```json
{
  "uid": 18821,
  "role": "admin",
  "company_uid": 931
}
```


#### HTTP Response

```json
{
  "profile": {
    "id": "5f3c4232c712de665632a2a3"
  }
}
```

### Disabling all Chameleon Experiences

To disable all Chameleon Experiences you can add the `disabled: true` boolean value for the use via the [JavaScript API](js/profiles.md) or via [REST API](apis/profiles.md)


### Limits

- Up to a total of 768 bytes are stored for each scalar value where each Array item and each Hash value can reach this limit.
- See the full page on [Normalization](concepts/normalization.md?id=limits) for more information on these limits.

### Normalization

- Property names are normalized to lower case and underscored i.e. `userRole` => `user_role`.
- See the full page on [Normalization](concepts/normalization.md?id=properties) for more information on how properties are normalized.


## Bulk Create/Update Profiles :id=profiles-bulk

- When sending a bulk create/update send an array of User Profile objects as the `profiles` parameter
- For each User Profile, send the User ID as `uid` and any other properties pertinent to that Profile.
- Instead of the `uid` you may use the Email address as `email`.

#### HTTP Request

```
POST https://api.chameleon.io/v3/observe/hooks/profiles/batch
# OR
POST https://api.chameleon.io/v3/observe/hooks/:account_secret/profiles/batch
```

| param              | -                         | description                                                                                                                                |
|--------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `profiles`         | array&lt;User Profile&gt; | The list of User Profiles to update; each item has the same schema as the [Single Profile update](webhooks/profiles.md?id=profiles-update) |
| `on_model_missing` | optional                  | The treatment of User Profiles not previously sent to Chameleon. Defaults to `create`. One of `create`, `ignore`                           |

```json
{
  "profiles": [
    {
      "uid": 18821,
      "first_name": "Leon",
      "role": "admin",
      "last_import_at": "2029-04-07T12:18:00Z",
      "invited_users_count": 7,
      ...
    },
    {
      "uid": 28421,
      "first_name": "Kim",
      "role": "engineer",
      "last_import_at": "2029-04-02T16:11:06Z",
      "invited_users_count": 4,
      ...
    },
    ...
  ]
}
```

The user with `uid=18821` is a member of the `uid=931` Company and The user with `uid=28421` is a member of the `uid=632` Company 

```json
{
  "profiles": [
    {
      "uid": 18821,
      "company_uid": 931
    },
    {
      "uid": 28421,
      "company_uid": 632
    },
    ...
  ]
}
```


#### HTTP Response

```json
{
  "batch": {
    "id": "7f332c712de6c4265632a32a"
  }
}
```

#### HTTP Response error

When the 4430th item had no value for `uid` or `email` keys

Note: The status code will be the normal 202 for (Accepted for processing)

```json
{
  "batch": {
    "id": "7f332c712de6c4265632a32a"
  },
  "errors": [
    {
      "code": 422,
      "index": 4429,
      "message": "No identifier found for the 4430th item. Pass your User ID as the `uid` parameter or the Email address as the `email` parameter"
    }
  ]
}
```

## Limits

- The size of each batch request is limited to 16mb
- As with the [Single Profile update](webhooks/profiles.md?id=profiles-update), up to a total of 768 bytes are stored for each scalar value where each Array item and each Hash value can reach this limit.
- See the full page on [Normalization](concepts/normalization.md?id=limits) for more information on these limits.

#### Examples

> Either set the number of items per batch to _10,000_ OR to approximate the number of
> items per batch (based on the average payload size), divide (16777216 / "Average characters in JSON payload per item") * 0.95

With the following update, you can send approximately _265,000 User Profiles_ per batch request

```json
{
  "uid": "49573fa9-f111-4644-8c24-e41520ee87e2",
  "plan": "gold"
}
```

With the following update, you can send approximately _62,000 User Profiles_ per batch request

```json
{
  "uid": "49573fa9-f111-4644-8c24-e41520ee87e2",
  "email": "jane@acme.software",
  "first_name": "Jane",
  "last_name": "Chameleon",
  "last_login": "2029-04-29T09:00:00.000Z",
  "subscription_type": "platinum",
  "role": "revops",
  "company_id": "72d8ce91-fa3c-40f4-954d-4a8e8319a61e"
}
```

#### HTTP Response error

When the request was larger than 16mb. The status code will be 413 (Request too large)

```json
{
  "code": 413,
  "messages": ["Each batch must be less than 16mb, try splitting the batch in half"]
}
```
