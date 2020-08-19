# Events

Send Event data **into Chameleon** from services like Customer.io, Heap, Zapier or from you own backend

Events are processed asynchronously (typically within ~5 seconds).

#### HTTP Request
`POST` to `https://api.trychameleon.com/v3/observe/hooks/events`

| param | - | description |
|---|---|---|
| id | optional | The Chameleon ID of the User Profile |
| uid | optional | The User Profile Identifier (typically the Database ID from your backend) |
| name | required | The name of the event ("Imported Data" or "Completed Task") |

```json
{
  "uid": 18821,
  "name": "Scheduled follow up"
}
```

#### HTTP Response

```json
{
  "status": 200
}
```
