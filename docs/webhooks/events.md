# Events (Incoming Webhook)

**Track Events to Chameleon from services like Customer.io, Heap, Zapier or from you own backend.** Looking for the [JavaScript API](js/events.md)?

------

> Events are processed asynchronously (typically within thirty seconds).
> Events and their properties can be used for Segmentation, Goals, Launcher item completed etc.
> Events tracked for users that have not yet been seen by Chameleon will be created first and then the event tracked to them

## Create an Event :id=events-create

#### HTTP Request

```
POST https://api.chameleon.io/v3/observe/hooks/events
# OR
POST to https://api.chameleon.io/v3/observe/hooks/:account_secret/events
```

| param   | -        | description                                                               |
|---------|----------|---------------------------------------------------------------------------|
| `id`    | optional | The Chameleon ID of the User Profile                                      |
| `uid`   | optional | The User Profile Identifier (typically the Database ID from your backend) |
| `name`  | required | The name of the Event ("Imported Data" or "Completed Task")               |
| *others | optional | All other properties will be added to the Event                           |

```json
{
  "uid": 18821,
  "name": "Scheduled follow up",
  "scheduling_link": "https://acme.claendly.com/meetings/round-robin/15-min"
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

### Event properties

All other properties will be added to the Event and will be made available for creating [Custom Events](https://help.chameleon.io/en/articles/1226442-how-can-i-create-custom-events).

```json
{
  "uid": 18821,
  "name": "Scheduled follow up",
  "scheduling_type": "demo",
  "scheduling_source": "upsell",
  "scheduling_link": "https://acme.claendly.com/meetings/round-robin/15-min"
}
```


```json
{
  "uid": 18821,
  "name": "Payment succeeded",
  "plan": "Enterprise",
  "amount": "129500",
  "lifetime_value": "42905000",
}
```

## Normalized Event naming

By default, Events are grouped by their case insensitive and normalized name value. The following are all counted as the _Same Event_

- "Imported Leads" => `imported_leads`
- "ImporteD leads" => `imported_leads`
- "imported-leads" => `imported_leads`

To know more about how Events are normalized, visit the [Normalization](concepts/normalization.md?id=events) page.
