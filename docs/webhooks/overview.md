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

| Topic                   | Example Payload                                                | Included models                                                                                                    | Description                                                                                                                                                                                                                                       |
|-------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ping`                  | [example](webhooks/overview.md?id=example-ping)                | Account                                                                                                            | Sent as a simple check to make sure the endpoint is working                                                                                                                                                                                       |
| `response.finished`     | [example](webhooks/overview.md?id=example-response-finished)   | [Response](apis/survey-responses.md), [Microsurvey](apis/surveys.md), [User Profile](apis/profiles.md)             | Sent when the Microsurvey is finished (all Steps completed; including text comment if configured)                                                                                                                                                 |
| `alert.triggered`       | [example](webhooks/overview.md?id=example-alert-triggered)     | [Alert Group](apis/alert_groups.md), [Experiences](concepts/experiences.md)                                        | Sent when an Alert is triggered by a violation of the alerting conditions                                                                                                                                                                         |
| `helpbar.answer`        | [example](webhooks/overview.md?id=example-helpbar-answer)      | Action, [User Profile](apis/profiles.md)                                                                           | Sent when a Search query generates an AI Answer in HelpBar                                                                                                                                                                                        |
| `helpbar.search`        | [example](webhooks/overview.md?id=example-helpbar-search)      | Action, [User Profile](apis/profiles.md)                                                                           | Sent when a Search query displays its results in the HelpBar                                                                                                                                                                                      |
| `helpbar.item.action`   | [example](webhooks/overview.md?id=example-helpbar-item-action) | Action, [User Profile](apis/profiles.md)                                                                           | Sent when an item in the HelpBar is clicked/actioned                                                                                                                                                                                              |
| `helpbar.item.error`    | [example](webhooks/overview.md?id=example-helpbar-item-error)  | Action, [User Profile](apis/profiles.md)                                                                           | Sent when an action from an item in the HelpBar throws an error when running                                                                                                                                                                      |
| `tour.started`          | [example](webhooks/overview.md?id=example-tour-all)            | [Tour](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                                     | Sent when the Tour is started; includes the first Step in the payload                                                                                                                                                                             |
| `tour.completed`        | [example](webhooks/overview.md?id=example-tour-all)            | [Tour](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                                     | Sent when the Tour is completed; includes the Step the user completed                                                                                                                                                                             |
| `tour.exited`           | [example](webhooks/overview.md?id=example-tour-all)            | [Tour](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                                     | Sent when the Tour is exited; includes the Step the user exited                                                                                                                                                                                   |
| `tour.snoozed`          | [example](webhooks/overview.md?id=example-tour-snooze)         | Action, [Tour](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                             | Sent when the Tour is exited on Step configured to snooze (re-display the Step at a later time).                                                                                                                                                  |
| `tour.button.clicked`   | [example](webhooks/overview.md?id=example-tour-button-clicked) | [Tour](apis/tours.md), [Step](apis/steps.md), [Button](apis/buttons.md), [User Profile](apis/profiles.md)          | Sent when the Tour is exited with the Step the user exited                                                                                                                                                                                        |
| `survey.started`        | [example](webhooks/overview.md?id=example-survey-all)          | [Microsurvey](apis/surveys.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                            | Sent when the Microsurvey is started with the first Step                                                                                                                                                                                          |
| `survey.completed`      | [example](webhooks/overview.md?id=example-survey-all)          | [Microsurvey](apis/surveys.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                            | Sent when the Microsurvey is completed with the Step the user completed                                                                                                                                                                           |
| `survey.exited`         | [example](webhooks/overview.md?id=example-survey-all)          | [Microsurvey](apis/surveys.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                            | Sent when the Microsurvey is exited with the Step the user exited                                                                                                                                                                                 |
| `survey.snoozed`        | [example](webhooks/overview.md?id=example-survey-snooze)       | Action, [Microsurvey](apis/surveys.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                    | Sent when the Tour is exited on Step configured to snooze (re-display the Step at a later time).                                                                                                                                                  |
| `survey.button.clicked` | [example](webhooks/overview.md?id=example-tour-button-clicked) | [Microsurvey](apis/surveys.md), [Step](apis/steps.md), [Button](apis/buttons.md), [User Profile](apis/profiles.md) | Sent when the Tour is exited with the Step the user exited                                                                                                                                                                                        |
| `embed.started`         | [example](webhooks/overview.md?id=example-embed-all)           | [Embed](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                                    | Sent when the Embed is started; includes the first Step in the payload                                                                                                                                                                            |
| `embed.completed`       | [example](webhooks/overview.md?id=example-embed-all)           | [Embed](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                                    | Sent when the Embed is completed; includes the Step the user completed                                                                                                                                                                            |
| `embed.exited`          | [example](webhooks/overview.md?id=example-embed-all)           | [Embed](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                                    | Sent when the Embed is exited; includes the Step the user exited                                                                                                                                                                                  |
| `embed.snoozed`         | [example](webhooks/overview.md?id=example-embed-snooze)        | Action, [Embed](apis/tours.md), [Step](apis/steps.md), [User Profile](apis/profiles.md)                            | Sent when the Embed is exited on Step configured to snooze (re-display the Step at a later time).                                                                                                                                                 |
| `embed.button.clicked`  | [example](webhooks/overview.md?id=example-tour-button-clicked) | [Embed](apis/tours.md), [Step](apis/steps.md), [Button](apis/buttons.md), [User Profile](apis/profiles.md)         | Sent when the Embed is exited with the Step the user exited                                                                                                                                                                                       |
| `demo.started`          | [example](webhooks/overview.md?id=example-demo-started)        | [Demo](apis/demos.md), [DemoRun](apis/demos.md?id=schema-demo-run), [User Profile](apis/profiles.md)               | Sent when the Demo is started                                                                                                                                                                                                                     |
| `demo.reveal`           | [example](webhooks/overview.md?id=example-demo-reveal)         | [Demo](apis/demos.md), [DemoRun](apis/demos.md?id=schema-demo-run), [User Profile](apis/profiles.md)               | Sent after the Demo is started _and_ [Clearbit reveal](https://app.chameleon.io/integrations/clearbit) is enabled _and_ a match is found. The `demo_run` will have `reveal_domain` and `reveal_name` keys for the Company domain and Company name |
| `demo.finished`         | [example](webhooks/overview.md?id=example-demo-finished)       | [Demo](apis/demos.md), [DemoRun](apis/demos.md?id=schema-demo-run), [User Profile](apis/profiles.md)               | Sent when the Demo is finished; Either the last step is reached **OR** when approximately 30 minutes has passed and the user likely bounced. The `demo_run` will have `finished_kind` of either `"last_step"` or `"timeout_30m"`.                 |
| `demo.form.submitted`   | [example](webhooks/overview.md?id=example-demo-form-submitted) | [Demo](apis/demos.md), [DemoRun](apis/demos.md?id=schema-demo-run), [User Profile](apis/profiles.md)               | Sent when a Demo form is submitted. The `action` will have the `submission` as a [DemoSubmission](apis/demos.md?id=schema-demo-submission) object. The final demo.finished webhook will contain all of the `actions` and `submissions`            |

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
  "id": "5f3c4232c712de665632d7a1",
  "kind": "response.finished",
  "sent_at": "2024-05-05T16:22:18.456Z",
  "data": {
    "profile": {
      "id": "5f3c4232c712de665632d7a2",
      "created_at": "2024-04-12T10:30:00.000Z",
      "updated_at": "2024-05-05T16:22:00.000Z",
      "uid": "feedback_user_888",
      "company_id": "5f3c4232c712de665632d7a3",
      "email": "rachel.green@designstudio.co",
      "browser_l": "fr-FR",
      "browser_n": "firefox",
      "browser_k": "desktop",
      "browser_x": 1680,
      "browser_tz": 1,
      "percent": 67.89,
      "last_seen_at": "2024-05-05T16:22:00.000Z",
      "last_seen_session_count": 24,
      "delivery_ids": [
        "5f3c4232c712de665632d7a4"
      ],
      "role": "ux_designer",
      "plan": "professional",
      "onboarding_completed": true,
      "feature_flags": ["design_tools", "collaboration_features"],
      "signup_source": "dribbble_ad",
      "team_size": 7,
      "subscription_status": "active",
      "department": "Design"
    },
    "response": {
      "id": "5f3c4232c712de665632d7a5",
      "created_at": "2024-05-05T16:22:18.000Z",
      "updated_at": "2024-05-05T16:22:18.234Z",
      "survey_id": "5f3c4232c712de665632d7a6",
      "profile_id": "5f3c4232c712de665632d7a2",
      "href": "https://app.example.com/dashboard/projects",
      "button_text": "Submit Feedback",
      "button_order": 0,
      "button_id": "5f3c4232c712de665632d7a7",
      "input_text": "The new design collaboration features are excellent! The real-time commenting system makes it so much easier to work with developers. Would love to see version history for design assets.",
      "finished_at": "2024-05-05T16:22:18.000Z",
      "rating": 5,
      "nps_score": 9
    },
    "survey": {
      "id": "5f3c4232c712de665632d7a6",
      "created_at": "2024-04-28T14:00:00.000Z",
      "updated_at": "2024-05-03T11:20:00.000Z",
      "name": "New Feature Feedback - Design Collaboration",
      "position": 8,
      "segment_ids": [
        "5f3c4232c712de665632d7a8",
        "5f3c4232c712de665632d7a9"
      ],
      "published_at": "2024-05-01T08:00:00.000Z",
      "rate_unlimit_at": null,
      "last_dropdown_items": [
        "Excellent",
        "Very Good",
        "Good",
        "Fair",
        "Poor"
      ],
      "kind": "survey",
      "stats": {
        "started_count": 134,
        "completed_count": 98,
        "response_rate": 0.731
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
  "id": "5f3c4232c712de665632c4d1",
  "kind": "helpbar.answer",
  "sent_at": "2024-04-28T13:45:22.567Z",
  "data": {
    "action": {
      "id": "5f3c4232c712de665632c4d2",
      "query": "How do I integrate with Slack?",
      "answer": "To integrate Chameleon with Slack, you can set up webhook notifications to send tour completions, survey responses, and other events directly to your Slack channels. First, create a Slack webhook URL in your Slack workspace settings, then configure it in your Chameleon dashboard under Integrations. You can customize which events trigger notifications and format the messages to include relevant user and experience data. This helps keep your team informed about user engagement in real-time.",
      "url": "https://app.example.com/helpbar",
      "results_count": 7,
      "references": [
        {
          "title": "Slack Integration Guide",
          "url": "https://help.example.com/integrations/slack"
        },
        {
          "title": "Webhook Configuration",
          "url": "https://help.example.com/webhooks/setup"
        }
      ]
    },
    "profile": {
      "id": "5f3c4232c712de665632c4d3",
      "created_at": "2024-03-20T12:30:00.000Z",
      "updated_at": "2024-04-28T13:44:00.000Z",
      "uid": "integration_user_999",
      "company_id": "5f3c4232c712de665632c4d4",
      "email": "david.kim@saas-company.com",
      "browser_l": "ko-KR",
      "browser_n": "chrome",
      "browser_k": "desktop",
      "browser_x": 1600,
      "browser_tz": 9,
      "percent": 44.67,
      "last_seen_at": "2024-04-28T13:44:00.000Z",
      "last_seen_session_count": 18,
      "delivery_ids": [
        "5f3c4232c712de665632c4d5",
        "5f3c4232c712de665632c4d6"
      ],
      "role": "integration_specialist",
      "plan": "enterprise",
      "onboarding_completed": true,
      "feature_flags": ["advanced_integrations", "custom_webhooks"],
      "signup_source": "partner_referral",
      "team_size": 50,
      "subscription_status": "active",
      "department": "Engineering"
    }
  }
}
```


