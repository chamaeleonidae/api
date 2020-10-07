# Searching and Counting User Profiles

**User Profiles represent your *product's end-users*: real individuals who were identified to Chameleon.** 

*If you want to know more about User Profiles, visit the [User Profiles section](apis/profiles.md).*

------



Searching User Profiles through the Chameleon API allows you to:

 - Search for a user by `id`, `uid` and `email`.
 - Search for users or get the Count of Users by any of the properties you have sent to us.
 - Search for users by any of the interactions they had with Chameleon (answered a Microsurvey etc.).

   

> *Note: [Rate Limiting](concepts/rate-limiting.md) applies according to the table below.*

| endpoint          | Maximum concurrent requests |
| ----------------- | --------------------------- |
| `/profiles`       | 2                           |
| `/profiles/count` | 1                           |



## Schema :id=schema

See the full [User Profile schema](apis/profiles.md?id=schema).


## Examples :id=examples

All of these examples are based directly on the full schema of [Segmentation Filter Expressions](concepts/filters.md).

> *Note: A fully-fledged version of these examples is implemented in the Chameleon Builder section for Segments.*

Each example below is used as the value for the `filters` key in the JSON request body:

```json
{
  "filters": [
    ...
  ]
}
```

#### 1. User Profiles that Completed a Tour

```json
[
  {
    "kind": "tour",
    "value": Chameleon Tour ID,
    "range": "completed"
  }
]
```



#### 2. User Profiles that exited a Tour within last 3 days

`cond` - A secondary time-based filter operator.
`int` - A secondary time-based filter # of days.

```json
[
  {
    "kind": "tour",
    "value": Chameleon Tour ID,
    "range": "exited",
    "cond": "gt-d",
    "int": 3
  }
]
```



#### 3. User Profiles that are an NPS promoter

`mod` - A secondary matching condition for range.
`range` - A secondary matching range (in this case, button index).

> *Note: For a 11-button NPS, value `range` are 0,1,2,3,4,5,6,7,8,9,10.*

```json
[
  {
    "kind": "survey",
    "value": Chameleon Microsurvey ID,
    "mod": "gte",
    "range": 9
  }
]
```



#### 4. User Profiles that answered negatively to CES Microsurvey

`mod` - A secondary matching condition for range.
`range` - A secondary matching range (in this case, button index).

> *Note: For a 5-button CES, value `range` are 0,1,2,3,4.*

```json
[
  {
    "kind": "survey",
    "value": Chameleon Microsurvey ID,
    "mod": "lte",
    "range": 2
  }
]
```



#### 5. User Profiles that were most recently active more than 7 days ago

```json
[
  {
    "kind": "property",
    "prop": "last_seen_at",
    "op": "gt-d",
    "value": 7
  }
]
```



#### 6. Admins who are responsible for 3 or more user invites on their account

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



## Searching Users :id=profiles-index

#### HTTP Request

```
GET|POST https://api.trychameleon.com/v3/analyze/profiles (plural)
```

| param      | -        | description                                                  |
| ---------- | -------- | ------------------------------------------------------------ |
| `segment_id` | optional | The Chameleon Segment ID from the [List of Segments](apis/segments.md) |
| `filters`    | optional | The array of [Segmentation filter expressions](concepts/filters.md) |
| `expand`         | optional | Object that specifies relationships to include/exclude. Supported keys are `profile` and `company`      |
| `expand.profile` | optional | use values of `all`, `min` to control the properties present in the `profile`. Defaults to `all` |
| `expand.company` | optional | use values of `all`, `min` or `skip` to control the properties present in the `company`. Defaults to `min` |

#### Using the `expand` parameter

```
# As a URL parameter
expand[profile]=min&expand[company]=skip

# In the Reqeust body
{"expand":{"profile":"min","company":"skip"}}
```

Notes:
- A `profile` key will always be present with an object value. The `company` (embedded within `profile`) will be missing when the User Profile is not attached to a Company, otherwise it will be an object.

#### Example: Segment ID

```json
{
  "segment_id": "5f3c4232c712de665632a6d7"
}
```

#### Example: Segmentation filter expressions

[See examples above](api/profiles-search.md?id=examples)



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

```
GET|POST https://api.trychameleon.com/v3/analyze/profiles/count
```

**Use the same params / request body as [Searching Users](apis/profiles-search.md?id=profiles-index)**



#### HTTP Response

```json
{
  "count": 65121
}
```
