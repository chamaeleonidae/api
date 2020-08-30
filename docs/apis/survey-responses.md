# Microsurvey Responses

A Response to a Microsurvey is a single object with all of the information about the buttons clicked on the first step, the text input entered in the follow up step and the time that the Microsurvey was finished.

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

#### HTTP Request
`GET` to `https://api.trychameleon.com/v3/analyze/responses`

| param | - | description |
|---|---|---|
| id | required | The Chameleon ID of the Microsurvey |
| limit | optional | Defaults to `50` with a maximum of `500` |
| before | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| before | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |
| expand | optional | Object that specifies relationships to include/exclude. |
| expand.profile | optional | use values of `all` or `none` control the properties present in the `profile`. Defaults to a minimal representation |

#### HTTP Response

```json
{
  "responses": [
    {
      "id": "5f3c4232c712de665632a6d5",
      "href": "https://app.example.com/starting/page/1",
      "button_text": "Yes please 👍",
      "button_order": 3,
      "input_text": "",
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

#### HTTP Request

`DELETE` to `https://api.trychameleon.com/v3/edit/responses/:id`

| param | - | description |
|---|---|---|
| id | required | A Response ID to remove

```json
{
  "response": {
    "id": "5f3c4232c712de665632a2a1",
  }
}
```
