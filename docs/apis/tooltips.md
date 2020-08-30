# Tooltips

A Tooltip is a single step which can be shown when your end-users click or hover on either:
 - A specific element already present on the page (button, header, text field)
 - A Custom Icon tha Chameleon adds to the page (beta or new label etc.)

## Schema :id=schema


## List Tooltips :id=tooltips-index

#### HTTP Request
`GET` to `https://api.trychameleon.com/v3/edit/tooltips`

| param | - | description |
|---|---|---|
| limit | optional | Defaults to `50` with a maximum of `500` |
| before | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| before | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |

#### HTTP Response

```json
{
  "tooltips": [
    {
      "id": "5f3c4232c712de665632a6d5",
      "name": "When Search is disabled",
      "position": 4,
      "published_at": "2029-04-07T12:18:00Z",
       ...
    },
    {
      "id": "5f3c4232c712de665632a2a1",
      "name": "Admin Self-serve menu",
      "position": 2,
      "published_at": null,
       ...
    },
    ...
  ],
  "cursor": {
    "limit": 50,
    "before": "5f3c4232c712de665632a2a1"
  }
}
```

## Show a Tooltip :id=campaigns-show

Show a single Tooltip

#### HTTP Request

`GET` to `https://api.trychameleon.com/v3/edit/tooltips/:id`

| param | - | description |
|---|---|---|
| id | required | A Tooltip ID to lookup

```json
{
  "tooltip": {
    "id": "5f3c4232c712de665632a2a1",
    "name": "Admin Self-serve menu",
    "style": "auto",
    "position": 0,
    "published_at": "2029-04-07T12:38:00Z",
    ...
  }
}
```
