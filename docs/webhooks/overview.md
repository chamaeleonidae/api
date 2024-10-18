# Overview

**Chameleon supports a robust data pipeline including receiving data from many different sources and sending Chameleon Experience data out to your connected destinations.**

---


## Data into Chameleon :id=incoming-webhooks

**These webhooks are a simple way to get data into Chameleon**.

Currently, our Incoming Webhooks API supports the following two advanced use cases:

 - To send data from your Backend into Chameleon for targeting with [Segments](apis/segments.md).
 - To send data directly from our Integration partners. Some examples are [Heap](https://heap.io?utm_source=Chameleon) and [Customer.io](https://customer.io?utm_source=Chameleon) which both have the robust omni-webhook functionality to send Data directly into Chameleon.


| Model + details                       | URL                                                |
|---------------------------------------|----------------------------------------------------|
| [User Profiles](webhooks/profiles.md) | `POST /v3/observe/hooks/:account_secret/profiles`  |
| [Companies](webhooks/companies.md)    | `POST /v3/observe/hooks/:account_secret/companies` |
| [Events](webhooks/events.md)          | `POST /v3/observe/hooks/:account_secret/events`    |


#### Integration partners
 - [Heap webhooks](https://help.chameleon.io/en/articles/1349836-heap-integration-user-guide)
 - [Customer.io webhooks](https://help.chameleon.io/en/articles/1349829-customer-io-integration-user-guide)


#### Limits

- Up to a total of 768 bytes are stored for each scalar value where each Array item and each Hash value can reach this limit.
- See the full page on [Limits](concepts/normalization.md?id=limits) for more information.
- Any data received that exceeds this limit will be truncated at the 768th byte and a warning surfaced on the data management page for [user data](https://app.chameleon.io/data/properties/profile) or for [company data](https://app.chameleon.io/data/properties/company).

#### Normalization

- Property names are normalized to lower case and underscored i.e. `planName` => `plan_name`.
- See the full page on [Normalization](concepts/normalization.md?id=properties) for more information.

------------


## Data out of Chameleon :id=outgoing-webhooks

A webhook is an agreed-upon method of data exchange across a **secure channel**. Since you will be adding a new endpoint to your backend servers to handle this webhook, is it **strongly recommended** that you [verify the signature](webhooks/overview.md?id=verification) of any webhook requests before processing any included data.

When sending a webhook to your backend Chameleon will:
 - Send a `POST` request to your `https` [configured endpoints](https://app.chameleon.io/integrations/webhooks).
 - Attempt delivery right away from `aws us-east`, use a request timeout of 7 seconds and include a `User-Agent` header specific to the [API version](concepts/authentication.md?id=version) the webhook is being sent from.
 - Generate a SHA256-HMAC signature of the request body and include the signature in the `X-Chameleon-Signature` header
 - In case of non-200 status code, will retry a total of 9 times over 43 hours (giving you a chance to fix errors without losing track of these webhooks)

When receiving a webhook from Chameleon you should:
 - Only accept requests from [Chameleon IP Addresses](concepts/authentication.md?id=ip-addresses)
 - [Verify](webhooks/overview.md?id=verification) the Webhook request signature; respond with a status `400` if the signature does not match
 - Drop the request if the webhook is too old (to prevent replay attacks); respond with a status `400`
 - Respond quickly with a `200` status code (or any `2xx` status code)
 - Optional: Request any related data with the [other APIs](apis/overview.md)


#### Webhook topics :id=topics

| Topic                   | Example Payload                                                | Included models                                                                                                    | Description                                                                                                                                                                                                                            |
|-------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ping`                  | [example](webhooks/overview.md?id=example-ping)                | Account                                                                                                            | Sent as a simple check to make sure the endpoint is working                                                                                                                                                                            |
| `response.finished`     | [example](webhooks/overview.md?id=example-response-finished)   | [Response](apis/survey-responses.md), [Microsurvey](apis/surveys.md), [User Profile](apis/profiles.md)             | Sent when the Microsurvey is finished (all Steps completed; including text comment if configured)                                                                                                                                      |
| `alert.triggered`       | [example](webhooks/overview.md?id=example-alert-triggered)     | [Alert Group](apis/alert_groups.md), [Experiences](concepts/experiences.md)                                        | Sent when an Alert is triggered by a violation of the alerting conditions                                                                                                                                                              |
| `helpbar.answer`        | [example](webhooks/overview.md?id=example-helpbar-answer)      | Action, [User Profile](apis/profiles.md)                                                                           | Sent when a Search query generates an AI Answer in HelpBar                                                                                                                                                                             |
| `helpbar.search`        | [example](webhooks/overview.md?id=example-helpbar-search)      | Action, [User Profile](apis/profiles.md)                                                                           | Sent when a Search query displays its results in the HelpBar                                                                                                                                                                           |
| `helpbar.item.action`   | [example](webhooks/overview.md?id=example-helpbar-item-action) | Action, [User Profile](apis/profiles.md)                                                                           | Sent when an item in the HelpBar is clicked/actioned                                                                                                                                                                                   |
| `helpbar.item.error`    | [example](webhooks/overview.md?id=example-helpbar-item-error)  | Action, [User Profile](apis/profiles.md)                                                                           | Sent when an action from an item in the HelpBar throws an error when running                                                                                                                                                           |
| `tour.started`          | [example](webhooks/overview.md?id=example-tour-all)            | [Tour](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                                     | Sent when the Tour is started; includes the first Step in the payload                                                                                                                                                                  |
| `tour.completed`        | [example](webhooks/overview.md?id=example-tour-all)            | [Tour](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                                     | Sent when the Tour is completed; includes the Step the user completed                                                                                                                                                                  |
| `tour.exited`           | [example](webhooks/overview.md?id=example-tour-all)            | [Tour](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                                     | Sent when the Tour is exited; includes the Step the user exited                                                                                                                                                                        |
| `tour.snoozed`          | [example](webhooks/overview.md?id=example-tour-snooze)         | Action, [Tour](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                             | Sent when the Tour is exited on Step configured to snooze (re-display the Step at a later time).                                                                                                                                       |
| `tour.button.clicked`   | [example](webhooks/overview.md?id=example-tour-button-clicked) | [Tour](apis/tours.md), [Step](apis/steps.md), [Button](apis/buttons.md), [User Profile](apis/profiles.md)          | Sent when the Tour is exited with the Step the user exited                                                                                                                                                                             |
| `survey.started`        | [example](webhooks/overview.md?id=example-survey-all)          | [Microsurvey](apis/surveys.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                            | Sent when the Microsurvey is started with the first Step                                                                                                                                                                               |
| `survey.completed`      | [example](webhooks/overview.md?id=example-survey-all)          | [Microsurvey](apis/surveys.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                            | Sent when the Microsurvey is completed with the Step the user completed                                                                                                                                                                |
| `survey.exited`         | [example](webhooks/overview.md?id=example-survey-all)          | [Microsurvey](apis/surveys.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                            | Sent when the Microsurvey is exited with the Step the user exited                                                                                                                                                                      |
| `survey.snoozed`        | [example](webhooks/overview.md?id=example-survey-snooze)       | Action, [Microsurvey](apis/surveys.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                    | Sent when the Tour is exited on Step configured to snooze (re-display the Step at a later time).                                                                                                                                       |
| `survey.button.clicked` | [example](webhooks/overview.md?id=example-tour-button-clicked) | [Microsurvey](apis/surveys.md), [Step](apis/steps.md), [Button](apis/buttons.md), [User Profile](apis/profiles.md) | Sent when the Tour is exited with the Step the user exited                                                                                                                                                                             |
| `embed.started`         | [example](webhooks/overview.md?id=example-embed-all)           | [Embed](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                                    | Sent when the Embed is started; includes the first Step in the payload                                                                                                                                                                 |
| `embed.completed`       | [example](webhooks/overview.md?id=example-embed-all)           | [Embed](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                                    | Sent when the Embed is completed; includes the Step the user completed                                                                                                                                                                 |
| `embed.exited`          | [example](webhooks/overview.md?id=example-embed-all)           | [Embed](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                                    | Sent when the Embed is exited; includes the Step the user exited                                                                                                                                                                       |
| `embed.snoozed`         | [example](webhooks/overview.md?id=example-embed-snooze)        | Action, [Embed](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                            | Sent when the Embed is exited on Step configured to snooze (re-display the Step at a later time).                                                                                                                                      |
| `embed.button.clicked`  | [example](webhooks/overview.md?id=example-tour-button-clicked) | [Embed](apis/tours.md), [Step](apis/steps.md), [Button](apis/buttons.md), [User Profile](apis/profiles.md)         | Sent when the Embed is exited with the Step the user exited                                                                                                                                                                            |
| `demo.started`          | [example](webhooks/overview.md?id=example-demo-started)        | [Demo](apis/demos.md), [DemoRun](apis/demos.md?id=schema-demo-run), [User Profile](apis/profiles.md)               | Sent when the Demo is started                                                                                                                                                                                                          |
| `demo.reveal`           | [example](webhooks/overview.md?id=example-demo-reveal)         | [Demo](apis/demos.md), [DemoRun](apis/demos.md?id=schema-demo-run), [User Profile](apis/profiles.md)               | Sent after the Demo is started _and_ Clearbit reveal is enabled _and_ a match is found. The `demo_run` will have `reveal_domain` and `reveal_name` keys for the Company domain and Company name                                        |
| `demo.finished`         | [example](webhooks/overview.md?id=example-demo-finished)       | [Demo](apis/demos.md), [DemoRun](apis/demos.md?id=schema-demo-run), [User Profile](apis/profiles.md)               | Sent when the Demo is finished; Either the last step is reached **OR** when approximately 30 minutes has passed and the user likely bounced. The `demo_run` will have `finished_kind` of either `"last_step"` or `"timeout_30m"`.      |
| `demo.form.submitted`   | [example](webhooks/overview.md?id=example-demo-form-submitted) | [Demo](apis/demos.md), [DemoRun](apis/demos.md?id=schema-demo-run), [User Profile](apis/profiles.md)               | Sent when a Demo form is submitted. The `action` will have the `submission` as a [DemoSubmission](apis/demos.md?id=schema-demo-submission) object. The final demo.finished webhook will contain all of the `actions` and `submissions` |

> **Looking for a different topic? We're excited to chat about your use case! [Contact us](https://app.chameleon.io/help)**

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
| `User-Agent` | `Chameleon Webhooks/v3 (chameleon.io; integral)` | The request is from the Chameleon v3 API (integral environment)|
| `Content-Type` | `application/json` | Signifying that the request body is JSON |
| `Accept` | `application/json` | Signifying that the response should be JSON (or nothing) |


### Verifying the Webhook :id=verification

The signature is the SHA256-HMAC of your [Webhook Secret](https://app.chameleon.io/integrations/webhooks) and the request body.
As a second step, reject the message if it was sent outside of a few minutes (in the examples below 5 minutes is used; to prevent replay attacks)

### Verification Examples

###### Rails :id=rails
 ```ruby
# Assumes this code runs in a Controller to access the `request` object
# Could easily be run in a background task or elsewhere by passing the `X-Chameleon-Signature` and `request.raw_post` exactly as-is

secret = ENV['CHAMELEON_VERIFICATION_SECRET']
received = request.headers['X-Chameleon-Signature']
expected = OpenSSL::HMAC.hexdigest('SHA256', secret, request.raw_post)

verified = ActiveSupport::SecurityUtils.secure_compare(received, expected) &&
  (sent_at = Time.zone.parse(params[:sent_at])) &&
  (sent_at > 5.minutes.ago && sent_at < 5.minutes.from_now)
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

Every Microsurvey that is finished will send a webhook to this topic.

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

##### Example: `helpbar.answer` :id=example-helpbar-answer

This is the most important HelpBar webhook; it can directly inform your roadmap for additional updated/documentation.

- Chameleon AI Answering operates best when:
 - A headline (h2/h3) in the Help center article is relevant to the question being asked
 - Multiple inputs corroborate from different angles
- Seeing a `results_count` less than 3 is an important metric to track
- Use `references` to know where to make improvements


```json
{
  "id": "5eb7c393300000dcb381a25a",
  "kind": "helpbar.answer",
  "sent_at": "2029-12-11T00:28:59.651Z",
  "data": {
    "action": {
      "id": "5f885a88e7daf3000e3eb4f6",
      "query": "What is a widget?",
      "answer": "A widget is the generic name for the work product of a production run. One might use this term to describe something generic as an example in place of an unimportant specific item.",
      "results_count": 7,
      "references": ["https://help.your-product.com/hc/articles/925844-widgets-galore", "https://help.your-product.com/hc/articles/559284-widgets-n-more"],
      "url": "https://app.your-product.com/widgets/start"
    },
    "profile": {
      "id": "5f885a88e7daf3000e3eb4f6",
      "email": "jane@example.com",
      "uid": "92340834",
      "name": "Jane E",
      "last_seen_at": "2029-12-11T00:21:59.109Z",
      "last_seen_session_count": 83,
      ...
    }
  }
}
```


##### Example: `helpbar.search` :id=example-helpbar-search

When a User searches for `"data importing"` only 0 results were found. This indicates a gap in your Help center.

```json
{
  "id": "5eb7c393300000dcb381a25a",
  "kind": "helpbar.search",
  "sent_at": "2029-12-11T00:29:59.651Z",
  "data": {
    "action": {
      "id": "5f885a88e7daf3000e3eb4f7",
      "query": "data importing",
      "results_count": 2,
      "url": "https://app.your-product.com/widgets/import"
    },
    "profile": {
      "id": "5f885a88f30e7da00e3eb4f6",
      "email": "jane@example.com",
      "uid": "92340834",
      "name": "Jane E",
      "last_seen_at": "2029-12-11T00:21:59.109Z",
      "last_seen_session_count": 85,
      ...
    }
  }
}
```

When a User searches for `"widget categories"` only 7 results were found.

```json
{
  "id": "5eb7c393300000dcb381a25a",
  "kind": "helpbar.search",
  "sent_at": "2029-12-11T00:28:30.651Z",
  "data": {
    "action": {
      "id": "5f885a8af30008e7de3eb4f9",
      "query": "widget categories",
      "results_count": 7,
      "url": "https://app.your-product.com/widgets/import"
    },
    "profile": {
      "id": "5f885a88e7daf3000e3eb4f6",
      "email": "jane@example.com",
      "uid": "92340834",
      "name": "Jane E",
      "last_seen_at": "2029-12-11T00:21:59.109Z",
      "last_seen_session_count": 93,
      ...
    }
  }
}
```


##### Example: `helpbar.item.action` :id=example-helpbar-item-action

When a helpbar search result item is clicked (or actioned)

```json
{
  "id": "5eb7c393300000dcb381a25a",
  "kind": "helpbar.item.action",
  "sent_at": "2029-12-11T00:28:18.651Z",
  "data": {
    "action": {
      "id": "5f885a8af30008e7de3eb4f9",
      "item_uid": "data-onboarding",
      "href": "https://help.your-product.com/hc/articles/559284-data-onboarding",
      "kinds": ["url"]
    },
    "profile": {
      "id": "5f885a88e7daf3000e3eb4f6",
      "email": "jane@example.com",
      "uid": "92340834",
      "name": "Jane E",
      "last_seen_at": "2029-12-11T00:21:59.109Z",
      "last_seen_session_count": 93,
      ...
    }
  }
}
```

##### Example: `helpbar.item.error` :id=example-helpbar-item-error

When a helpbar search result item is clicked (or actioned) and then encounters an error processing the actions.

In the example below, the `script` item is not working properly and should be checked

```json
{
  "id": "5eb7c393300000dcb381a25a",
  "kind": "helpbar.item.action",
  "sent_at": "2029-12-11T00:28:18.651Z",
  "data": {
    "action": {
      "id": "5f885a8af30008e7de3eb4f9",
      "item_uid": "demo-upgrade",
      "href": "https://calendly.com/your-product/demo-upgrade-chat",
      "kinds": ["script", "calendly"]
    },
    "profile": {
      "id": "5f885a88e7daf3000e3eb4f6",
      "email": "jane@example.com",
      "uid": "92340834",
      "name": "Jane E",
      "last_seen_at": "2029-12-11T00:21:59.109Z",
      "last_seen_session_count": 93,
      ...
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
      "name": "Jane E",
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
  "kind": "tour.snoozed",
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
      "name": "Jane E",
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



##### Example: `tour.button.clicked` + `survey.button.clicked`  + `embed.button.clicked` :id=example-tour-button-clicked

Every Button that is clicked in a Tour / Microsurvey will send a webhook to this topic. It includes the Step and the Button configuration.

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
      "name": "Jane E",
      "last_seen_at": "2029-12-11T00:21:59.109Z",
      "last_seen_session_count": 83,
      ...
    },
    "tour": { // or "survey" or "embed"
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


##### Example: `embed.started`, `embed.completed`, `embed.exited` :id=example-embed-all

An Embed is started, runs through a sequence of 1 or more Steps and finishes by being Exited or Completed. Embeds by default show once to any one User but can, depending on their settings, show multiple times.

```json
{
  "id": "5fb70dcbc39330000325a818",
  "kind": "embed.started",
  "sent_at": "2029-12-11T00:28:59.652Z",
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
    "embed": {
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

##### Example: `embed.snoozed` :id=example-embed-snooze

When an Embed is snoozed it is set to come back after a certain amount of time has passed (i.e. 1 day, 2 weeks, 2 hours etc.).

> **Look for `data.action` to be an object with the information on when this snooze ends, how many hours, and how many snoozes this totals.**

```json
{
  "id": "5fb70dcbc39330000325a818",
  "kind": "embed.snoozed",
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
      "name": "Jane E",
      "last_seen_at": "2029-12-11T00:21:59.109Z",
      "last_seen_session_count": 83,
      ...
    },
    "embed": {
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



##### Example: `alert.triggered` :id=example-alert-triggered

When Experiences are in violation of the Alert conditions.
The primary use case for this is to notify the person in charge of the Experience when X days have passed without activity (on something that is otherwise expected to have activity).

> [Experiences](concepts/experiences.md) are either `kind=tour` for a [Tour](apis/tours.md) or `kind=survey` for a [Microsurvey](apis/surveys.md)

> For Tags and Environments see the `"tags"` and `"url_groups"` keys below and see [Experience](concepts/experiences.md) page.


```json
{
  "id": "6fd85a88e7daf3000e3eb4f7",
  "kind": "alert.triggered",
  "sent_at": "2029-12-12T01:28:59.654Z",
  "data": {
    "alert_group": {
      "id": "6de85a88e7daf3000e3eb4f6",
      "name": "Tour + Microsurvey 5-day dropoff",
      "summary": "Checks for Experiences that are not Seen in the past 5 days.",
      "interval": 5,
      "kind": "all",
      "style": "unseen",
      "created_user": {
        "id": "63165266260fe8000781b161",
        "email": "jon@example.com",
        ...
      },
      "urls": {
        "dashboard": "https://app.chameleon.io/alerts/6de85a88e7daf3000e3eb4f6"
      },
      ...
    },
    "experiences": [
      {
        "id": "6fd85a88e7daf3000e3eb4f8",
        "name": "Usage upsell banner - A",
        "kind": "tour",
        "segment_id": "6d885a88e7daf3000e3eb4f9",
        "published_at": "2029-11-06T00:12:59.002Z",
        ...
      },
      {
        "id": "6fd85a88e7daf3000e3eb4e8",
        "name": "Usage upsell banner - C",
        "kind": "tour",
        "segment_id": "6d885a88e7daf3000e3eb4f8",
        "published_at": "2029-11-11T00:12:59.002Z",
        "tags": [
          {
            "id": "6a885a880e3e4b8fe7daf300",
            "uid": "announcement",
            "name": "Feature announcement",
            "urls": {
              "dashboard": "https://app.chameleon.io/data/tags/6a885a880e3e4b8fe7daf300"
            },
            ...
          },
          ...
        ],
        "url_groups": [
          {
            "id": "6f885a88e7daf3000e3e4b8f",
            "name": "Production",
            "urls": {
              "dashboard": "https://app.chameleon.io/domains/6f885a88e7daf3000e3e4b8f"
            },
            ...
          }
        ],
        ...
      },
      {
        "id": "6fd85a88e7daf3000e3eb4e8",
        "name": "Request for research participants - 2029-11",
        "kind": "survey",
        "segment_id": "6d885a88e7daf3000e3eb4f8",
        "published_at": "2029-11-01T00:12:59.002Z",
        ...
      }
    ],
    "action": {
      "id": "5f885a88e7daf3000e3eb4f6",
      "summary": "3 Experiences went 5 days without being Seen."
    }
  }
}
```


##### Example: `survey.started`, `survey.completed`, `survey.exited` :id=example-survey-all


These three topics are considered lifecycle events and occur when the user is presented with or interacts with a Chameleon
Microsurvey. The `response.finished` Webhook is only sent when we consider the user **done** with the Microsurvey and will
no longer interact with it. A [Microsurvey Response](apis/survey-responses.md) is generated when the Survey Step + associated
Response Step are finished; it sends a `response.finished` Webhook.

A Microsurvey is started on the _Survey_ Step and either `completed` or `exited` when the first step is "actioned". It then automatically
branches through a sequence of optional _Response_ Steps and finishes with an optional _Thank You_ Step.

> The Steps corresponding to a _Response_ Step have `preset=response`; The _Thank You_ Steps have  `preset=thank_you`

 
```json
{
  "id": "5fb70dcbc39330000325a818",
  "kind": "survey.completed",
  "sent_at": "2029-12-11T00:28:59.652Z",
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
    "survey": {
      "id": "5fb7936edee1f70011bfc4c9",
      "name": "2029-11 Role question",
      "segment_id": "5f885a88e7daf3000e3eb4f7",
      "published_at": "2029-11-11T00:12:59.002Z",
      "steps": [
        {
          "id": "5fb7936d566535d75a87507c",
          "body": "How was that?",
          "preset": "survey_five",
          ...
        },
        {
          "id": "5fb7936d566535d75a87507d",
          "body": "Why specifically did you struggle?",
          "preset": "response",
          ...
        }
        ...
      ],
      ...
    },
    "step": {
      "id": "5fb7936d566535d75a87507c",
      "body": "How was that?",
      "preset": "survey_five",
       ...
    },
    "action": {
      "id": "5f885a88e7daf3000e3eb4f6"
    }
  }
}
```


##### Example: `survey.snoozed` :id=example-survey-snooze

When a Microsurvey is snoozed it is set to come back after a certain amount of time has passed (i.e. 1 day, 2 weeks, 2 hours etc.).

> **Look for `data.action` to be an object with the information on when this snooze ends, how many hours, and how many snoozes this totals.**

```json
{
  "id": "5fb70dcbc39330000325a818",
  "kind": "survey.snoozed",
  "sent_at": "2029-12-11T00:28:59.652Z",
  "data": {
    "action": {
      "id": "5f885a88e7daf3000e3eb4f6",
      "deferred_until": "2029-11-15T00:02:19.002Z",
      "deferred_hours": 48,
      "deferred_count": 2
    },
    "profile": {
      "id": "5f885a88e7daf3000e3eb4f6",
      "email": "jane@example.com",
      "uid": "92340834",
      "name": "Jane E",
      "last_seen_at": "2029-12-11T00:21:59.109Z",
      "last_seen_session_count": 83,
      ...
    },
    "survey": {
      "id": "5fb7936edee1f70011bfc4c9",
      "name": "2029-11 Role question",
      "segment_id": "5f885a88e7daf3000e3eb4f7",
      "published_at": "2029-11-11T00:12:59.002Z",
      "steps": [
        {
          "id": "5fb7936d566535d75a87507c",
          "body": "How was that?",
          "preset": "survey_five",
          ...
        },
        {
          "id": "5fb7936d566535d75a87507d",
          "body": "Why specifically did you struggle?",
          "preset": "response",
          ...
        }
        ...
      ],
      ...
    },
    "step": {
      "id": "5fb7936d566535d75a87507d",
      "body": "Why specifically did you struggle?",
      "preset": "response",
      ...
    }
  }
}
```


##### Example: `demo.started` :id=example-demo-started

Right when the Demo is first started in this session. Chameleon calls this a Demo "run".

> For an anonymous user (e.g. on your marketing website) the `data.profile` will be `null`

```json
{
  "id": "6fb70330dcbc39000325a94a",
  "kind": "demo.started",
  "sent_at": "2029-12-11T00:28:59.331Z",
  "data": {
    "action" : {
      "id": "6f885a88e7daf34f6000e3eb"
    },
    "profile": {
      "id": "5f885a88e7daf3000e3eb4f6",
      "email": "jane@example.com",
      "uid": "92340834",
      "name": "Jane E",
      "last_seen_at": "2029-12-11T00:21:59.109Z",
      "last_seen_session_count": 83,
      ...
    },
    "demo_run": {
      "id": "5fb7afb5ea19724169374269",
      "referrer":  "https://www.acme.co/products/analytics",
      "created_what":  "Chrome 191.0 (Mac)",
      "created_where": "Oakland CA, US 🇺🇸",
      "anonymous_id": "5fb7afb5ea19724169374269",
      "consent_mode": "granted",
      ...
    },
    "demo": {
      "id": "5fb7936edee1f70011bfc4c9",
      "name": "Demo of Analysis quickstart",
      "description": "Our analysis goes deeper than you'd typically see in a trial",
      "href": "https://app.acme.co/setup/tough-thing-to-do",
      "page_title": "Analytics",
      ...
      "user": {
        "id": "5490e42d65353700020030fa",
        "email": "jim@acme.co",
        "name": "Jim B"
      }
    }
  }
}
```


##### Example: `demo.finished` :id=example-demo-finished

This webhook topic only differs from `demo.started` by the addition of the following keys in the `demo_run`.

1. In the `demo_run`, an `actions` array of [DemoAction](apis/demos.md?id=schema-demo-action)s
2. In the `demo_run`, a `submissions` array of [DemoSubmission](apis/demos.md?id=schema-demo-submission)s with a `data` key of [DemoSubmissionData](apis/demos.md?id=schema-demo-submission-data)
3. `finished_kind` in the `demo_run` as either `"last_step"` or `"timeout_30m""` to give an indication of how this Demo was finished

It will be sent when the the last step of the Demo is reached with `finished_kind=last_step` _OR_ approximately
30 minutes after the last activity in the Demo and `finished_kind=timeout_30m`.

```json
{
  "id": "6fb70330dcbc39000325a94b",
  "kind": "demo.finished",
  "sent_at": "2029-12-11T00:28:59.331Z",
  "data": {
    "action" : {
      "id": "6f885a88e7daf34f6000e3eb"
    },
    "demo_run": {
      ...,
      "finished_kind": "last_step",
      "actions": [
        {
          "id": "",
          "name": "Demo Started",
          ...
        },
        {
          "id": "",
          "name": "Demo Step Started",
          ...
        },
        ...
      ],
      "submissions": [
        {
          "id": "6f885a84f600b0e38e7daf3e",
          "step_id": "5fb7936edee1f70011bfc4c9",
          "data": [
            {
              "field": {
                "id": "6fa88e7daf34f6000e3eb885",
                "type": "email",
                "name": "Email address",
                "description": ""
              },
              "value": "jane@example.io"
            },
            {
              "field": {
                "id": "6fa88e7daf34f6000e3eb885",
                "type": "select",
                "name": "Urgency",
                "description": "Knowing how quickly you want to evaluate Acme helps us mirror your urgency"
              },
              "value": "this week"
            },
            ...
          ]
        }
      ],
    },
    "demo": {
      "id": "5fb7936edee1f70011bfc4c9",
      ...
    }
  }
}
```



##### Example: `demo.reveal` :id=example-demo-reveal

This webhook topic only differs by the addition of `reveal_domain`, `reveal_name`, and `clearbit_uid` in the `demo_run`.
It will be sent when the following conditions are met

1. [Clearbit Reveal](https://clearbit.com/) in configured in [your dashboard](https://app.chameleon.io/integrations/clearbit)
2. The `consent_mode` of the Demo was set to `granted` (e.g. `data-consent-mode="granted"` on the iframe element for the embed)
3. A match is found to the IP address of anonymous traffic

```json
{
  "id": "6fb70330dcbc39000325a94b",
  "kind": "demo.reveal",
  "sent_at": "2029-12-11T00:28:59.331Z",
  "data": {
    "action" : {
      "id": "6f885a88e7daf34f6000e3eb"
    },
    "demo_run": {
      ...,
      "reveal_domain": "zenflex.io",
      "reveal_name": "Zen Flexing Aura Ltd.",
      "clearbit_uid": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
      "consent_mode": "granted"
    },
    "demo": {
      "id": "5fb7936edee1f70011bfc4c9",
      ...
    }
  }
}
```



##### Example: `demo.form.submitted` :id=example-demo-form-submitted

This webhook topic is meant to sync any form data to an external system; typically involving adding a new contact to your CRM. The
`action` will have a `submission` as a [DemoSubmission](apis/demos.md?id=schema-demo-submission)s with a `data` key of [DemoSubmissionData](apis/demos.md?id=schema-demo-submission-data) and
each data item has a `field` as [DemoFormField](apis/demos.md?id=schema-demo-form-field) and `value`.


```json
{
  "id": "6fb70330dcbc39000325a94b",
  "kind": "demo.finished",
  "sent_at": "2029-12-11T00:28:59.331Z",
  "data": {
    "action" : {
      "id": "6f885a88e7daf34f6000e3eb",
      "submission": {
        "id": "6f885a84f600b0e38e7daf3e",
        "step_id": "5fb7936edee1f70011bfc4c9",
        "data": [
          {
            "field": {
              "id": "6fa88e7daf34f6000e3eb885",
              "type": "email",
              "name": "Email address",
              "description": ""
            },
            "value": "jane@example.io"
          },
          {
            "field": {
              "id": "6fa88e7daf34f6000e3eb885",
              "type": "select",
              "name": "Urgency",
              "description": "Knowing how quickly you want to evaluate Acme helps us mirror your urgency"
            },
            "value": "this week"
          },
          ...
        }
      ],
    },
    "demo_run": {
      ...,
    },
    "demo": {
      "id": "5fb7936edee1f70011bfc4c9",
      ...
    }
  }
}
```

