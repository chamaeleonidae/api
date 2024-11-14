# Product Demos

A Product Demo is recorded with the Chameleon Chrome extension as a way to show your product features to prospects, introduce
new features, explain complex workflows, and drive adoption/retention.

> [Demo Webhooks](webhooks/overview.md?id=topics) are also available for key moments in the life of a Demo


## Using Demos with your CRM :id=demos-in-the-crm

Chameleon can create new (and update existing) **Contact** and **Company** records in response to interactions with Demos.
Completions of, and Tags of Demos will be stored as properties; the data schema is [below](?id=schema-crm).


### Contacts

These are the moments when Chameleon will sync **Contact** data to your CRM:

1. When an anonymous user submits a form with their email address
2. When an [identified user](js/demos.md?id=mode-profile) with an email address starts a Demo

What will happen in the above situations?

1. A **Contact** is created or updated
2. `Chameleon Demos last seen time` is updated
3. The current Demo is added to `Chameleon Demos Seen` and the Tags (if any) are added to `Chameleon Demos Tags`
4. Any previous demos attached to the same `anonymous_id` will be added to the respective properties from [3]


### Companies

These are the moments when Chameleon will sync **Company** data to your CRM:

1. When [Clearbit reveal](https://app.chameleon.io/integrations/clearbit) is enabled, the Demo user has `consent_mode=granted` and a match is found

What will happen in the above situation?

1. A **Company** is created or updated



## Integrations :id=integrations

### Hubspot integration :id=hubspot

1. Visit the [Hubspot integration](https://app.chameleon.io/integrations/hubspot) page in the Chameleon dashboard
2. If you have not yet configured Hubspot, click "Connect" to initiate OAuth
3. Toggle on the "Create and Update objects in the CRM" option
4. Add an Email capture form or include a Product Demo in your product via another Chameleon experience


## CRM Schema :id=schema-crm

### Contacts

| Name                                       | Property                                   | Type             | Description                                                                                              |
|--------------------------------------------|--------------------------------------------|------------------|----------------------------------------------------------------------------------------------------------|
| `Chameleon Demos - All Demos Seen`         | `chameleon_demos_seen__profile_v1`         | Multiple select  | A multi-checkbox of the Chameleon Demos that this Contact has seen                                       |
| `Chameleon Demos - Last updated at`        | `chameleon_demos_last_updated__profile_v1` | Timestamp        | The last time any Demo/Tag was added to this Contact                                                     |
| `Chameleon Demos - Tags of All Demos Seen` | `chameleon_demos_tags__profile_v1`         | Multiple select  | A multi-checkbox of the Chameleon Tags that were attached to all of the Demos that this Contact has seen |


### Companies

| Name                                       | Property                                   | Type             | Description                                                                                                                   |
|--------------------------------------------|--------------------------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `Chameleon Demos - All Demos Seen`         | `chameleon_demos_seen__company_v1`         | Multiple select  | A multi-checkbox of the Chameleon Demos that all of the Contacts have collectively seen                                       |
| `Chameleon Demos - Last updated at`        | `chameleon_demos_last_updated__company_v1` | Timestamp        | The last time any Demo/Tag was added to this Company                                                                          |
| `Chameleon Demos - Tags of All Demos Seen` | `chameleon_demos_tags__company_v1`         | Multiple select  | A multi-checkbox of the Chameleon Tags that were attached to all of the Demos that all of the Contacts have collectively seen |




------



## `Demo` Schema :id=schema

| Property      | Type            | Description                                                          |
|---------------|-----------------|----------------------------------------------------------------------|
| `id`          | ID              | The Chameleon ID                                                     |
| `created_at`  | timestamp       | When this happened or when this was added to the Database            |
| `updated_at`  | timestamp       | The last time any property was updated                               |
| `name`        | string          | The name given by an administrator of Chameleon                      |
| `description` | string          | The display description                                              |
| `position`    | string          | The order that these appear in lists (starting from 0)               |
| `page_title`  | string          | The title of the page this Demo was recorded on                      |
| `tag_ids`     | array&lt;ID&gt; | The Chameleon IDs of the [Tags](apis/tags.md) attached to this model |


## `DemoRun` Schema :id=schema-demo-run

| Property        | Type                                                                   | Description                                                                                                                                       |
|-----------------|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`            | ID                                                                     | The Chameleon ID                                                                                                                                  |
| `created_at`    | timestamp                                                              | When this happened or when this was added to the Database                                                                                         |
| `updated_at`    | timestamp                                                              | The last time any property was updated                                                                                                            |
| `consent_mode`  | string                                                                 | One of `pending`, `denied`, or `granted`                                                                                                          |
| `referrer`      | string                                                                 | The referrer of the page this Demo is embedded into                                                                                               |
| `created_what`  | string                                                                 | The Browser name, version number and OS e.g. `Chrome 191.0 (Mac)`                                                                                 |
| `created_where` | string                                                                 | The city, region, country, country flag of the likely location of the user; _Only present for `consent_mode=granted`_. e.g. `Oakland CA, US 🇺🇸` |
| `actions`       | array&lt;[DemoSubmission](apis/demos.md?id=schema-demo-submission)&gt; | The city, region, country, country flag of the likely location of the user; _Only present for `consent_mode=granted`_. e.g. `Oakland CA, US 🇺🇸` |
| `submissions`   | string                                                                 | The city, region, country, country flag of the likely location of the user; _Only present for `consent_mode=granted`_. e.g. `Oakland CA, US 🇺🇸` |

Additional `DemoRun` Schema when [Clearbit Reveal](https://clearbit.com/)

1. Add your API Key in [your dashboard](https://app.chameleon.io/integrations/clearbit)
2. Ensure `consent_mode` of the Demo is set to `granted` (e.g. `data-consent-mode="granted"` on the iframe element for the embed)
3. Chameleon will try to find a match based on the IP address of anonymous traffic

| Property        | Type      | Description                                             |
|-----------------|-----------|---------------------------------------------------------|
| `clearbit_uid`  | string    | The ID of the matched company from Clearbit             |
| `reveal_domain` | string    | The Company domain of the matched company from Clearbit |
| `reveal_name`   | string    | The Company name of the matched company from Clearbit   |



## `DemoSubmission` Schema :id=schema-demo-submission

| Property     | Type                                                               | Description                                                             |
|--------------|--------------------------------------------------------------------|-------------------------------------------------------------------------|
| `id`         | ID                                                                 | The Chameleon ID                                                        |
| `created_at` | timestamp                                                          | When this happened or when this was added to the Database               |
| `updated_at` | timestamp                                                          | The last time any property was updated                                  |
| `step_id`    | string                                                             | The id of the DemoItem this submission came from                        |
| `action_id`  | string                                                             | The id of the item as found in [DemoRun](?id=schema-demo-run) `actions` |
| `data`       | array&lt;[DemoSubmissionData](?id=schema-demo-submission-data)&gt; |                                                                         |


## `DemoSubmissionData` Schema :id=schema-demo-submission-data

| Property     | Type                                                      | Description                                                                                                                |
|--------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `id`         | ID                                                        | The Chameleon ID                                                                                                           |
| `created_at` | timestamp                                                 | When this happened or when this was added to the Database                                                                  |
| `updated_at` | timestamp                                                 | The last time any property was updated                                                                                     |
| `field`      | object&lt;[DemoFormField](?id=schema-demo-form-field)&gt; |                                                                                                                            |
| `value`      | string/array/number/timestamp                             | The inputted value from the user as the real data type. Array for field `type=select`, timestamp for `datetime-local` etc. |


## `DemoFormField` Schema :id=schema-demo-form-field

| Property      | Type      | Description                                                                                                                                      |
|---------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`          | ID        | The Chameleon ID                                                                                                                                 |
| `created_at`  | timestamp | When this happened or when this was added to the Database                                                                                        |
| `updated_at`  | timestamp | The last time any property was updated                                                                                                           |
| `type`        | string    | The input/field type of this field. One of `text`, `email`, `select`, `checkbox`, `radio`, `datetime-local`, `number`, `tel`, `url`, or `button` |
| `name`        | string    | The display label of the field                                                                                                                   |
| `description` | string    | The display description of the field                                                                                                             |

