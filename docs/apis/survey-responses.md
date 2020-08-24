# Microsurvey Responses

A Response to a microsurvey is a single object with all of the information about the buttons clicked on the first step, the text input entered in the follow up step and the time that the survey was finished.



## Schema :id=schema

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


## List Microsurvey Responses :id=responses-index



## Delete a Microsurvey Response :id=responses-show

