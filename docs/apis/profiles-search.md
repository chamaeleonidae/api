# User Profile Searching + Counting

User Profiles are "your product's end-users", they represent a real person who was identified to Chameleon. They can store complex (semi-arbitrary) properties about who they are. 

The Chameleon User Profiles API allows you to
 - Search for a User by `id`, `uid` and `email`
 - Search for Users or get the Count of Users by any of the properties you have sent to us
 - Search for Users by any of the interactions they had with Chameleon (answered a Microsurvey etc.)

## Schema :id=schema

See the full [User Profile schema](api/profiles.md?id=schema)

## Examples :id=examples

All of these examples are based directly on the full schema of [Segmentation filter expressions](concepts/filters.md)

A fully-fledged version of this is implemented in the Chameleon Builder section for Segments

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

`cond` - A secondary time-based filter operator
`int` - A secondary time-based filter # of days

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

For a 11-button NPS, value `range` are 0,1,2,3,4,5,6,7,8,9,10

`mod` - A secondary matching condition for range
`range` - A secondary matching range (in this case, button index)

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

For a 5-button CES, value `range` are 0,1,2,3,4

`mod` - A secondary matching condition for range
`range` - A secondary matching range (in this case, button index)

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

## Listing / Searching Users :id=profiles-index

#### HTTP Request
`GET|POST` to `https://api.trychameleon.com/v3/analyze/profiles` (plural)

| param | - | description |
|---|---|---|
| segment_id | optional | The Chameleon Segment ID from the [List of Segments](apis/segments.md) |
| filters | optional | The array of [Segmentation filter expressions](concepts/filters.md) |


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
`GET|POST` to `https://api.trychameleon.com/v3/analyze/profiles/count`

**Use the same params / request body as [Searching Users](apis/profiles-search.md?id=profiles-index)**

#### HTTP Response

```json
{
  "count": 65121
}
```
