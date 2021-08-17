# Deliveries

Deliveries are used to directly trigger an Experience to one specific User.

- In the simple case, on the next page-load, the linked Experience will be triggered with the given options.
- In the more complex case, a time window (`from` / `until`) can be applied.
- In the even more complex case filters such as `redirect` or `use_segmentation` can fine-tune the triggering.

An Experience that is delivered to the User will show immediately and with higher priority than any other Automatic Experiences.
Additionally, and Experience _may not_ show due to the conditions added to the Delivery itself. For example, when a Delivery uses
segmentation (`use_segmentation`) and the segmentation does not match the User at the time of the page load, the Experience
will not show and the Delivery is not attempted again. 

## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `model_id` | ID | The Chameleon ID of Experience this Delivery will trigger. |
| `model_kind` | string | The kind of Experience: One of `tour` or `survey` |
| `profile_id` | ID | The Chameleon ID of the [User Profile](apis/profiles.md?id=schema) |
| `idempotency_key` | string | A key that is used to enforce server-side "at most once delivery" for the given `profile_id`. [Learn more ↓](apis/deliveries.md?id=idempotency) |
| `options` | mixed | Any content to be used in the Experience, accessible via merge tag. |
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
 - When User Profile has too many pending Deliveries (`409`)
 - When the user has not been seen by Chameleon (`422`)
 - When the supplied dates (`from` and `until`) are out of order (`422`)
 - When the supplied dates (`from` and `until`) are not in compatible formats (`422`)


| Code  | description                                                  |
| ----- | ------------------------------------------------------------ |
| `404` | A related model cannot be found (Tour, Survey or Profile) |
| `409` | The experience is not live, please publish and retry |
| `409` | The Experience has already been triggered (it can no longer be subsequently changed) |
| `409` | Too many outstanding deliveries for this User Profile, use `delivery_ids_at_limit` with value of `drop` |
| `422` | The dates cannot be used in their given values (use `iso8601` or similar format) |
| `429` | Only one Delivery at a time can be created per User Profile |


### Limitations :id=limits

> **Once a Delivery is marked as triggered (when `at` has a timestamp value) the delivery can no-longer be updated.**

**Pending Deliveries** (yet untriggered; with a `null` value for the `at` property) are limited to 3 total per User Profile.
This limit can be changed in certain circumstances on our Growth plan by [contacting us](mailto:hello@trychameleon.com?subject=API+Delivery+limits).
A User Profile that already has 2 pending Deliveries requires a special parameter `delivery_ids_position` to instruct us where in
the list to add this new Delivery. Use values of `first`, `last` or an integer array index. To 

If an error occurs for a "limit reached", either specify `delivery_ids_at_limit` with value of `drop` or
first [list the Deliveries by User Profile](apis/deliveries.md?id=deliveries-index) to determine which ones to remove.


**Time based limits**: When using `from` and `until` the deliveries will be added to the list of pending deliveries and made
available to the client-side JavaScript but will remain undelivered until the `from` time is reached
or after the `until` time is been passed.


**Managing Delivery lifecycle**: When delivering for multiple use cases or when using different versions of `from` and `until` are used
you may need to implicitly manage the "current set of deliveries for a user". This can be done **_directly_** with the API for [Removing a Delivery ↓](apis/deliveries.md?id=deliveries-destroy)
OR **_indirectly_** with `delivery_ids_at_limit` and `delivery_ids_position`.


### Idempotency :id=idempotency

An idempotency key is appended to the `profile_id` thus scoping it to the specific user in question.

It is used to only generate a single delivery when the delivering criteria might otherwise be met **multiple times**. This is different than
the `once` parameter because the `idempotency_key` operates at the moment when the Delivery is being created, where the `once` is
used when attempting the Delivery on the client-side and only shows the Experience if it has **not been seen before**.

In terms of use cases:

- Create a Delivery when an Event is triggered (but only deliver the Experience once).
- Create a Delivery when an account needs to be upgraded to a new plan (but only deliver the Experience once).
- Create a Delivery when an account crosses a specific billing threshold (but only deliver the Experience once).
- Create a Delivery when you want feedback on a very specific action they took (but only delivery any of this type of feedback once).


###### Picking a good `idempotency_key`:

