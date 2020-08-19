# Incoming Webooks: User Profiles

Send User Profile data **into Chameleon** from services like Customer.io, Heap, Zapier or from you own backend

Profile data updates are processed synchronously on the application server

#### HTTP Request
`POST` to `https://api.trychameleon.com/v3/observe/hooks/profiles`

| param | - | description |
|---|---|---|
| id | optional | The Chameleon ID of the User Profile |
| uid | optional | The User Profile Identifier (typically the Database ID from your backend) |
| *others | optional | All other properties will be stored on the Profile |

```json
{
  "uid": 18821,
  "email": "leon@chmln.co",
  "first_name": "Leon",
  "role": "admin",
  "last_import_at": "2029-04-07T12:18:00Z",
   ...
}
```

#### HTTP Response

```json
{
  "status": 200
}
```

#### Limits <!-- Make sure to change this elsewhere too -->

- Up to a total of 512 characters are stored for each value. Data received longer than 512 will be truncated and an alert will be set on the [Data management](https://app.trychameleon.com/data/properties/profile) page.
- Nested object are acceptable as long as they are kept to 3 levels and aren't nested within array values