##### Example: `helpbar.search` :id=example-helpbar-search

When a User searches for `"tell me about webhooks"` and 10 results were found.

```json
{
  "id": "5f3c4232c712de665632c5e1",
  "kind": "helpbar.search",
  "sent_at": "2024-04-30T09:20:15.432Z",
  "data": {
    "action": {
      "id": "5f3c4232c712de665632c5e2",
      "query": "export user data",
      "results_count": 5
    },
    "profile": {
      "id": "5f3c4232c712de665632c5e3",
      "created_at": "2024-04-25T14:15:00.000Z",
      "updated_at": "2024-04-30T09:19:00.000Z",
      "uid": "admin_user_111",
      "company_id": "5f3c4232c712de665632c5e4",
      "email": "emma.taylor@compliance-corp.org",
      "browser_l": "en-AU",
      "browser_n": "safari", 
      "browser_k": "desktop",
      "browser_x": 1440,
      "browser_tz": 10,
      "percent": 78.12,
      "last_seen_at": "2024-04-30T09:19:00.000Z",
      "last_seen_session_count": 6,
      "delivery_ids": [
        "5f3c4232c712de665632c5e5"
      ],
      "role": "compliance_officer",
      "plan": "enterprise",
      "onboarding_completed": true,
      "feature_flags": ["data_export", "compliance_tools", "audit_logging"],
      "signup_source": "enterprise_sales",
      "team_size": 8,
      "subscription_status": "active",
      "department": "Legal",
      "permissions": ["admin", "data_export", "user_management"]
    }
  }
}
```


