# Companies

**Companies represent your *accounts*: real customers who were identified to Chameleon. They can store complex (semi-arbitrary) properties.**

---

## Schema :id=schema

#### Fully-expanded company when listed directly or embedded with `expand` param specified properly

| Property                  | Type      | Description                                                  |
| ------------------------- | --------- | ------------------------------------------------------------ |
| `id`                      | ID        | The Chameleon ID                                             |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `uid`                     | string    | The external ID that came from your backend system           |
| `*any options`            | mixed     | Any other options you have sent as Custom Properties will show up here too |

#### Non-expanded company when embedded in another (i.e. Microsurvey response)

| Property     | Type      | Description                                               |
| ------------ | --------- | --------------------------------------------------------- |
| `id`         | ID        | The Chameleon ID                                          |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `uid`        | string    | The external ID that came from your backend system        |


## List Companies :id=companies-index

[Coming soon] List all Companies based on the specified set of parameters.


## Retrieve a specific Company

[Coming soon] Get a specific Company based on the Chameleon ID or the external UID.
