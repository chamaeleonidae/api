# Events

**Send Event data into Chameleon from services like Customer.io, Heap, Zapier or from you own backend.**

------

Events are processed asynchronously (typically within a few seconds).

## Create an event :id=events-create

#### HTTP Request

`POST` to `https://api.trychameleon.com/v3/observe/hooks/events` 

*or*

`POST` to `https://api.trychameleon.com/v3/observe/hooks/:account_secret/events`

| param | -        | description                                                  |
| ----- | -------- | ------------------------------------------------------------ |
| id    | optional | The Chameleon ID of the User Profile                         |
| uid   | optional | The User Profile Identifier (typically the Database ID from your backend) |
| name  | required | The name of the event ("Imported Data" or "Completed Task")  |

```json
{
  "uid": 18821,
  "name": "Scheduled follow up"
}
```

#### HTTP Response

```json
{
  "event": {
    "id": "5f3c4232c712de665632a2a3"
  }
}
```

## Normalized Event naming

By default, events are grouped by their case insensitive and normalized name value. The following are all counted as the _Same event_

- "Imported Leads" => `imported_leads`
- "ImporteD leads" => `imported_leads`
- "imported-leads" => `imported_leads`

To know more about how events are normalized, visit the [Normalization](http://concepts/normalization.md?id=events) page.
