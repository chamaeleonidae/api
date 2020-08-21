# Surveys

## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `name` | string | The name given by an administrator of Chameleon |
| `position` | number | The order that these appear in lists (starting from 0) |
| `segment_id` | ID | The Chameleon ID of the configured segment |
| `published_at` | timestamp | The time this was most recently published |
| `rate_unlimit_at` | timestamp | This item is excluded from [Rate limiting](https://help.trychameleon.com/en/articles/3513345-rate-limiting-experiences) |
| `stats` | object | Aggregated statistics for this model (all-time) |
| `stats.started_count` | number | Number of your end-users who saw this |
| `stats.last_started_at` | timestamp | Most recent time any user saw this |
| `stats.completed_count` | number | Number of your end-users who completed/finished this |
| `stats.last_completed_at` | timestamp | Most recent time any user completed/finished this |
| `stats.exited_count` | number | Number of your end-users who dismissed/exited this |
| `stats.last_exited_at` | timestamp | Most recent time any user dismissed/exited this |

## Survey Response Schema :id=response-schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `href` | string | The current page URL when the Microsurvey was displayed |
| `button_text` | string | The text of the button when clicked |
| `button_order` | number | The 0-indexed index of the button |
| `button_id` | ID | The Chameleon ID of the button |
| `input_text` | string | Text comment left by the user (if configured) |
| `finished_at` | timestamp | When the last step of Microsurvey response was completed |


## List Microsurveys :id=campaigns-index

## Show a Microsurvey :id=campaigns-show

## List Microsurvey Responses :id=responses-index

## Delete a Microsurvey Response :id=responses-show
