# Deliveries (Coming soon)

> **Interested in the Deliveries BETA program?? [Ping us here](mailto:hello@trychameleon.com?subject=API+Deliveries+beta)**

Deliveries are used to directly trigger an Experience to one or to many users. On the next page-load, the linked Experience will be triggered with the given options. While this is generally true there are a few different conditions that must be met for the trigger to occur:

Reason the trigger may not occur
 - The user never loads any page
 - The `from` time has not be reached
 - The `until` time has passed
 - The Experience is not live
 - `use_segmentation=true` and the Audience does not currently match
 - `once=false` and the user has seen the Experience before
 - `redirect=false` and the user never loads the matching URL
 - `skip_triggers=false` and the user never clicks/hovers on the configured Step triggers
 - `skip_url_match=false` and the user never loads the matching URL


## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `model_id` | ID | The Chameleon ID of Experience this Delivery will trigger. |
| `model_kind` | string | The kind of Experience: One of `tour` or `survey` |
| `profile_id` | ID | The Chameleon ID of the [User Profile](apis/profiles.md?id=schema) |
| `from` | timestamp | The timestamp before which this Delivery will not run. |
| `until` | timestamp | The timestamp after which this Delivery is no longer valid. |
| `use_segmentation` | boolean | Whether or not to first apply the Audience (Segmentation) to determine if the Experience show display to the user. |
| `once` | boolean | Whether or not to check if the user has seen this Experience before |
| `redirect` | boolean | Whether or not to redirect to the "page the Experience starts on". |
| `skip_triggers` | boolean | Whether or not to bypass the triggers, elements and delays on the first step to "force" it to show right away. |
| `skip_url_match` | boolean | Whether or not to bypass the first step URL match to "force" it to show right away. |
| `at` | timestamp | The timestamp of when this Delivery was triggered for the User. |
| `at_href` | string | The page URL of where this Delivery was triggered for the User. |
| `interaction_id` | ID | The Chameleon ID of [Interaction](apis/tour-interactions.md) this Delivery triggered. |
| `group_kind` | string | The triggering system/api: One of `link`, `api_js`, `launcher`, `experiment`, `campaign`, or `api_edit` |


### Errors

 - When the Experience is not live (not currently published) (`409`)
 - When the user has not been seen by Chameleon (`422`)
 - When the supplied dates (`from` and `until`) are out of order (`422`)
 - When the supplied dates (`from` and `until`) are not in compatible formats (`422`)


| Code  | description                                                  |
| ----- | ------------------------------------------------------------ |
| `404` | A related model cannot be found (Tour, Survey or Profile) |
| `409` | The experience is not live, please publish and retry |
| `409` | The Experience has already been triggered (it can no longer be subsequently changed) |
| `422` | The dates cannot be honored in their given values |
| `429` | Only one Delivery at a time can be created per User Profile |


### Limitations :id=limits

> **Once a delivery is marked as triggered (when `at` has a timestamp value) the delivery can no-longer be updated.**

Pending Deliveries (yet untriggered) are limited to 3 per User Profile. This limit can be changed in certain circumstances by [contacting us](mailto:hello@trychameleon.com?subject=API+Delivery+limits).
If a User Profile already has 3 pending Deliveries when a new Delivery is created, the request will fail with a HTTP 409 error code.
The good news is that you can instruct the API prioritize this one as the `first` or the `last` position in the queue: Use `delivery_ids_position=first`.


------

## List all Deliveries :id=deliveries-index

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/deliveries
```

| param              | -        | description    |
| ------------------ | -------- | -------------- |
| `model_id`         | optional | The Chameleon ID of Experience to filter to |
| `profile_id`       | optional | The Chameleon ID of User Profile to filter to |
| `limit`  | optional | Defaults to `50` with a maximum of `500`                     |
| `before` | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| `before` | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |
| `after`  | optional | Read as "created `after`" and can be given as a timestamp or ID to get only `limit` items that were created after this time |


```json
{
  "deliveries": [
    {
      "model_kind": "survey",
      "model_id": "5f3c4232c712de665632a6d4",
      "uid": 34283,
      "until": "2029-04-07T12:18:00Z",
      ...
    },
    {
      "model_kind": "tour",
      "model_id": "5f3c4232c712de665632a6d5",
      "uid": 542213,
      "from": "2029-02-03T12:18:00Z",
      "until": "2029-04-07T12:18:00Z",
      ...
    },
    ...
  ]
}
```


## Create a Delivery :id=deliveries-create

#### HTTP Request

```
POST https://api.trychameleon.com/v3/edit/deliveries
```

Mirrors to the options for [Showing an Experience via JavaScript](js/show-tour.md?id=options)

| param              | -        | description    |
| ------------------ | -------- | -------------- |
| `model_kind`       | required | The kind of Experience this Delivery will trigger either `tour` or `survey` |
| `model_id`         | required | The Chameleon ID of Experience this Delivery will trigger |
| `profile_id`       | optional | The Chameleon ID of User Profile to target |
| `uid`              | optional | The User Profile Identifier (typically the Database ID from your backend) |
| `email`            | optional | The email address of User Profile to target |
| `from`             | optional | The timestamp before which this Delivery will not run - don't trigger this Experience before this time. |
| `until`            | optional | The timestamp after which this Delivery is no longer valid - don't trigger this Experience after this time. Default +infinity |
| `until`            | optional | The [time interval](concepts/normalization.md?id=timestamps) after which this Delivery is no longer valid (i.e. `"+30d"` => 30 days from now, `"+62d"` => 62 days from now) |
| `use_segmentation` | optional | Default `false`. Boolean value whether or not to first apply the Audience (Segmentation) to determine if the Experience show display to the user. |
| `once`             | optional | Default `false`. Boolean value whether or not to check if the user has seen this Experience before, `false` means for the Tour to display. |
| `redirect`         | optional | Default `false`. Boolean value whether or not to redirect to the "page the Experience starts on". This redirect loads the "Tour link" that can be copied from "Additional sharing options". |
| `skip_triggers`    | optional | Default `false`. Boolean value whether or not to bypass the triggers, elements and delays on the first step to "force" it to show right away. |
| `skip_url_match`   | optional | Default `false`. Boolean value whether or not to bypass the first step URL match to "force" it to show right away. |
| `delivery_ids_position` | optional | Defaults to `first`. The value of `last` or a specific integer index to insert at are accepted. |

> Required: One of `profile_id`, `uid` or `email`

```json
{
  "model_kind": "tour",
  "model_id": "5f3c4232c712de665632a6d5",
  "uid": 542213,
  "from": "2029-02-03",
  "until": "+45d",
  ...
}
```


## Update a Delivery :id=deliveries-update

> **Once a delivery is marked as triggered (when `at` has a timestamp value) the delivery can no-longer be updated.**

#### HTTP Request

```
PATCH https://api.trychameleon.com/v3/edit/deliveries/:id
```

| param | -        | description                                                  |
| ----- | -------- | ------------------------------------------------------------ |
| `id`    | optional | The Chameleon ID of the Delivery                         |
| *others | optional | Any other params from [Create a Delivery](apis/deliveries.md?id=deliveries-create)                         |


## Remove a Delivery :id=deliveries-destroy

Cancel a delivery that has yet to happen

> **Once a delivery is marked as triggered (when `at` has a timestamp value) the delivery can no-longer be updated.**

#### HTTP Request

```
DELETE https://api.trychameleon.com/v3/edit/deliveries/:id
```

| param | -        | description                                                  |
| ----- | -------- | ------------------------------------------------------------ |
| `id`    | optional | The Chameleon ID of the Delivery                         |

