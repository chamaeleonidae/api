# Steps

Steps are he building blocks of Tours and Microsurveys

## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `body` | string | The configured body copy for this Step |
| `preset` | string | The template this step follows: One of `survey_two`, `survey_nps`, `survey_csat`, `survey_ces`, `response`, `thank_you`, `survey_three`, `survey_four`, `survey_five`, `survey_input`, or `survey_dropdown` |
| `dropdown_items` | array&lang;String&rang; | For a dropdown Microsurvey, the configured options for the dropdown |
| `quantifier_urls` | array | List of URL matching conditions that must match the current page URL |
| `quantifier_urls.url` | none | The specific URL used in this matching condition |
| `quantifier_urls.match_type` | none | The type of matching used. One of: `simple`, `exact`, `regex`, `inverse_simple`, or `inverse_exact` |

