# Tooltips

**A Tooltip is a single step which can be shown when your end-users click or hover on either:**

- **A specific element already present on the page (button, header, text field).**
- **A Custom Icon that Chameleon adds to the page (beta or new label etc.)**



*To know more about Tooltips, feel free to visit our [product documentation](https://help.trychameleon.com/en/articles/2177293-how-to-add-a-tooltip)*.

------



With the Chameleon API for Tooltips, you can:

- List all the Tooltips that follow a specified set of parameters.

- Retrieve a single Tooltip based on the `id`.

  

## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `name` | string | The name given by an administrator of Chameleon |
| `position` | number | The order that these appear in lists (starting from 0) |
| `published_at` | timestamp | The time this was most recently published |


## List Tooltips :id=tooltips-index

List all the Tooltips that follow a specified set of parameters.

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/tooltips
```

| param  | -        | description                                                  |
| ------ | -------- | ------------------------------------------------------------ |
| limit  | optional | Defaults to `50` with a maximum of `500`                     |
| before | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| before | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |
| after  | optional | Read as "created `after`" and can be given as a timestamp or ID to get only `limit` items that were created after this time |

#### HTTP Response

```
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

## Retrieve a Tooltip :id=campaigns-show

Retrieve a single Tooltip

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/tooltips/:id
```

| param | -        | description            |
| ----- | -------- | ---------------------- |
| id    | required | A Tooltip ID to lookup |

```
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
