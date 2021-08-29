# Overview

**Chameleon supports a robust data pipeline including receiving data from may different sources and sending Chameleon Experience data out to you connected destinations.**

---


## Data into Chameleon :id=incoming-webhooks

**These webhooks are a simple way to get data into Chameleon**.

Currently, our Incoming Webhooks API supports the following two advanced use cases:

 - To send data from your Backend into Chameleon for targeting with [Segments](apis/segments.md).
 - To send data directly from our Integration partners. Two examples are [Heap](https://heap.io?utm_source=Chameleon) and [Customer.io](https://customer.io?utm_source=Chameleon) which both have the robust omni-webhook functionality to send Data directly into Chameleon.


| Model + details                                              | URL                         |
| ------------------------------------------------------------ | --------------------------- |
| [User Profiles](webhooks/profiles.md) | `POST /v3/observe/hooks/:account_secret/profiles`  |
| [Companies](webhooks/companies.md)    | `POST /v3/observe/hooks/:account_secret/companies` |
| [Events](webhooks/events.md)          | `POST /v3/observe/hooks/:account_secret/events`    |


#### Integration partners
 - [Heap webhooks](https://help.trychameleon.com/en/articles/1349836-heap-integration-user-guide)
 - [Customer.io webhooks](https://help.trychameleon.com/en/articles/1349829-customer-io-integration-user-guide)


#### Limits

- Up to a total of 768 bytes are stored for each scalar value where each Array item and each Hash value can reach this limit.
- See the full page on [Limits](concepts/normalization.md?id=limits) for more information.
- Any data received that exceeds this limit will be truncated at the 768th byte and a warning surfaced on the data management page for [user data](https://app.trychameleon.com/data/properties/profile) or for [company data](https://app.trychameleon.com/data/properties/company).

#### Normalization

- Property names are normalized to lower case and underscored i.e. `planName` => `plan_name`.
- See the full page on [Normalization](concepts/normalization.md?id=properties) for more information.

------------

## Data out of Chameleon :id=outgoing-webhooks

A webhook is an agreed-upon method of data exchange across a **secure channel**. Since you will be adding a new endpoint to your backend servers to handle this webhook, is it **strongly recommended** that you [verify the signature](webhooks/overview.md?id=verification) of any webhook requests before processing any included data.

When sending a webhook to your backend Chameleon will:
 - Send a `POST` request to your `https` [configured endpoints](https://app.trychameleon.com/settings/integrations/webhooks).
 - Attempt delivery right away from `aws us-east`, use a request timeout of 7 seconds and include a `User-Agent` header specific to the [API version](concepts/authentication.md?id=version) the webhook is being sent from.
 - Generate a SHA256-HMAC signature of the request body and include the signature in the `X-Chameleon-Signature` header
 - In case of non-200 status code, will retry a total of 9 times over 43 hours (giving you a chance to fix errors without losing track of these webhooks)

When receiving a webhook from Chameleon you should:
 - Verify the Webhook request signature or responding a status `400` if the signature does not match
 - Drop the request if the webhook is too old (to prevent replay attacks). If the timestamp too old, respond with a status `400`
 - Respond quickly with a `200` status code (or any `2xx` status code)
 - Optional: Request any related data with the [other APIs](apis/overview.md)

#### Webhook topics :id=topics

| Topic | Example Payload | Included models | Description |
| --- | --- | --- |--- |
| `ping` | [example](webhooks/overview.md?id=example-ping) | Account | Sent as a simple check to make sure the endpoint is working |
| `response.finished` | [example](webhooks/overview.md?id=example-response-finished) | [Response](apis/survey-responses.md), [Microsurvey](apis/surveys.md), [User Profile](apis/profiles.md) | Sent when the Microsurvey is finished (all steps completed; including text comment if configured) |
| `tour.started` | [example](webhooks/overview.md?id=example-tour-all) | [Tour](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md) | Sent when the Tour is started with the first Step |
| `tour.completed` | [example](webhooks/overview.md?id=example-tour-all) | [Tour](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md) | Sent when the Tour is completed with the Step the user completed |
| `tour.exited` | [example](webhooks/overview.md?id=example-tour-all) | [Tour](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md) | Sent when the Tour is exited with the Step the user exited |
| `tour.snoozed` | [example](webhooks/overview.md?id=example-tour-snooze) | [Tour](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md) | Sent when the Tour is exited on Step configured to snooze (re-display the step at a later time). |
| `tour.button.clicked` | [example](webhooks/overview.md?id=example-tour-button-clicked) | [Tour](apis/tours.md), [Step](apis/steps.md), [Button](apis/buttons.md), [User Profile](apis/profiles.md) | Sent when the Tour is exited with the Step the user exited |

> **Looking for a different topic? We're excited to chat about your use case! [Ping us here](mailto:hello@trychameleon.com?subject=API+Webhooks)**

#### Schema (request body) :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `sent_at` | timestamp | The current server time when this webhook was sent (used in [verification](webhooks/overview.md?id=verification)) |
| `kind` | enum | The [topic identifier](webhooks/overview.md?id=topics) |
| `data` | object | Contains the webhook payload data. This can be any models included by singular or plural name |

#### Request headers :id=headers

| Header | Example value | Description |
| --- | --- |--- |
| `X-Chameleon-Id` | `5f3c4232c712de665632a2a3` | The Chameleon ID of this webhook |
| `X-Chameleon-Signature` | 5a17b.... | The SHA256-HMAC of the raw request body |
| `User-Agent` | `Chameleon Webhooks/v3 (trychameleon.com; integral)` | The request is from the Chameleon v3 API (integral environment)|
| `Content-Type` | `application/json` | Signifying that the request body is JSON |
| `Accept` | `application/json` | Signifying that the response should be JSON (or nothing) |


### Verifying the Webhook :id=verification

The signature is the SHA256-HMAC of your [Webhook Secret](https://app.trychameleon.com/settings/integrations/webhooks) and the request body. To prevent replay attacks, reject the message if it is older than a few minutes (in the examples below 5 minutes is used)

### Verification Examples

###### Rails :id=rails
 ```ruby
# Assumes this code runs in a Controller to access the `request` object
# Could easily be run in a background task or elsewhere by passing the `X-Chameleon-Signature` and `request.raw_post` exactly as-is

secret = ENV['CHAMELEON_VERIFICATION_SECRET']
received = request.headers['X-Chameleon-Signature']
expected = OpenSSL::HMAC.hexdigest('SHA256', secret, request.raw_post)

verified = received.size == expected.size &&
  ActiveSupport::SecurityUtils.fixed_length_secure_compare(received, expected) &&
  Time.zone.parse(params[:sent_at]) > 5.minutes.ago
```

**Have an example from your production app to add? Submit a [PR to this file](https://github.com/chamaeleonidae/api/blob/master/docs/webhooks/overview.md) and we'll give you $25 Amazon credit via our Docs Bounty program!**


### Payload Examples


##### Example: `ping` :id=example-ping

Typically do process Verification for this topic but nothing really to be done when topic is received. It's simply part of how Chameleon determines active/inactive/performance of webhook endpoints.

```json
{
  "id": "5fb70dcbc39330000325a817",
  "kind": "ping",
  "sent_at": "2029-12-11T00:28:59.650Z",
  "data": {
    "account": {
      "id": "58918bc07de121000432e9c0",
      "domain": "acme.co",
      "name": "Acme Corp"
    }
  }
}
```

##### Example: `response.finished` :id=example-response-finished

Every Microsruvey that is finished will send a webhook to this topic.

```json
{
  "id": "5fb70dcbc39330000325a81a",
  "kind": "response.finished",
  "sent_at": "2029-12-11T00:28:59.651Z",
  "data": {
    "profile": {
      "id": "5f885a88e7daf3000e3eb4f6",
      "email": "jane@example.com",
      "uid": "92340834",
      "name": "Jane E",
      "last_seen_at": "2029-12-11T00:21:59.109Z",
      "last_seen_session_count": 83,
      ...
    },
    "response": {
      "id": "5fb7afb5ea19724169374269",
      "survey_id": "5fb7936edee1f70011bfc4c9",
      "profile_id": "5f884e1e03d9f4000ebcbb59",
      "href": "https://app.acme.co/setup/tough-thing-to-do",
      "button_text": "Very Easy",
      "button_order": 0,
      "input_text": "I was able to figure it out quickly.",
      "finished_at": "2029-12-11T00:28:59.641Z"
    },
    "survey": {
      "id": "5fb7936edee1f70011bfc4c9",
      "name": "2029-11 Role question",
      "segment_id": "5f885a88e7daf3000e3eb4f7",
      "published_at": "2029-11-11T00:12:59.002Z",
      ...
      "steps": [
        {
          "id": "5fb7936d566535d75a87507c",
          "body": "How was that?",
          "preset": "survey_five",
          "dropdown_items": [
          ]
        },
        {
          "id": "5fb7936d566535d75a87507e",
          "body": "Thanks so much for your feedback! 🙏",
          "preset": "thank_you"
        }
      ],
      "user": {
        "id": "5490e42d65353700020030fa",
        "email": "jim@acme.co",
        "name": "Jim B"
      }
    }
  }
}
```


##### Example: `tour.started`, `tour.completed`, `tour.exited` :id=example-tour-all

A Tour is started, runs through a sequence of 1 or more Steps and finishes by being Exited or Completed. Tours by default show once to any one User but can, depending on their settings, show multiple times.

```json
{
  "id": "5fb70dcbc39330000325a818",
  "kind": "tour.started",
  "sent_at": "2029-12-11T00:28:59.652Z",
  "data": {
    "profile": {
      "id": "5f885a88e7daf3000e3eb4f6",
      "email": "jane@example.com",
      "uid": "92340834",
      "name": "Jon E",
      "last_seen_at": "2029-12-11T00:21:59.109Z",
      "last_seen_session_count": 83,
      ...
    },
    "tour": {
      "id": "5fb6e4ab8af58a00073f0d98",
      "name": "Usage upsell banner - A",
      "segment_id": "5f885a88e7daf3000e3eb4f7",
      "published_at": "2029-11-11T00:12:59.002Z",
      ...
    },
    "step": {
      "id": "5fb6e4ab8af58a00073f0d99",
       "body": "You've grown beyond your current plan by {{mau_blocks fallback='a lot'}}! 🎉 -- Next billing cycle, you will be charged for the additional users or pre-pay to save",
       ...
    },
    "action": {
      "id": "5f885a88e7daf3000e3eb4f6"
    }
  }
}
```

##### Example: `tour.snoozed` :id=example-tour-snooze

When a Tour is snoozed it is set to come back after a certain amount of time has passed (i.e. 1 day, 2 weeks, 2 hours etc.).

> **Look for `data.action` to be an object with the information on when this snooze ends, how many hours, and how many snoozes this totals.**

```json
{
  "id": "5fb70dcbc39330000325a818",
  "kind": "tour.started",
  "sent_at": "2029-12-11T00:28:59.652Z",
  "data": {
    "action": {
      "id": "5f885a88e7daf3000e3eb4f6",
      "deferred_until": "2029-12-14T00:28:58.622Z",
      "deferred_hours": 72,
      "deferred_count": 2
    },
    "profile": {
      "id": "5f885a88e7daf3000e3eb4f6",
      "email": "jane@example.com",
      "uid": "92340834",
      "name": "Jon E",
      "last_seen_at": "2029-12-11T00:21:59.109Z",
      "last_seen_session_count": 83,
      ...
    },
    "tour": {
      "id": "5fb6e4ab8af58a00073f0d98",
      "name": "Usage upsell banner - A",
      "segment_id": "5f885a88e7daf3000e3eb4f7",
      "published_at": "2029-11-11T00:12:59.002Z",
      ...
    },
    "step": {
      "id": "5fb6e4ab8af58a00073f0d99",
       "body": "You've grown beyond your current plan by {{mau_blocks fallback='a lot'}}! 🎉 -- Next billing cycle, you will be charged for the additional users or pre-pay to save",
       ...
    }
  },
}
```



##### Example: `tour.button.clicked` :id=example-tour-button-clicked

Every Button that is clicked in a Tour will send a webhook to this topic. It includes the Step and the Button configuration.

```json
{
  "id": "5fb70dcbc39330000325a819",
  "kind": "tour.button.clicked",
  "sent_at": "2029-12-11T00:28:59.653Z",
  "data": {
    "profile": {
      "id": "5f885a88e7daf3000e3eb4f6",
      "email": "jane@example.com",
      "uid": "92340834",
      "name": "Jon E",
      "last_seen_at": "2029-12-11T00:21:59.109Z",
      "last_seen_session_count": 83,
      ...
    },
    "tour": {
      "id": "5fb6e4ab8af58a00073f0d98",
      "name": "Usage upsell banner - A",
      "segment_id": "5f885a88e7daf3000e3eb4f7",
      "published_at": "2029-11-11T00:12:59.002Z",
      ...
    },
    "step": {
      "id": "5fb6e4ab8af58a00073f0d99",
       "body": "You've grown beyond your current plan by {{mau_blocks fallback='a lot'}}! 🎉 -- Next billing cycle, you will be charged for the additional users or pre-pay to save",
       ...
    },
    "button": {
      "id": "5fb6e4ab8af58a00073f0d9a",
       "text": "Check pricing",
       "tour_action": "next",
       "position": "bottom_right",
       ...
    },
    "action": {
      "id": "5f885a88e7daf3000e3eb4f6"
    }
  }
}
```
