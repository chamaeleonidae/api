# Buttons

Buttons are the configuration for a specific "call to action" on a Step. They can contain information about styling and about any actions that should be taken when clicked.

## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `text` | string | The call to action text for this button |
| `position` | string | The placement of this button: One of `bottom_left`, `bottom_center`, `bottom_right`, `center_right`, or `center_left` |
| `tour_action` | string | What does this [Tour](apis/tours.md) do when clicked: One of `next`, `previous`, or `exit` |
| `additional_action` | string | What else does this Button do when clicked: One of `cta`, `cta_url`, `any_click`, `code`, `element_click`, `hero_button`, `tour`, `survey`, or `exit` |
| `action_url` | string | With `additional_action=cta_url` this is the URL to load (action_new_window=tue opens this URL in a new `_blank` tab) |
| `action_new_window` | boolean | Should the `action_url` open in a new tab |
| `action_script` | string | With `additional_action=code` this is the JavaScript code snippet to evaluate |
| `action_element` | object | With `additional_action=element_click` this is the element targeted for clicking |
| `action_campaign_id` | ID | With `additional_action={tour,survey}` uses this attribute to determine which Tour or Microsurvey to link to |

