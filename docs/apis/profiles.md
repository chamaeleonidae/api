# User Profiles

User Profiles are "your product's end-users", they represent a real person who was identified to Chameleon. They can store complex (semi-arbitrary) properties about who they are. 

The Chameleon User Profiles API allows you to
 - Search for a User by `id`, `uid` and `email`
 - Filter for Users or get the Count of Users by any of the properties you have sent to us

## Schema :id=schema

#### Fully-expanded profile when listed directly or embedded with `expand` param specified properly

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `uid` | string | The external ID that came from your backend system |
| `browser_x` | number | Browser width in pixels |
| `browser_tz` | number | Browser timezone in integer offset (+/-) from UTC |
| `browser_l` | string | Language code as reported by the Accept-Language header |
| `browser_n` | string | Browser name: One of `chrome`, `firefox`, `safari`, `opera`, `ie10`, `ie11`, or `edge` |
| `browser_k` | string | Browser kind: One of `desktop` or `mobile` |
| `percent` | number | Randomly assigned but stable, used for A/B testing |
| `last_seen_at` | timestamp | When the user was las active on a page where Chameleon is installed |
| `last_seen_session_count` | number | Number of sessions specified as a period of inactivity of `last_seen_at` of greater than 90 minutes |
| `*any options` | mixed | Any other options you have sent as Custom Properties will show up here too |

#### Non-expanded profile when embedded in another (i.e. Microsurvey response)

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `uid` | string | The external ID that came from your backend system |


## Finding a specific User :id=profiles-show

#### HTTP Request
`GET|POST` to `https://api.trychameleon.com/v3/analyze/profile` (singular)

| param | - | description |
|---|---|---|
| id | optional | The Chameleon ID of the User Profile |
| uid | optional | The User Profile identifier (typically the Database ID from your backend) |
| email | optional | If you have sent an email address this will be available for single-user lookup  |

Only one of these parameters is required. Users matched are unique identified based on these keys (no two users have the same `uid` or `email`)

When using a **GET** request

```
?id=5f3c4232c712de665632a6d5
?uid=18821
?email=leon@chmln.co
```

When using a **POST** request send one of these properties

```json
{
  "id": "5f3c4232c712de665632a6d5",
  "uid": 18821,
  "email": "leon@chmln.co"
}
```

#### HTTP Response

```json
{
  "profile": {
    "id": "5f3c4232c712de665632a6d5",
    "uid": 18821,
    "email": "leon@chmln.co",
    "first_name": "Leon",
    "role": "admin",
    "last_import_at": "2029-04-07T12:18:00Z",
    "invited_users_count": 4,
     ...
  }
}
```

------

## Searching Users :id=profiles-index

#### HTTP Request
`GET|POST` to `https://api.trychameleon.com/v3/analyze/profiles` (plural)

| param | - | description |
|---|---|---|
| segment_id | optional | The Chameleon Segment ID from the [List of Segments](apis/segments.md) |
| filters | optional | The array of [Segmentation filter expressions](concepts/filters.md) |


```json
{
  "segment_id": "5f3c4232c712de665632a6d7"
}
```

#### Example: Segmentation filter expressions

Admins who are responsible for 3 or more user invites on their account

```json
[
  {
    "prop": "role",
    "op": "eq",
    "value": "admin" 
  },
  {
    "prop": "invited_users_count",
    "op": "gte",
    "value": 3 
  }
]
```

#### HTTP Response

```json
{
  "profiles": [
    {
      "id": "5f3c4232c712de665632a6d5",
      "uid": 18821,
      "email": "leon@chmln.co",
      "role": "admin",
      "invited_users_count": 4,
       ...
    },
    {
      "id": "5f3c4232c712de665632a6d6",
      "uid": 18829,
      "email": "prehensile@chmln.co",
      "role": "admin",
      "invited_users_count": 6,
       ...
    }
  ]
}
```

------

## Counting Users :id=profiles-count

#### HTTP Request
`GET|POST` to `https://api.trychameleon.com/v3/analyze/profiles/count`

**Use the same params / request body as [Searching Users](apis/profiles.md?id=profiles-index)**

#### HTTP Response

```json
{
  "count": 65121
}
```
