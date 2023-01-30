# Alert Groups

**Alert Groups are used for Tours and Microsurveys to notify any relevant Team members when an Experience is in violation of the alert conditions.**

In the HTTP Response for [Listing](apis/alert-groups.md?id=alert-groups-index) and [Showing](apis/alert-groups.md?id=alert-groups-show) Alert Groups,
the full list of matching [Experiences](concepts/experiences.md) are returned as the `experiences` key.

-------


## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `name` | string | The name given by an administrator of Chameleon |
| `kind` | string | The kind of matched Experiences for this Alert Group. [More info ↓](apis/alert-groups.md?id=alert-group-kinds): One of `all`, `tour`, `survey`, `tags`, or `campaigns` |
| `interval` | number | # of days that the alerting condition should wait before triggering a violation |
| `published_at` | timestamp | The time this was most recently published |
| `style` | string | The style of alert condition to evaluate. [More info ↓](apis/alert-groups.md?id=alert-group-styles): One of `unseen` or `uncompleted` |
| `last_notified_at` | timestamp | Last time this alert was triggered for any Experience |
| `tag_ids` | array | When `kind=tags`, the IDs of the [Tags](apis/tags.md) that Experiences must be tagged with to be included in this Alert Group |
| `campaign_ids` | array | When `kind=campaigns`, the IDs of the [Experiences](concepts/experiences.md) to be included in this Alert Group |
| `slack_uid` | string | The Slack channel ID to notify on, only when `opt_in_slack_at` has a value |
| `opt_in_slack_at` | timestamp | Whether or not to send triggered alerts to Slack on the `slack_uid` channel |
| `emails` | array | The email address(es) to message, only when `opt_in_email_at` has a value |
| `opt_in_email_at` | timestamp | Whether or not to send triggered alerts to the given list of `emails` |


##### Kinds of Alert Groups (`kind` property) :id=alert-group-kinds

An Alert Group creates a **dynamic** or **static** group of Experiences. Each experience is checked for violation of the alert conditions.

| Kind | - | Description |
| --- | --- | --- |
| `all` | dynamic | All currently published [Tours](apis/tours.md) + [Microsurveys](apis/surveys.md) |
| `tour` | dynamic | All published [Tours](apis/tours.md) |
| `survey` | dynamic | All published [Microsurveys](apis/surveys.md) |
| `tags` | dynamic | All published [Tours](apis/tours.md) + [Microsurveys](apis/surveys.md) with **_any_** of the specified [Tags](apis/tags.md) in the `tag_ids` list |
| `campaigns` | static | All published [Tours](apis/tours.md) + [Microsurveys](apis/surveys.md) **_explicitly_** in the `campaign_ids` list |


##### Alerting conditions (`style` property) :id=alert-group-styles
| Kind | - | Description |
| --- | --- | --- |
| `unseen` | - | An Experience that is not Seen (i.e. displayed to any User) during the `interval` # of days will trigger an alert. |
| `uncompleted` | - | An Experience that is not Completed (i.e. no User finished) during the `interval` # of days will trigger an alert. |


## Listing Alert Groups :id=alert-groups-index

Retrieve a list of **all** Alert Groups and **all** currently matching [Experiences](concepts/experiences.md).
An account typically has 1-5 Alert Groups so this response should be relatively small.

#### HTTP Request

```
GET https://api.chameleon.io/v3/edit/alert_groups
```


#### HTTP Response

```json
{
  "alert_groups": [
    {
      "id": "5f3c4232c712de665632a6e2",
      "name": "Research opportunities flow (at least 1 per 2 weeks)",
      "interval": 14,
      "style": "uncompleted",
      "kind": "campaigns",
      "campaign_ids": [
        "5f3c4232c712de665632a6d5",
        "5f3c4232c712de665632a2a3"
      ],
      ...
      "experiences": [
        {
          "id": "5f3c4232c712de665632a6d5",
          "name": "Research: Planed New Feature X",
          ...
        },
        {
          "id": "5f3c4232c712de665632a2a3",
          "name": "Research: New Feature Z",
          ...
        }
      ],
    },
    {
      "id": "5f3c4232c712de665632a6e1",
      "name": "Any Tour/Microsurvey that goes 1 week without a completion",
      "interval": 7,
      "style": "uncompleted",
      "kind": "all",
      ...
      "experiences": [
        ...
      ]
    },
    {
      "id": "5f3c4232c712de665632a6d8",
      "name": "Broken Feature announcements (1 day not Seen)",
      "interval": 1,
      "style": "unseen",
      "kind": "tags",
      "tag_ids": [
        "5f3c4232c712de665632a5d7",
        "5f3c4232c712de665632aa3b"
      ],
      ...
      "experiences": [
        ...
      ]
    },
    ...
  ]
}
```

-----

## Showing a Alert Group :id=alert-groups-show

Retrieve a single Alert Group and **all** currently matching [Experiences](concepts/experiences.md).

#### HTTP Request

| param | -        | description |
|---|---|---|
| `id`  | required | An Alert Group ID to lookup |


```
GET https://api.chameleon.io/v3/edit/alert_groups/:id
```

#### HTTP Response

```json
{
  "alert_group": {
    "id": "5f3c4232c712de665632a6e2",
    "name": "Research opportunities flow (at least 1 per 2 weeks)",
    "interval": 14,
    "style": "uncompleted",
    "kind": "campaigns",
    "campaign_ids": [
      "5f3c4232c712de665632a6d5",
      "5f3c4232c712de665632a2a3"
    ],
    "experiences": [
      {
        "id": "5f3c4232c712de665632a6d5",
        "name": "Research: Planed New Feature X",
        ...
      },
      {
        "id": "5f3c4232c712de665632a2a3",
        "name": "Research: New Feature Z",
        ...
      }
    ],
    ...
  }
}
```


