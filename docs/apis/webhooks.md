# Webhooks

**This doc is all about how to manage your webhook subscriptions via API.**

> See the [Webhooks page](webhooks/overview.md) for information about the Webhooks that Chameleon sends to configured endpoints

> See the [configured Webhooks](https://app.chameleon.io/integrations/webhooks) in your dashboard.


## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `uid` | string | The webhook url to POST to |
| `name` | string | The identifiable name for this webhook |
| `last_item_at` | timestamp | Last time this webhook URL was POSTed to |
| `last_item_state` | string | Result of the last POST to the URL. One of `valid` or `error` |
| `last_item_error` | string | Description of the last non-2xx error code response |


## Listing Webhooks :id=webhooks-index

Retrieve a complete (un-paginated) list of webhooks.

#### HTTP Request

```
GET https://api.chameleon.io/v3/edit/webhooks
```

| param  | -        | description                                                  |
| ------ | -------- | ------------------------------------------------------------ |
| `kind`        | required | Use a values of either `webhook` or `zapier_hook`                     |


#### HTTP Response

```json
{
  "webhooks": [
    {
      "id": "5f3c4232c712de665632a6d9",
      "uid": "https://data.chameleon.io/where?is=it",
      "name": "Tour events to Data warehouse",
      "last_item_at": "2029-04-07T12:18:00Z",
      ...
    },
    {
      "id": "5f3c4232c712de665632a6e2",
      "uid": "https://hooks.other-system.com/N6bE1XGhTz5YbAQ?via=chameleon",
      "name": "Keep Other system up to date",
      ...
    },
    ...
  ]
}
```


## Create a Webhook :id=webhooks-create

Add a new Webhook endpoint (limited to 5 total)

#### HTTP Request

```
POST https://api.chameleon.io/v3/edit/webhooks
```

| param  | -        | description                                                  |
| ------ | -------- | ------------------------------------------------------------ |
| `kind`  | required | The type of webhook. One of `webhook` or `zapier_hook`. (defaults to `webhook`) |
| `url`  | required | A https-based URL where webhooks are to be sent              |
| `topics` | required | A comma-separated list OR Array of topics to send webhooks for. Any/all of the [Webhook topics](webhooks/overview.md?id=topics)             |
| `experience_id` | optional | A single Experience ID to send Webhooks for. An Experience is a Tour or Microsurvey |
| `experience_ids` | required | An array of Experience IDs to send Webhooks for. An Experience is a Tour or Microsurvey |


#### HTTP Response

```json
{
  "webhook": {
    "id": "5f3c4232c712de665632a6d9",
    "uid": "https://data.chameleon.io/where?is=it",
    ...
  }
}
```


## Delete a Webhook :id=webhooks-destroy

Remove a Webhook

#### HTTP Request

```
DELETE https://api.chameleon.io/v3/edit/webhooks/:id
```

| param  | -        | description                                                  |
| ------ | -------- | ------------------------------------------------------------ |
| `id`  | required | The Chameleon ID of the Webhook |


#### HTTP Response

```json
{
  "webhook": {
    "id": "5f3c4232c712de665632a6d9"
  }
}
```

