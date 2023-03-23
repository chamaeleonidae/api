# Normalization

**Data in Chameleon is [normalized](concepts/normalization.md) for storage, to eliminate redundancy and data inconsistency and to ensure proper querying and analysis.**

---


## Properties, Events and Tags :id=all

- **User Property** names are normalized to their lower-cased and underscored versions.
- **Event Names** are normalized in the same way.
- **Tag Names** are normalized in the same way.
- This is done to provide the consistent application of API inputs and Segmentation outputs without runtime translations.

### User/Company Properties :id=properties

All of these examples will be stored internally as `user_role` and be called "User Role" in the UI.

- `user-role` => `user_role`
- `userRole` => `user_role`
- `UserRole` => `user_role`
- `user role` => `user_role`

### Event Names :id=events

All of these examples will be stored internally as `imported_leads` and be called "Imported Leads" in the UI.

- `imported leads` => `imported_leads`
- `Imported Leads` => `imported_leads`
- `ImportedLeads` => `imported_leads`
- `Imported leads` => `imported_leads`

### Tag Names :id=tags

All of these examples will be stored internally as `feature_announcements` and be called "Feature Announcements" in the UI.

- `Feature announcements` => `feature_announcements`
- `Feature Announcements!` => `feature_announcements`
- `feature-announcements` => `feature_announcements`

## Data and Data types

All of the data sent to Chameleon is cleaned before storage in the Database.
We translate JSON and/or String inputs into *real data* for the purpose of storage.

### Timestamps and Dates :id=timestamps

We try to recognize as many types of dates as possible to provide rich filtering based on date ranges.

- `"2029-08-21T02:46:46Z"` => `Tue, 21 Aug 2029 02:46:46 UTC +00:00`
- `"2029-08-21 02:46:46"` => `Tue, 21 Aug 2029 02:46:46 UTC +00:00`
- `"2029-08-21 02:46:46 +00:00"` => `Tue, 21 Aug 2029 02:46:46 UTC +00:00`
- `"2029-08-21"` => `Tue, 21 Aug 2029 00:00:00 UTC +00:00`
- `1881974806` => `Tue, 21 Aug 2029 02:46:46 UTC +00:00`
- `"1881974806"` => `Tue, 21 Aug 2029 02:46:46 UTC +00:00`
- `"$now"` => The current server time
- `"+30d"` => 30 days from the current server time

### Integers and floating point numbers

- `"12"` => `12`
- `"12.12"` => `12`
- `"11.9932e5"` => `1199320.0`
- `11.9932e5` => `1199320.0`

### Boolean

- `"true"` => `true`
- `"false"` => `false`

### Arrays and Hashes

- `["992", "2029-08-21T02:46:46Z","12.12"]` => `[992, Tue, 21 Aug 2029 02:46:46 UTC +00:00, 12.12]`
- `["992", null]` => `[992]`

- `{"when":"2029-08-21T02:46:46Z"}` => `{ when: Tue, 21 Aug 2029 02:46:46 UTC +00:00 }`
- `{"when":"2029-08-21T02:46:46Z","then":"443"}` => `{ when: Tue, 21 Aug 2029 02:46:46 UTC +00:00, then: 443 }`

### Arrays in hashes - supported

- `{"list_of_things":["thing1","12"]}` => `{ list_of_things: ["thing1",12]}`

### Hashes in Arrays - not supported

- `["992", {"list_of_things":["thing1","12"]}]` => `[992]`

## Limitations :id=limits

- Data received which is bigger than 768 bytes (characters) will be truncated and an alert will be set on the [Data management](https://app.chameleon.io/data/properties/profile) page.
- Each Array member as well as each Hash value can reach this limit.
- Nested object Hashes are acceptable as long as they are kept to 3 levels and aren't nested within array values.
- Any data that cannot be parsed or stored as a native data type is stored as a string.
