# Events (Incoming Webhook)

**Track Events to Chameleon from services like Customer.io, Heap, Zapier or from you own backend.** Looking for the [JavaScript API](js/events.md)?

------

> Events are processed asynchronously (typically within a few seconds).

## Create an Event :id=events-create

#### HTTP Request

```
POST https://api.chameleon.io/v3/observe/hooks/events
# OR
POST to https://api.chameleon.io/v3/observe/hooks/:account_secret/events
```

| param | -        | description                                                  |
| ----- | -------- | ------------------------------------------------------------ |
| `id`    | optional | The Chameleon ID of the User Profile                         |
| `uid`   | optional | The User Profile Identifier (typically the Database ID from your backend) |
| `name`  | required | The name of the Event ("Imported Data" or "Completed Task")  |

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

By default, Events are grouped by their case insensitive and normalized name value. The following are all counted as the _Same Event_

- "Imported Leads" => `imported_leads`
- "ImporteD leads" => `imported_leads`
- "imported-leads" => `imported_leads`

To know more about how Events are normalized, visit the [Normalization](concepts/normalization.md?id=events) page.