In many the use cases above simply repeat the `model_id` as the
`idempotency_key`. In other cases you may want to deliver one of many an in-product Microsurveys but only want the
"first one" to be shown to your end-user pick a "campaign specific" idempotency key
such as `"data-import-feedback-2029"` to only ask for one Microsurvey response for the campaign you're running to
get feedback on your hypothetical "data import flow".

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
      "profile_id": "5f3c4232c712de665632a6d6",
      "until": "2029-04-07T12:18:00Z",
      ...
    },
    {
      "model_kind": "tour",
      "model_id": "5f3c4232c712de665632a6d5",
      "profile_id": "5f3c4232c712de665632a6d7",
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
| `profile_id`       | optional* | The Chameleon ID of User Profile to target |
| `uid`              | optional* | The User Profile Identifier (typically the Database ID from your backend -- same value passed to `chmln.identify`) |
| `email`            | optional* | The email address of User Profile to target |
| `idempotency_key`  | optional | The key used to enforce server-side "at most once delivery" for the given user profile. |
| `options`          | optional | Any keys/values to be used in personalizing the Experience content (i.e. body text, button CTA url) |
| `from`             | optional | The timestamp before which this Delivery will not run - don't trigger this Experience before this time. |
| `until`            | optional | The timestamp after which this Delivery is no longer valid - don't trigger this Experience after this time. Default +infinity |
| `until`            | optional | The [time interval](concepts/normalization.md?id=timestamps) after which this Delivery is no longer valid (i.e. `"+30d"` => 30 days from now, `"+62d"` => 62 days from now) |
| `use_segmentation` | optional | Default `false`. Boolean value whether or not to first apply the Audience (Segmentation) to determine if the Experience show display to the user. |
| `once`             | optional | Default `false`. Boolean value whether or not to check if the user has seen this Experience before, `false` means for the Tour to display. |
| `redirect`         | optional | Default `false`. Boolean value whether or not to redirect to the "page the Experience starts on". This redirect loads the "Tour link" that can be copied from "Additional sharing options". |
| `skip_triggers`    | optional | Default `false`. Boolean value whether or not to bypass the triggers, elements and delays on the first step to "force" it to show right away. |
| `skip_url_match`   | optional | Default `false`. Boolean value whether or not to bypass the first step URL match to "force" it to show right away. |
| `delivery_ids_position` | optional | Defaults to `first`. The value of `last` or a specific integer array index to insert at, are accepted. |
| `delivery_ids_at_limit` | optional | Defaults to `error`. The value of `drop` is used to "pop" a delivery id off the end of the `delivery_ids` array after adding the current one. Note: when at the limit of pending deliveries, using `delivery_ids_position=last` + `delivery_ids_at_limit=drop` will cause an error. |

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

#### HTTP Response

| Status code        | -        | description    |
| ------------------ | -------- | -------------- |
| `201` | - | Delivery was created |
| `200` | - | idempotent Delivery already occurred |


```json
{
  "delivery": {
    "model_kind": "tour",
    "model_id": "5f3c4232c712de665632a6d5",
    "profile_id": "5f3c4232c712de665632a6d7",
    "from": "2029-02-03T00:00:00Z",
    "until": "2029-04-20T00:00:00Z",
    ...
  }
}
```

###### Request with data (in `options`) intended for **merge tags** in the Experience

```json
{
  "model_kind": "tour",
  "model_id": "5f3c4232c712de665632a6d5",
  "profile_id": "5f3c4232c712de665632a6d7",
  "options": {
    "title": "Upcoming changes to billing",
    "body": "Book a demo with your Account manager, Jessica to see our upcoming changes in action",
    "button1": {
      "text": "Book Demo",
      "url": "https://calendly.com/your-product/15min"
    },
    ...
  }
}
```

## Update a Delivery :id=deliveries-update

> **Once a Delivery is marked as triggered (when `at` has a timestamp value) the delivery can no-longer be updated.**

#### HTTP Request

```
PATCH https://api.trychameleon.com/v3/edit/deliveries/:id
```

| param | -        | description                                                  |
| ----- | -------- | ------------------------------------------------------------ |
| `id`    | optional | The Chameleon ID of the Delivery                         |
| *others | optional | Any other params from [Create a Delivery](apis/deliveries.md?id=deliveries-create)                         |


## Remove a Delivery :id=deliveries-destroy

Cancel a Delivery that has yet to happen

> **Once a Delivery is marked as triggered (when `at` has a timestamp value) the delivery can no-longer be deleted.**

#### HTTP Request

```
DELETE https://api.trychameleon.com/v3/edit/deliveries/:id
```

| param | -        | description                                                  |
| ----- | -------- | ------------------------------------------------------------ |
| `id`    | optional | The Chameleon ID of the Delivery                         |



---------


## Troubleshooting

Deliveries are used to directly trigger an Experience to one or to many users. On the next page-load, the linked Experience will be triggered with the given options.

While this is generally true there are a few different conditions that must be met for the trigger to occur:

 - The user never loads any page
 - The `from` time has not be reached
 - The `until` time has passed
 - The Experience is not live
 - `use_segmentation=true` and the Audience does not currently match
 - `once=false` and the user has seen the Experience before
 - `redirect=false` and the user never loads the matching URL
 - `skip_triggers=false` and the user never clicks/hovers on the configured Step triggers
 - `skip_url_match=false` and the user never loads the matching URL

