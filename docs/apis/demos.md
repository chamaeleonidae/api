# Product Demos

A Product Demo is recorded with the Chameleon Chrome extension as a way to show your product features to prospects, introduce
new features, explain complex workflows, and drive adoption/retention.

[Demo Webhooks](webhooks/overview.md?id=topics) are available for key moments in the life of a Demo

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
| ``            | string          |                                                                      |


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

1. Add for API Key in [your dashboard](https://app.chameleon.io/integrations/clearbit)
2. Set `consent_mode` of the Demo was set to `granted` (e.g. `data-consent-mode="granted"` on the iframe element for the embed)
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

