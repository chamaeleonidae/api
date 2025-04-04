# Microsurvey Responses

**A Microsurvey response is a single object with all of the information about the microsurvey interactions: the buttons clicked on the first step, the text input entered in the follow-up step, and the time that the microsurvey was finished.**

------

Using Chameleon's API for Microsurvey responses, you can:

- List Microsurvey responses.
- Delete a Microsurvey response.


## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `survey_id` | ID | The Chameleon ID of the [Microsurvey](apis/surveys.md?id=schema) |
| `profile_id` | ID | The Chameleon ID of the [User Profile](apis/profiles.md?id=schema) |
| `href` | string | The current page URL when the Microsurvey was displayed |
| `button_text` | string | The text of the button when clicked |
| `button_order` | number | The 0-indexed index of the button |
| `button_id` | ID | The Chameleon ID of the button |
| `input_text` | string | Text comment left by the user (if configured) for Input Microsurveys 1st Step or Question 1 in the Follow Up Step |
| `comment_step_input_text2` | string | Text comment left by the user (if configured) for Question 2 in the Follow Up Step |
| `dropdown_items` | string | For a dropdown Microsurvey, the selected options from the dropdown on the 1st Step |
| `other_text` | string | For a dropdown Microsurvey, the alternative text comment left by the user (if configured) |
| `comment_step_dropdown_items` | string | For any kind of Microsurvey, the selected options from the Follow Up Step dropdown in Question 1 |
| `comment_step_other_text` | string | For any kind of Microsurvey, the alternative text comment left by the user as the dropdown answer (if configured) in Question 1 |
| `comment_step_dropdown_items2` | string | For any kind of Microsurvey, the selected options from the Follow Up Step dropdown in Question 2 |
| `comment_step_other_text2` | string | For any kind of Microsurvey, the alternative text comment left by the user as the dropdown answer (if configured) in Question 2 |
| `comment_step_buttons_selected` | string | For any kind of Microsurvey, the selected option(s) from the Follow Up Step buttons in Question 1 |
| `comment_step_buttons_selected2` | string | For any kind of Microsurvey, the selected option(s) from the Follow Up Step buttons in Question 2 |
| `finished_at` | timestamp | When the last step of Microsurvey response was completed |
| `profile` | object | An expandable [Profile](apis/profiles.md) model |
| `profile.company` | none | An expandable [Company](apis/companies.md) model embedded in the profile |

## List Microsurvey Responses :id=responses-index

#### HTTP Request

```
GET https://api.chameleon.io/v3/analyze/responses
```

| param          | -        | description                                                  |
| -------------- | -------- | ------------------------------------------------------------ |
| `id`             | required | The Chameleon ID of the Microsurvey                          |
| `limit`          | optional | Defaults to `50` with a maximum of `500`                     |
| `before`         | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| `before`         | optional | Read as "created `before`" and can be given as a timestamp or ID to get only `limit` items that were created before this time |
| `after`          | optional | Read as "created `after`" and can be given as a timestamp or ID to get only `limit` items that were created after this time |
| `order`          | optional | One of `created_at` or `updated_at`. Defaults to `created_at` (the ID encodes this information). |
| `expand`         | optional | Object that specifies relationships to include/exclude. Supported keys are `profile` and `company`      |
| `expand.profile` | optional | use values of `all`, `min` or `skip` to control the properties present in the `profile`. Defaults to `min` |
| `expand.company` | optional | use values of `all`, `min` or `skip` to control the properties present in the `company`. Defaults to `min` |

#### Using the `expand` parameter

```
# As a URL parameter
expand[profile]=all&expand[company]=skip

# In the Reqeust body
{"expand":{"profile":"all","company":"skip"}}
```

Notes:
- A `profile` key will always be present with an object value. The `company` (embedded within `profile`) will be missing when the User Profile is not attached to a Company, otherwise it will be an object.
- The combination of `before` and `after` can be used to limit pagination to "stop" at your most recently cached Survey Response (send the max ID from your last import as the `after` parameter).


#### HTTP Response

```json
{
  "responses": [
    {
      "id": "5f3c4232c712de665632a6d5",
      "href": "https://app.example.com/starting/page/1",
      "button_text": "Yes please 👍",
      "button_order": 3,
      "input_text": "I saw...",
      "finished_at": "2029-04-07T12:18:00Z",
      "profile": {
        "id": "5f3c4232c712de665632a6d5",
        "uid": "55232",
        ...
      },
      ...
    },
    {
      "id": "5f3c4232c712de665632a2a3",
      "href": "https://app.example.com/starting/page/2",
      "button_text": "No thanks 👎",
      "button_order": 2,
      "input_text": "I would have liked to see...",
      "finished_at": "2029-04-07T12:18:00Z",
      "profile": {
        "id": "5f3c4232c712de665632a6d6",
        "uid": "55125",
        "company": {
          "id": "5f3c4232c712de665632a6d7",
          "uid": "3321",
        },
        ...
      },
      ...
    },
    ...
  ],
  "cursor": {
    "limit": 50,
    "before": "5f3c4232c712de665632a2a3"
  }
}
```

## Delete a Microsurvey Response :id=responses-destroy

Deleting a Microsurvey response also clears the associated metrics and summaries

#### HTTP Request

```
DELETE https://api.chameleon.io/v3/edit/responses/:id
```

| param | -        | description             |
| ----- | -------- | ----------------------- |
| `id`    | required | A Response ID to remove |

```json
{
  "response": {
    "id": "5f3c4232c712de665632a2a1",
  }
}
```
