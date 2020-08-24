# Segments

Segments are fundamental to targeting users withing Chameleon. They are used for Microsyrveys, Tours and Launchers to make sure the right users see the right content at the right moment.

A Segment is a collection of [Segmentation filter expressions](concepts/filters.md) in the `items` key

## Schema :id=schema


## Listing Segments :id=segments-index

#### HTTP Request

`GET` to `https://api.trychameleon.com/v3/edit/segments`

| param | - | description |
|---|---|---|
| limit | optional | Defaults to `50` with a maximum of `500` |
| before | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| before | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |


With a timestamp

```json
{
  "limit": 100,
  "before": "2029-04-07T12:18:00Z"
}
```

From the previous response `cursor.before`

```json
{
  "limit": 500,
  "before": "5f3c4232c712de665632a6d7"
}
```

#### HTTP Response

```json
{
  "segments": [
    {
      "id": "5f3c4232c712de665632a6d9",
      "name": "Admins who invited > 3",
      "items": [
        {
          "id": "5f3c4232c712de665632a6d8",
          "kind": "property",
          "prop": "role",
          "op": "eq",
          "value": "admin"
        },
        {
          "id": "5f3c4232c712de665632a6d7",
          "kind": "property",
          "prop": "invited_users_count",
          "op": "gte",
          "value": 3
        }
      ]
    },
    {
      "id": "5f3c4232c712de665632a6e2",
      "name": "Grown Plan Upsell",
       ...
    },
    ...
  ],
  "cursor": {
    "limit": 50,
    "before": "5f3c4232c712de665632a6d7"
  }
}
```

-----

## Showing a Segment :id=segments-show

Show a single Segment

#### HTTP Request

`GET` to `https://api.trychameleon.com/v3/edit/segments/:id`

| param | - | description |
|---|---|---|
| id | required | A Segment ID to lookup

#### HTTP Response

```json
{
  "segment": {
    "id": "5f3c4232c712de665632a6d7",
    "name": "Admins who invited > 3",
    "items": [
      {
        "id": "5f3c4232c712de665632a6d8",
        "kind": "property",
        "prop": "role",
        "op": "eq",
        "value": "admin"
      },
      {
        "id": "5f3c4232c712de665632a6d9",
        "kind": "property",
        "prop": "invited_users_count",
        "op": "gte",
        "value": 3
      }
    ]
  }
}
```

------

## Listing Related Experiences :id=segment-experiences-index

A segment can be configured to be attached to **many Chameleon Experiences** including Microsurveys, Tours and Launchers. This endpoint allows you to list any of these items that are currently attached to the Segment given with the ID

#### HTTP Request
`GET` to `https://api.trychameleon.com/v3/edit/segments/:id/:kind`

| param | - | description |
|---|---|---|
| id | required | A Segment ID to lookup
| kind | required | One of `tour` `survey` `launcher`

#### HTTP Response

```json
{
  "segment": {
    "id": "5f3c4232c712de665632a6d7",
    "name": "Admins",
    ...
  },
  "tours": [
    {
      "id": "5f3c4232c712de665632a6d5",
      "name": "Revamped Dashboard Launch",
      "style": "auto",
      "position": 4,
      "published_at": "2029-04-07T12:18:00Z",
       ...
    },
  ],
  "cursor": {
    "limit": 50,
    "before": "5f3c4232c712de665632a2a1"
  }
}
```