##### Example: `helpbar.item.action` :id=example-helpbar-item-action

When a helpbar search result item is clicked (or actioned)

```json
{
  "id": "5f3c4232c712de665632c6f1",
  "kind": "helpbar.item.action",
  "sent_at": "2024-05-02T14:35:42.891Z",
  "data": {
    "action": {
      "id": "5f3c4232c712de665632c6f2",
      "query": "setup analytics tracking",
      "item_uid": "analytics-setup-guide-v2",
      "title": "Analytics Integration Setup Guide",
      "href": "https://help.example.com/analytics/setup-guide",
      "kinds": ["url", "tutorial"]
    },
    "profile": {
      "id": "5f3c4232c712de665632c6f3",
      "created_at": "2024-04-18T11:00:00.000Z",
      "updated_at": "2024-05-02T14:34:00.000Z",
      "uid": "analytics_user_777",
      "company_id": "5f3c4232c712de665632c6f4",
      "email": "priya.patel@datadriven.startup",
      "browser_l": "hi-IN",
      "browser_n": "chrome",
      "browser_k": "desktop",
      "browser_x": 1920,
      "browser_tz": 5.5,
      "percent": 33.44,
      "last_seen_at": "2024-05-02T14:34:00.000Z",
      "last_seen_session_count": 12,
      "delivery_ids": [
        "5f3c4232c712de665632c6f5",
        "5f3c4232c712de665632c6f6",
        "5f3c4232c712de665632c6f7"
      ],
      "role": "data_analyst",
      "plan": "growth",
      "onboarding_completed": true,
      "feature_flags": ["advanced_analytics", "custom_events", "cohort_analysis"],
      "signup_source": "content_marketing",
      "team_size": 15,
      "subscription_status": "active",
      "department": "Product",
      "time_zone": "Asia/Kolkata",
      "preferred_language": "en"
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

**Example: `tour.started`**
```json
{
  "id": "5f3c4232c712de665632a6d5",
  "kind": "tour.started",
  "sent_at": "2024-04-15T14:30:22.150Z",
  "data": {
    "action": {
      "id": "5f3c4232c712de665632a6d6"
    },
    "profile": {
      "id": "5f3c4232c712de665632a6d7",
      "created_at": "2024-03-10T09:15:00.000Z",
      "updated_at": "2024-04-15T14:25:00.000Z",
      "uid": "user_12345",
      "company_id": "5f3c4232c712de665632a6d8",
      "email": "sarah.johnson@techstartup.io",
      "browser_l": "en-US",
      "browser_n": "chrome",
      "browser_k": "desktop",
      "browser_x": 1920,
      "browser_tz": -8,
      "percent": 72.45,
      "last_seen_at": "2024-04-15T14:25:00.000Z",
      "last_seen_session_count": 15,
      "delivery_ids": [
        "5f3c4232c712de665632a6e1",
        "5f3c4232c712de665632a6e2"
      ],
      "role": "product_manager",
      "plan": "professional",
      "onboarding_completed": false,
      "feature_flags": ["new_dashboard", "analytics_beta"],
      "signup_source": "organic_search"
    },
    "tour": {
      "id": "5f3c4232c712de665632a6d9",
      "created_at": "2024-02-20T10:00:00.000Z",
      "updated_at": "2024-04-10T16:30:00.000Z",
      "name": "Dashboard Onboarding Tour",
      "position": 1,
      "segment_ids": [
        "5f3c4232c712de665632a6da"
      ],
      "published_at": "2024-04-01T08:00:00.000Z",
      "rate_unlimit_at": null,
      "kind": "tour",
      "style": "auto",
      "urls": {
        "dashboard": "https://app.chameleon.io/tours/5f3c4232c712de665632a6d9"
      },
      "stats": {
        "started_count": 1247,
        "completed_count": 892,
        "exited_count": 355
      }
    },
    "step": {
      "id": "5f3c4232c712de665632a6db",
      "created_at": "2024-02-20T10:00:00.000Z",
      "updated_at": "2024-04-10T16:30:00.000Z",
      "body": "Welcome to your new dashboard! Let's take a quick tour to help you get started with the key features.",
      "preset": "tooltip_bottom"
    }
  }
}
```

**Example: `tour.exited`**
```json
{
  "id": "5f3c4232c712de665632a2a1",
  "kind": "tour.exited",
  "sent_at": "2024-04-18T16:45:12.890Z",
  "data": {
    "action": {
      "id": "5f3c4232c712de665632a2a2"
    },
    "profile": {
      "id": "5f3c4232c712de665632a2a3",
      "created_at": "2024-01-15T11:30:00.000Z",
      "updated_at": "2024-04-18T16:44:00.000Z",
      "uid": "dev_user_789",
      "company_id": "5f3c4232c712de665632a2a4",
      "email": "mike.chen@enterprise-corp.com",
      "browser_l": "en-CA",
      "browser_n": "firefox",
      "browser_k": "desktop",
      "browser_x": 1440,
      "browser_tz": -5,
      "percent": 28.91,
      "last_seen_at": "2024-04-18T16:44:00.000Z",
      "last_seen_session_count": 45,
      "delivery_ids": [
        "5f3c4232c712de665632a2a5"
      ],
      "role": "developer",
      "plan": "enterprise",
      "onboarding_completed": true,
      "feature_flags": ["advanced_analytics", "api_access"],
      "signup_source": "referral",
      "team_size": 12
    },
    "tour": {
      "id": "5f3c4232c712de665632a2a6",
      "created_at": "2024-03-01T14:00:00.000Z",
      "updated_at": "2024-04-15T09:20:00.000Z",
      "name": "New Feature Announcement - API v2",
      "position": 3,
      "segment_ids": [
        "5f3c4232c712de665632a2a7",
        "5f3c4232c712de665632a2a8"
      ],
      "published_at": "2024-04-01T12:00:00.000Z",
      "rate_unlimit_at": "2024-05-01T00:00:00.000Z",
      "kind": "tour",
      "style": "manual",
      "tour_link_url": "https://app.example.com/tours/api-v2-announcement",
      "urls": {
        "dashboard": "https://app.chameleon.io/tours/5f3c4232c712de665632a2a6"
      },
      "stats": {
        "started_count": 324,
        "completed_count": 198,
        "exited_count": 126
      }
    },
    "step": {
      "id": "5f3c4232c712de665632a2a9",
      "created_at": "2024-03-01T14:00:00.000Z",
      "updated_at": "2024-04-15T09:20:00.000Z",
      "body": "🎉 Introducing API v2 with enhanced performance and new endpoints. Click here to explore the updated documentation.",
      "preset": "banner_top"
    }
  }
}
```

**Example: `tour.completed`**
```json
{
  "id": "5f3c4232c712de665632a3b1",
  "kind": "tour.completed",
  "sent_at": "2024-05-12T14:25:45.123Z",
  "data": {
    "action": {
      "id": "5f3c4232c712de665632a3b2"
    },
    "profile": {
      "id": "5f3c4232c712de665632a3b3",
      "created_at": "2024-05-10T11:15:00.000Z",
      "updated_at": "2024-05-12T14:25:00.000Z",
      "uid": "design_user_202",
      "company_id": "5f3c4232c712de665632a3b4",
      "email": "lisa.wang@creativestudio.design",
      "browser_l": "en-US",
      "browser_n": "chrome",
      "browser_k": "desktop",
      "browser_x": 1920,
      "browser_tz": -8,
      "percent": 56.78,
      "last_seen_at": "2024-05-12T14:25:00.000Z",
      "last_seen_session_count": 7,
      "delivery_ids": [
        "5f3c4232c712de665632a3b5",
        "5f3c4232c712de665632a3b6"
      ],
      "role": "senior_designer",
      "plan": "professional",
      "onboarding_completed": false,
      "feature_flags": ["theme_templates", "custom_styling", "design_library"],
      "signup_source": "behance_integration",
      "team_size": 6,
      "subscription_status": "active",
      "department": "Creative",
      "trial_converted": true
    },
    "tour": {
      "id": "5f3c4232c712de665632a3b7",
      "created_at": "2024-03-20T09:00:00.000Z",
      "updated_at": "2024-05-10T16:30:00.000Z",
      "name": "Theme Templates & Custom Styling Guide",
      "position": 4,
      "segment_ids": [],
      "published_at": "2024-04-15T12:00:00.000Z",
      "rate_unlimit_at": null,
      "kind": "tour",
      "style": "auto",
      "urls": {
        "dashboard": "https://app.chameleon.io/tours/5f3c4232c712de665632a3b7"
      },
      "stats": {
        "started_count": 89,
        "completed_count": 71,
        "exited_count": 18
      }
    },
    "step": {
      "id": "5f3c4232c712de665632a3b8",
      "created_at": "2024-03-20T09:00:00.000Z",
      "updated_at": "2024-05-10T16:30:00.000Z",
      "body": "🎨 You can also create your own Templates that follow the style of specific Themes!\n\n1. Create a new Experience as usual\n2. Pick the Theme you want to add a new Template to\n3. Adjust it in the Builder\n4. Use the **'Templatize'** option to save your new Template.",
      "preset": "tooltip_right"
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

**Example: `tour.button.clicked`**
```json
{
  "id": "5f3c4232c712de665632f9c1",
  "kind": "tour.button.clicked",
  "sent_at": "2024-05-15T11:40:18.456Z",
  "data": {
    "action": {
      "id": "5f3c4232c712de665632f9c2"
    },
    "profile": {
      "id": "5f3c4232c712de665632f9c3",
      "created_at": "2024-04-28T15:20:00.000Z",
      "updated_at": "2024-05-15T11:39:00.000Z",
      "uid": "content_user_444",
      "company_id": "5f3c4232c712de665632f9c4",
      "email": "maria.gonzalez@contentcorp.es",
      "browser_l": "es-MX",
      "browser_n": "safari",
      "browser_k": "desktop",
      "browser_x": 1440,
      "browser_tz": -6,
      "percent": 73.21,
      "last_seen_at": "2024-05-15T11:39:00.000Z",
      "last_seen_session_count": 16,
      "delivery_ids": [
        "5f3c4232c712de665632f9c5"
      ],
      "role": "content_manager",
      "plan": "growth",
      "onboarding_completed": true,
      "feature_flags": ["content_templates", "multilingual_support"],
      "signup_source": "linkedin_ad",
      "team_size": 12,
      "subscription_status": "active",
      "department": "Marketing",
      "preferred_language": "es"
    },
    "tour": {
      "id": "5f3c4232c712de665632f9c6",
      "created_at": "2024-04-22T14:00:00.000Z",
      "updated_at": "2024-05-12T10:30:00.000Z",
      "name": "Content Templates & Styling Guide",
      "position": 7,
      "segment_ids": [],
      "published_at": "2024-05-05T09:00:00.000Z",
      "rate_unlimit_at": null,
      "kind": "tour",
      "style": "auto",
      "urls": {
        "dashboard": "https://app.chameleon.io/tours/5f3c4232c712de665632f9c6"
      },
      "stats": {
        "started_count": 142,
        "completed_count": 108,
        "exited_count": 34
      }
    },
    "step": {
      "id": "5f3c4232c712de665632f9c7",
      "created_at": "2024-04-22T14:00:00.000Z",
      "updated_at": "2024-05-12T10:30:00.000Z",
      "body": "Explore the Templates Gallery and pick a specific Theme when saving new Templates on your account to leverage your style.",
      "preset": "tooltip_bottom"
    },
    "button": {
      "id": "5f3c4232c712de665632f9c8",
      "text": "Next",
      "style_color_fill": "2563EB",
      "style_color_text": "FFFFFF",
      "style_color_border": "2563EB",
      "style_button_roundness": "6px",
      "style_border_width": "1px",
      "action_new_window": false,
      "position": "bottom_right",
      "tour_action": "next",
      "order": 1
    }
  }
}
```

**Example: `survey.button.clicked`**
```json
{
  "id": "5f3c4232c712de665632e8b1",
  "kind": "survey.button.clicked",
  "sent_at": "2024-05-08T12:15:30.789Z",
  "data": {
    "action": {
      "id": "5f3c4232c712de665632e8b2"
    },
    "profile": {
      "id": "5f3c4232c712de665632e8b3",
      "created_at": "2024-05-01T09:45:00.000Z",
      "updated_at": "2024-05-08T12:14:00.000Z",
      "uid": "power_user_555",
      "company_id": "5f3c4232c712de665632e8b4",
      "email": "tom.harrison@productteam.io",
      "browser_l": "en-US",
      "browser_n": "chrome",
      "browser_k": "desktop",
      "browser_x": 2560,
      "browser_tz": -8,
      "percent": 89.34,
      "last_seen_at": "2024-05-08T12:14:00.000Z",
      "last_seen_session_count": 41,
      "delivery_ids": [
        "5f3c4232c712de665632e8b5",
        "5f3c4232c712de665632e8b6"
      ],
      "role": "product_owner",
      "plan": "enterprise",
      "onboarding_completed": true,
      "feature_flags": ["beta_features", "power_user_tools", "advanced_permissions"],
      "signup_source": "word_of_mouth",
      "team_size": 35,
      "subscription_status": "active",
      "department": "Product",
      "seniority": "senior"
    },
    "survey": {
      "id": "5f3c4232c712de665632e8b7",
      "created_at": "2024-05-05T13:00:00.000Z",
      "updated_at": "2024-05-07T16:45:00.000Z",
      "name": "Beta Feature Feedback - Advanced Workflows",
      "position": 15,
      "segment_ids": [
        "5f3c4232c712de665632e8b8"
      ],
      "published_at": "2024-05-06T10:00:00.000Z",
      "rate_unlimit_at": null,
      "last_dropdown_items": [
        "Extremely useful",
        "Very useful",
        "Somewhat useful",
        "Not very useful",
        "Not useful at all"
      ],
      "kind": "survey",
      "stats": {
        "started_count": 67,
        "completed_count": 52,
        "response_rate": 0.776
      }
    },
    "step": {
      "id": "5f3c4232c712de665632e8b9",
      "created_at": "2024-05-05T13:00:00.000Z",
      "updated_at": "2024-05-07T16:45:00.000Z",
      "body": "How useful do you find the new advanced workflow automation features?",
      "preset": "survey_rating"
    },
    "button": {
      "id": "5f3c4232c712de665632e8ba",
      "text": "Extremely useful",
      "style_color_fill": "4F46E5",
      "style_color_text": "FFFFFF",
      "style_color_border": "4F46E5",
      "style_button_roundness": "8px",
      "action_new_window": false,
      "position": "center",
      "tour_action": "next",
      "order": 0,
      "value": 5
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

**Example: `survey.started`**
```json
{
  "id": "5f3c4232c712de665632b1a1",
  "kind": "survey.started",
  "sent_at": "2024-04-20T10:15:30.245Z",
  "data": {
    "action": {
      "id": "5f3c4232c712de665632b1a2"
    },
    "profile": {
      "id": "5f3c4232c712de665632b1a3",
      "created_at": "2024-02-12T08:45:00.000Z",
      "updated_at": "2024-04-20T10:10:00.000Z",
      "uid": "marketing_user_456",
      "company_id": "5f3c4232c712de665632b1a4",
      "email": "alex.rivera@startup-inc.com",
      "browser_l": "es-ES",
      "browser_n": "safari",
      "browser_k": "mobile",
      "browser_x": 375,
      "browser_tz": 2,
      "percent": 64.33,
      "last_seen_at": "2024-04-20T10:10:00.000Z",
      "last_seen_session_count": 8,
      "delivery_ids": [
        "5f3c4232c712de665632b1a5",
        "5f3c4232c712de665632b1a6",
        "5f3c4232c712de665632b1a7"
      ],
      "role": "marketing_manager",
      "plan": "startup",
      "onboarding_completed": true,
      "feature_flags": ["mobile_optimization", "multilingual_support"],
      "signup_source": "product_hunt",
      "team_size": 4,
      "subscription_status": "trial"
    },
    "survey": {
      "id": "5f3c4232c712de665632b1a8",
      "created_at": "2024-03-15T12:00:00.000Z",
      "updated_at": "2024-04-18T14:30:00.000Z",
      "name": "Product Feedback - Mobile Experience",
      "position": 5,
      "segment_ids": [
        "5f3c4232c712de665632b1a9"
      ],
      "published_at": "2024-04-15T09:00:00.000Z",
      "rate_unlimit_at": null,
      "last_dropdown_items": [
        "Excellent",
        "Good", 
        "Fair",
        "Poor"
      ],
      "kind": "survey",
      "stats": {
        "started_count": 156,
        "completed_count": 98,
        "response_rate": 0.628
      }
    },
    "step": {
      "id": "5f3c4232c712de665632b1aa",
      "created_at": "2024-03-15T12:00:00.000Z",
      "updated_at": "2024-04-18T14:30:00.000Z",
      "body": "How would you rate your overall experience using our mobile app?",
      "preset": "survey_five"
    }
  }
}
```

**Example: `survey.completed`**
```json
{
  "id": "5f3c4232c712de665632b2b1",
  "kind": "survey.completed",
  "sent_at": "2024-04-22T15:25:45.678Z",
  "data": {
    "action": {
      "id": "5f3c4232c712de665632b2b2"
    },
    "profile": {
      "id": "5f3c4232c712de665632b2b3",
      "created_at": "2024-03-05T14:20:00.000Z",
      "updated_at": "2024-04-22T15:25:00.000Z",
      "uid": "support_user_321",
      "company_id": "5f3c4232c712de665632b2b4",
      "email": "jessica.wong@techsolutions.co",
      "browser_l": "zh-CN",
      "browser_n": "edge",
      "browser_k": "tablet",
      "browser_x": 768,
      "browser_tz": 8,
      "percent": 91.27,
      "last_seen_at": "2024-04-22T15:25:00.000Z",
      "last_seen_session_count": 32,
      "delivery_ids": [
        "5f3c4232c712de665632b2b5"
      ],
      "role": "customer_success",
      "plan": "business",
      "onboarding_completed": true,
      "feature_flags": ["asian_localization", "advanced_reporting"],
      "signup_source": "sales_demo",
      "team_size": 25,
      "subscription_status": "active",
      "last_login_at": "2024-04-22T08:00:00.000Z"
    },
    "survey": {
      "id": "5f3c4232c712de665632b2b6",
      "created_at": "2024-04-01T10:00:00.000Z",
      "updated_at": "2024-04-20T16:45:00.000Z",
      "name": "Customer Support Satisfaction Survey",
      "position": 12,
      "segment_ids": [
        "5f3c4232c712de665632b2b7",
        "5f3c4232c712de665632b2b8"
      ],
      "published_at": "2024-04-10T09:00:00.000Z",
      "rate_unlimit_at": "2024-05-10T00:00:00.000Z",
      "last_dropdown_items": [
        "Very Satisfied",
        "Satisfied",
        "Neutral",
        "Dissatisfied",
        "Very Dissatisfied"
      ],
      "kind": "survey",
      "stats": {
        "started_count": 89,
        "completed_count": 67,
        "response_rate": 0.753
      }
    },
    "step": {
      "id": "5f3c4232c712de665632b2b9",
      "created_at": "2024-04-01T10:00:00.000Z",
      "updated_at": "2024-04-20T16:45:00.000Z",
      "body": "Thank you for completing our survey! Your feedback helps us improve our service.",
      "preset": "thank_you"
    }
  }
}
```

**Example: `survey.exited`**
```json
{
  "id": "5f3c4232c712de665632b3c1",
  "kind": "survey.exited",
  "sent_at": "2024-04-25T11:30:18.234Z",
  "data": {
    "action": {
      "id": "5f3c4232c712de665632b3c2"
    },
    "profile": {
      "id": "5f3c4232c712de665632b3c3",
      "created_at": "2024-04-10T16:00:00.000Z",
      "updated_at": "2024-04-25T11:29:00.000Z",
      "uid": "trial_user_654",
      "company_id": "5f3c4232c712de665632b3c4",
      "email": "carlos.mendez@freelancer.dev",
      "browser_l": "pt-BR",
      "browser_n": "opera",
      "browser_k": "desktop",
      "browser_x": 1366,
      "browser_tz": -3,
      "percent": 15.88,
      "last_seen_at": "2024-04-25T11:29:00.000Z",
      "last_seen_session_count": 3,
      "delivery_ids": [],
      "role": "freelancer",
      "plan": "free",
      "onboarding_completed": false,
      "feature_flags": ["basic_features"],
      "signup_source": "google_ads",
      "team_size": 1,
      "subscription_status": "trial",
      "trial_ends_at": "2024-05-10T00:00:00.000Z",
      "utm_campaign": "latam_expansion",
      "integration_connected": false
    },
    "survey": {
      "id": "5f3c4232c712de665632b3c5",
      "created_at": "2024-04-20T13:00:00.000Z",
      "updated_at": "2024-04-24T10:15:00.000Z",
      "name": "Early User Feedback - Feature Requests",
      "position": 2,
      "segment_ids": [
        "5f3c4232c712de665632b3c6"
      ],
      "published_at": "2024-04-22T08:00:00.000Z",
      "rate_unlimit_at": null,
      "last_dropdown_items": [
        "Integrations",
        "Analytics",
        "Collaboration Tools",
        "API Access",
        "Other"
      ],
      "kind": "survey",
      "stats": {
        "started_count": 45,
        "completed_count": 12,
        "response_rate": 0.267
      }
    },
    "step": {
      "id": "5f3c4232c712de665632b3c7",
      "created_at": "2024-04-20T13:00:00.000Z",
      "updated_at": "2024-04-24T10:15:00.000Z",
      "body": "What feature would be most valuable for your workflow? Help us prioritize our roadmap!",
      "preset": "survey_multiple_choice"
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

Demos can also [sync Contact data](apis/demos.md?id=demos-in-the-crm) into the CRM

> For an anonymous user (e.g. on your marketing website) the `data.profile` will be `null` and `demo_run.anonymous_id` will be stable until local cache is cleared

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
3. `finished_kind` in the `demo_run` as either `"last_step"` or `"timeout_30m"` to give an indication of how this Demo was finished

It will be sent when the last step of the Demo is reached with `finished_kind=last_step` _OR_ approximately
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

1. [Clearbit Reveal](https://clearbit.com/) is configured in [your dashboard](https://app.chameleon.io/integrations/clearbit)
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
`action.submission` is a [DemoSubmission](apis/demos.md?id=schema-demo-submission)s with a `data` key of [DemoSubmissionData](apis/demos.md?id=schema-demo-submission-data) and
each data item has a `field` as [DemoFormField](apis/demos.md?id=schema-demo-form-field) and `value`.


```json
{
  "id": "6fb70330dcbc39000325a94b",
  "kind": "demo.form.submitted",
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


##### Example: `demo.email.added` :id=example-demo-email-added

This webhook topic is meant to capture the moment when previously taken anonymous Demos receive an email address.
The flow can be arbitrarily complex but typically follows one of these paths:

1. **Demos taken => Submits interest form**
   1. User takes 1 or more Demos on the marketing site, help documentation, etc.
   2. In one of the Demos, the User submits a form with their email
   3. Chameleon will then update all the previous [DemoRun](apis/demos.md?id=schema-demo-run)s from [1i] (e.g. those connected with the `anonymous_id`)
   4. Chameleon sends one `demo.email.added` webhook per updated [DemoRun](apis/demos.md?id=schema-demo-run)

2. **Demos taken => Product signup**
   1. User takes 1 or more Demos on the marketing site, help documentation, etc.
   2. User sign up for the product and is [identified](js/overview.md?id=examples) with their email address
   3. Chameleon will then update all the previous [DemoRun](apis/demos.md?id=schema-demo-run)s from [2i] (e.g. those connected with the `anonymous_id`)
   4. Chameleon sends one `demo.email.added` webhook per updated [DemoRun](apis/demos.md?id=schema-demo-run)

`action.email` will have email address as a copy of the email address now found in `demo_run.email`.

```json
{
  "id": "6fb70330dcbc39000325a94b",
  "kind": "demo.email.added",
  "sent_at": "2029-12-11T00:28:59.331Z",
  "data": {
    "action" : {
      "id": "6f885a88e7daf34f6000e3eb",
      "email": "jane@acme.co"
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

