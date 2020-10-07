# User Profiles (Incoming Webhook)

**Send User Profile data to Chameleon from services like Customer.io, Heap, Zapier or from you own backend.** Looking for the [JavaScript API](js/profiles.md)?

------

A User Profile that does not yet exist by `uid` will first be created and then updated with the other data included in this request.

> Profile data updates are processed synchronously on the application server.

## Create/Update a Profile :id=profiles-update

- When you are creating the User Profile, simply send the `uid` and any other properties pertinent to that profile.
- When you are updating the Profile, simply send the Chameleon `id` field or use the `uid` and any other properties pertinent to that profile.

#### HTTP Request

```
POST https://api.trychameleon.com/v3/observe/hooks/profiles
# OR
POST https://api.trychameleon.com/v3/observe/hooks/:account_secret/profiles
```

| param      | -        | description                                                  |
| ---------- | -------- | ------------------------------------------------------------ |
| `id`         | optional | The Chameleon ID of the User Profile                         |
| `uid`        | optional | The User Profile Identifier (typically the Database ID from your backend) |
| `company_id` | optional | The Chameleon Company ID that this user is a member of       |
| *others    | optional | All other properties will be stored on the Profile           |

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

#### HTTP Response

```json
{
  "profile": {
    "id": "5f3c4232c712de665632a2a3"
  }
}
```

## Disabling all Chameleon Experiences

To disable all Chameleon experiences you can add the `disabled: true` boolean value for the use via the [JavaScript API](js/profiles.md) or via [REST API](apis/profiles.md)


## Limits

- Up to a total of 768 bytes are stored for each scalar value where each Array item and each Hash value can reach this limit.
- See the full page on [Normalization](concepts/normalization.md?id=limits) for more information on these limits.

## Normalization

- Property names are normalized to lower case and underscored i.e. `userRole` => `user_role`.
- See the full page on [Normalization](concepts/normalization.md?id=properties) for more information on how properties are normalized.
