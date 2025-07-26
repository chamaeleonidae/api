# User Profiles

**User Profiles represent your *product's end-users*: real individuals who were identified to Chameleon. They can store complex (semi-arbitrary) properties about who they are.**

> For a full list of your User / Company Properties see the [Properties API](apis/properties.md)

---

The Chameleon User Profiles API allows you to:

- Create / Update custom User properties
- Retrieve a user by `id`, `uid` and `email`.
- Search for users or get the count of users using any of the properties you have sent to us.
- Clear or reset a specific user's data.
- Delete a user permanently


## Schema :id=schema

#### Fully-expanded profile when listed directly or embedded with `expand` param specified properly

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `uid` | string | The external ID that came from your backend system |
| `company_id` | ID | The Chameleon ID of the [Company](apis/companies.md?id=schema) (only if associated) |
| `browser_x` | number | Browser width in pixels |
| `browser_tz` | number | Browser timezone in integer offset (+/-) from UTC |
| `browser_l` | string | Language code as reported by the Accept-Language header |
| `browser_n` | string | Browser name: One of `chrome`, `firefox`, `safari`, `opera`, `ie10`, `ie11`, `edge`, or `unknown` |
| `browser_k` | string | Browser kind: One of `desktop`, `mobile`, or `tablet` |
| `percent` | number | Randomly assigned but stable, used for A/B testing |
| `last_seen_at` | timestamp | When the user was las active on a page where Chameleon is installed |
| `last_seen_session_count` | number | Number of sessions specified as a period of inactivity of `last_seen_at` of greater than 90 minutes |
| `delivery_ids` | array&lt;ID&gt; | Ordered list of [Delivery](apis/deliveries.md?id=schema) model IDs |
| `company` | object | The expandable [Company](apis/companies.md?id=schema) (only if associated)  |
| `*any options` | mixed | Any other options you have sent as Custom Properties will show up here too |


#### Non-expanded profile when embedded in another (i.e. Microsurvey response)

| Property     | Type      | Description                                               |
| ------------ | --------- | --------------------------------------------------------- |
| `id`         | ID        | The Chameleon ID                                          |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated                    |
| `uid`        | string    | The external ID that came from your backend system        |


## Create / Update a User :id=profiles-create

See the [User Profiles Webhook](webhooks/profiles.md) for sending User data to Chameleon


## Retrieve a specific User :id=profiles-show

#### HTTP Request

```
GET|POST https://api.chameleon.io/v3/analyze/profiles/:id
GET|POST https://api.chameleon.io/v3/analyze/profile # singular with parameters
```

| param | -        | description                                                  |
| ----- | -------- | ------------------------------------------------------------ |
| `id`    | optional | The Chameleon ID of the User Profile                         |
| `uid`   | optional | The User Profile identifier (typically the Database ID from your backend) |
| `email` | optional | If you have sent an email address, this will be available for single-user lookup |

Only one of these parameters is required. Users matched are uniquely identified based on these keys (no two users have the same `uid` or `email`)

When using a **GET** request with parameters:

```
?id=5f3c4232c712de665632a6d5
?uid=18821
?email=leon@chmln.co
```

When using a **POST** request send one of these properties:

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
    "created_at": "2024-03-15T10:30:00.000Z",
    "updated_at": "2024-04-07T12:18:00.000Z",
    "uid": "user_18821",
    "company_id": "5f3c4232c712de665632a6e8",
    "browser_x": 1920,
    "browser_tz": -8,
    "browser_l": "en-US",
    "browser_n": "chrome",
    "browser_k": "desktop",
    "percent": 42.87,
    "last_seen_at": "2024-04-07T11:45:00.000Z",
    "last_seen_session_count": 23,
    "delivery_ids": [
      "5f3c4232c712de665632a6f1",
      "5f3c4232c712de665632a6f2"
    ],
    "email": "john.doe@acmecorp.com",
    "first_name": "John",
    "last_name": "Doe",
    "role": "admin",
    "plan": "enterprise",
    "onboarding_completed": true,
    "subscription_status": "active",
    "team_size": 25,
    "last_login_at": "2024-04-07T11:30:00.000Z",
    "feature_flags": ["beta_ui", "advanced_analytics"],
    "custom_properties": {
      "department": "Engineering",
      "seniority": "Senior",
      "signup_source": "organic"
    },
    "company": {
      "id": "5f3c4232c712de665632a6e8",
      "created_at": "2024-01-10T08:00:00.000Z",
      "uid": "company_abc123",
      "name": "Acme Corporation"
    }
  }
}
```



## Clear or Reset a User Profile :id=profiles-destroy

Clearing a profile consists of:

- Resetting the properties such as browser width, last seen time, sessions count, etc..
- Removing Microsurvey responses.
- Reverts summary data from any actions this user took (i.e. Tour Started counts decremented appropriately).
- Removes and resets any Events that were tracked for this user.
- A new `percent` is assigned and `last_cleared_at` is updated to `"$now"`.
- A few other internal cleanup items.

It is also possible to clear a user profile through the [Chameleon Dashboard](https://app.chameleon.io/testing) but is limited to profiles associated with the currently logged-in Chameleon Admin. To clear any profile on your account use this API.



#### HTTP Request

```
DELETE https://api.chameleon.io/v3/edit/profiles/:id
# OR
DELETE https://api.chameleon.io/v3/edit/profiles?uid=:uid
```

| param | -        | description                                                  |
| ----- | -------- | ------------------------------------------------------------ |
| `id`    | optional | A Chameleon User Profile ID to lookup                        |
| `uid`   | optional | The User Profile Identifier (typically the Database ID from your backend) |

#### HTTP Response

```json
{
  "profile": {
    "id": "5f3c4232c712de665632a6d5",
    "uid": 18821,
    "last_cleared_at": "2029-04-07T12:18:00Z",
    "browser_x": null,
    "last_seen_at": null,
    "percent": 12.231,
     ...
  }
}
```



## Delete a User Profile permanently :id=delete-a-user-profile-permanently

The ability to delete a User Permanently is part of our effort to allow your users to opt-out of continued data storage by Chameleon and its partners.
The key actions taken directly after deleting a User, is to remove Associated data before then removing the User profile data.
Associated data includes records of Chameleon Experiences, Events logged and any other internal metrics associated with actions the user has taken.
At the end of the process no record of this user exists in our database. Additionally, any data stored in backups relating to user profile data in our database has a retention of 3 months.

#### HTTP Request

```
DELETE https://api.chameleon.io/v3/edit/profiles/:id/forget
# OR
DELETE https://api.chameleon.io/v3/edit/profiles/forget?uid=:uid
```

| param | -        | description                                                  |
| ----- | -------- | ------------------------------------------------------------ |
| id    | optional | A Chameleon User Profile ID to remove                                  |
| uid   | optional | The User Profile Identifier (typically the Database ID from your backend) |
| `email` | optional | If you have sent an email address, this will be available for single-user lookup |


#### HTTP Response

The Deletion is an internal Chameleon record that can be referenced as proof of initiating this request.

```json
{
  "profile": {
    "id": "5f3c4232c712de665632a6d5",
  },
  "deletion": {
    "id": "5f3c4232c712de665632a6d6",
  }
}
```


## Delete many User Profiles :id=delete-many

Please use [this gist](https://gist.github.com/bnorton/f8f3cf5ecf7fc72d0586ad1774ca7802) to delete users via a CSV!
