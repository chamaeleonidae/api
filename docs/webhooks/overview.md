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


#### Normalization

- Property names are normalized to lower case and underscored i.e. `planName` => `plan_name`.
- See the full page on [Normalization](concepts/normalization.md?id=properties) for more information.

------------

## Data out of Chameleon [Coming soon] :id=outgoing-webhooks

> **Interested in the Outgoing Webhooks BETA program?? [Ping us here](mailto:hello@trychameleon.com?subject=API+Webhooks+beta)**

A webhook is an agreed-upon method of data exchange across a **secure channel**. Since you will be adding a new endpoint to your backend servers to handle this webhook, is it **strongly recommended** that you [verify the signature](?id=verification) of any webhook requests before processing any included data.

When sending a webhook to your backend Chameleon will:
 - Send a `POST` request to your `https` [configured endpoints](https://app.trychameleon.com/settings/webhooks).
 - Attempt delivery right away from `aws us-east`, use a request timeout of 7 seconds and include a `User-Agent` header specific to the [API version](concepts/authentication.md?id=version) the webhook is being sent from.
 - Generate a SHA256-HMAC signature of the request body and include the signature in the `X-Chameleon-Signature` header
 - In case of non-200 status code, will retry a total of 9 times over 43 hours (giving you a chance to fix errors without losing track of these webhooks)

When receiving a webhook from Chameleon you should:
 - Verify the Webhook request signature or responding a status `400` if the signature does not match
 - Drop the request if the webhook is too old (to prevent replay attacks). If the timestamp too old, respond with a status `400`
 - Respond quickly with a `200` status code (or any `2xx` status code)
 - Optional: Request any related data with the [other APIs](apis/overview.md)

#### Webhook topics :id=topics

| Topic | Included models | Description |
| --- | --- |--- |
| `ping` | Account | Sent as a simple check to make sure the endpoint is working |
| `survey.finished` | [Response](apis/survey-responses.md), [Microsurvey](apis/surveys.md), [User Profile](apis/profiles.md) | Sent when the Microsurvey is finished (all steps completed; including text comment if configured) |

> **Looking for a different topic? We're excited to chat about your use case! [Ping us here](mailto:hello@trychameleon.com?subject=API+Webhooks)**

#### Schema (request body) :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `sent_at` | timestamp | The current server time when this webhook was sent (used in [verification](?id=verification)) |
| `kind` | enum | The [topic identifier](?id=topics) |
| `data` | object | Contains the webhook payload data. This can be any models included by singular or plural name |

#### Request headers :id=headers

| Header | Example value | Description |
| --- | --- |--- |
| `X-Chameleon-Id` | `5f3c4232c712de665632a2a3` | The Chameleon ID of this webhook |
| `X-Chameleon-Signature` | 5a17b.... | The SHA256-HMAC of the raw request body |
| `User-Agent` | `Chameleon Webhooks/v3 (trychameleon.com; integral)` | The request is from the Chameleon v3 API (integral environment)|
| `Content-Type` | `application/json` | Signifying that the request body is JSON |
| `Accept` | `application/json` | Signifying that the response should be JSON (or nothing) |


## Verifying the Webhook :id=verification

The signature is the SHA256-HMAC of your [Webhook Secret](https://app.trychameleon.com/settings/webhooks) and the request body. To prevent replay attacks, reject the message if it is older than a few minutes (in the examples below 5 minutes is used)

#### Examples

###### Rails
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

**Have an example from your production app to add? Submit a [PR to this file](https://github.com/chamaeleonidae/api/blob/master/docs/webhooks/overview.md) and we'll give you $25 Amazon credit**
