# Rate Limit Groups [BETA]

> **[Contact us](https://app.trychameleon.com/help) and reference this page to be added to the open BETA.**

**Rate Limit Groups are used for Microsurveys and Tours to make sure no more than X Experiences per Y time period are shown to a user.**

An example of this are your "How do you find this Feature?" Microsurveys. You may want only want to show one per week to limit fatigue.
Your Limit Group would have `rate_limit_size=1` and `rate_limit-kind=7d` then include all of the Microsurveys.

> Rate Limit Groups can purposefully overlap and work together to form a cohesive Rate Limiting strategy, to learn more or to run your strategy by the Team, feel free to [Contact us](https://app.trychameleon.com/help).

-------

Certain Experiences are exempt from a Rate Limit Group policy:

- Explicitly [toggling them off](https://app.trychameleon.com/rate-limiting)
- When [manually delivered](https://help.trychameleon.com/en/articles/3406346-choosing-a-delivery-method) via Short Link
- via [JavaScript API](js/show-tour.md)
- via [Deliveries API](apis/deliveries.md)
- When shown in a [Launcher](apis/launchers.md)


------

With the Chameleon API for Rate Limit Groups, you can:

- Retrieve a list of Rate Limit Groups.
- List all the related data that are connected to this Limit Group; Tours, Microsurveys and/or Tags



## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `name` | string | The name given by an administrator of Chameleon |
| `description` | string | The display description |
| `kind` | string | The type of Rate Limit Group this represents: One of `all`, `tour`, `survey`, `tags`, or `campaigns` |
| `rate_limit_size` | number | The total number of Experiences for the period of time specified by `rate_limit_kind` |
| `rate_limit_kind` | string | The period of time to apply to this Rate Limit Group: One of `1h`, `2h`, `4h`, `1d`, `7d`, `30d`, `91d`, `182d` or `365d` |
| `tag_ids` | array | The [Tags](apis/tags.md) associated with this Rate Limit Group (only present when `kind=tags`) |
| `campaign_ids` | array | The [Tours](apis/tours.md) + [Microsurveys](apis/surveys.md) associated with this Rate Limit Group (only present when `kind=campaigns`) |


##### Kinds of Rate Limit Groups (`kind` property)

A Rate Limit Group creates a **dynamic** or **static** group of Experiences over which to apply the `rate_limit_size` number of Experiences in `rate_limit_kind` interval of time.

| Kind | - | Description |
| --- | --- | --- |
| `all` | dynamic | All currently published [Tours](apis/tours.md) + [Microsurveys](apis/surveys.md) |
| `tour` | dynamic | All published [Tours](apis/tours.md) |
| `survey` | dynamic | All published [Microsurveys](apis/surveys.md) |
| `tags` | dynamic | All published [Tours](apis/tours.md) + [Microsurveys](apis/surveys.md) with **_any_** of the specified [Tags](apis/tags.md) in the `tag_ids` list |
| `campaigns` | static | All published [Tours](apis/tours.md) + [Microsurveys](apis/surveys.md) **_explicitly_** in the `campaign_ids` list |



## Listing Limit Groups :id=limit-groups-index

Retrieve a list of **all** Limit Groups. An account typically has 1-5 Limit Groups so this response should be relatively small.

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/limit_groups
```

#### HTTP Response

```json
{
  "limit_groups": [
    {
      "id": "5f3c4232c712de665632a6e2",
      "name": "1 Tour or Microsurvey every 2 hours (1 per session)",
      "kind": "all",
      "rate_limit_size": 1,
      "rate_limit_kind": "2h",
      ...
    },
    {
      "id": "5f3c4232c712de665632a6d9",
      "name": "How is X Feature? (1 per week)",
      "kind": "tags",
      "tag_ids": [
        "5f3c4232c712de665632a5d6",
        "5f3c4232c712de665632aa3a"
      ],
      "rate_limit_size": 1,
      "rate_limit_kind": "7d",
      ...
    },
    {
      "id": "5f3c4232c712de665632a6e2",
      "name": "Product upsell opportunities (2 per month)",
      "kind": "campaigns",
      "campaign_ids": [
        "5f3c4232c712de665632a6d5",
        "5f3c4232c712de665632a2a3"
      ],
      "rate_limit_size": 2,
      "rate_limit_kind": "30d",
      ...
    },
    ...
  ]
}
```

-----

## Showing a Limit Group :id=limit-groups-show

Retrieve a single Limit Group.

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/limit_groups/:id
```

| param | - | description |
|---|---|---|
| `id` | required | A Limit Group ID to lookup

#### HTTP Response

```json
{
  "limit_group": {
    "id": "5f3c4232c712de665632a6e2",
    "name": "1 Tour or Microsurvey every 2 hours (1 per session)",
    "kind": "all",
    "rate_limit_size": 1,
    "rate_limit_kind": "2h",
    ...
  }
}
```

------

## Listing Related Experiences :id=limit-group-experiences-index

A Limit Group is attached to many Chameleon Experiences (Tours/Microsurveys). This endpoint allows you to get a complete picture of all Experiences currently attached to the Limit Group. 

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/limit_groups/:id/experiences
```

| param | - | description |
|---|---|---|
| `id` | required | A Limit Group ID to lookup |
| `filter` | optional | Use `all` or `published_at` to include or exclude Experiences that are currently not published. Defaults to `published_at` |


#### HTTP Response (Example with `kind=campaigns`)

Note: this example Limit Group is based on `kind=campaigns` which means the Chameleon administrator **_explicitly picked these Experiences_** from a dropdown menu in the application.  

Keys returned: `limit_group`, `tours` and `surveys`

```json
{
  "limit_group": {
    "id": "5f3c4232c712de665632a6d9",
    "name": "How is X Feature? (1 per week)",
    "kind": "campaigns",
    "campaign_ids": [
      "5f3c4232c712de665632a6d5",
      "5f3c4232c712de665632a2a3",
      "5f3c4232c712de665632a2a9"
    ],
    ...
  },
  "tours": [
    {
      "id": "5f3c4232c712de665632a2a9",
      "name": "Data was just imported v2",
      "position": 2,
      "published_at": null,
      ...
    }
  ],
  "surveys": [
    {
      "id": "5f3c4232c712de665632a6d5",
      "name": "Task #2 completion CES",
      "position": 1,
      "published_at": "2029-04-07T12:18:00Z",
      ...
    },
    {
      "id": "5f3c4232c712de665632a2a3",
      "name": "Admin account setup #1 completion question",
      "position": 0,
      "published_at": "2029-04-07T12:38:00Z",
      ...
    }
  ]
}
```
#### HTTP Response (Example kind=tags)

Note: this example Limit Group is based on `kind=tags` which means the Chameleon administrator **_explicitly picked a [set of Tags](apis/tags.md)_** from a dropdown menu in the application.

Keys returned: `limit_group`, `tags`, `tours` and `surveys`

```json
{
  "limit_group": {
    "id": "5f3c4232c712de665632a6d9",
    "name": "How is X Feature? (1 per week)",
    "kind": "tags",
    "tag_ids": [
      "5f3c4232c712de665632a5f1",
      "5f3c4232c712de665632a5f2"
    ],
    ...
  },
  "tags": [
    {
      "id": "5f3c4232c712de665632a5f1",
      "uid": "new_feature",
      "name": "New Feature",
      "description": "Any feature announcement",
      "models_count": 9,
      "last_seen_at": "2029-04-07T12:18:00Z"
    },
    {
      "id": "5f3c4232c712de665632a5f2",
      "uid": "ui_change",
      "name": "Interface Change",
      "description": "Any significant interface change to highlight",
      "models_count": 5,
      "last_seen_at": "2029-04-07T12:19:00Z"
    }
  ],
  "tours": [
    {
      "id": "5f3c4232c712de665632a6d5",
      "name": "How hard was it to complete this task?",
      "position": 19,
      "published_at": "2029-04-07T12:18:00Z",
      "tag_ids": [
        "5f3c4232c712de665632a5f2"
      ],
      ...
    },
   ...
  ],
  "surveys": [
    {
      "id": "5f3c4232c712de665632a2a3",
      "name": "Admin account setup #1 completion question",
      "position": 12,
      "published_at": "2029-04-07T12:38:00Z",
      "tag_ids": [
        "5f3c4232c712de665632a190",
        "5f3c4232c712de665632a5f1"
      ]
      ...
    }
  ]
}
```


