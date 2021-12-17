# Listing Models

**The Chameleon API allows a generic retrieval and listing of data models.**

You may also be interested in these additional resources:

- [Authentication](concepts/authentication.md)
- [Errors](concepts/errors.md)
- [Pagination](concepts/pagination.md)


------



The currently supported models are:

| Model + details                                  | List URL                    | Show URL                        |
|--------------------------------------------------|-----------------------------|---------------------------------|
| [Segments](apis/segments.md)                     | `GET /v3/edit/segments`     | `GET /v3/edit/segments/:id`     |
| [Tours](apis/tours.md)                           | `GET /v3/edit/tours`        | `GET /v3/edit/tours/:id`        |
| [Microsurveys](apis/surveys.md)                  | `GET /v3/edit/surveys`      | `GET /v3/edit/surveys/:id`      |
| [Launchers](apis/launchers.md)                   | `GET /v3/edit/launchers`    | `GET /v3/edit/launchers/:id`    |
| [Tooltips](apis/tooltips.md)                     | `GET /v3/edit/tooltips`     | `GET /v3/edit/tooltips/:id`     |
| [Domains](apis/urls.md)                          | `GET /v3/edit/urls`         | `GET /v3/edit/urls/:id`         |
| [Experience Deliveries](apis/deliveries.md)      | `GET /v3/edit/deliveries`   | `GET /v3/edit/deliveries/:id`   |
| [Tags](apis/tags.md)                             | `GET /v3/edit/tags`         | `GET /v3/edit/tags/:id`         |
| [BETA - Rate Limit Groups](apis/limit-groups.md) | `GET /v3/edit/limit_groups` | `GET /v3/edit/limit_groups/:id` |
| [BETA - Alert Groups](apis/alert-groups.md)      | `GET /v3/edit/alert_groups` | `GET /v3/edit/alert_groups/:id` |
| [BETA - Imports](apis/imports.md)                | `GET /v3/edit/imports`      | `GET /v3/edit/imports/:id`      |



#### HTTP Responses

All the HTTP responses look the same, with a pluralized top-level key with the list of models.

```
{
  "segments": [
    {
      "id": "5f3c4232c712de665632a2a1",
      ...
    }
  ]
}

# OR

{
  "launchers": [
    {
      "id": "5f3c4232c712de665632a2a3",
      ...
    }
  ]
}
```



When retrieving a single item, its designation will be singular (`launchers` becomes `launcher`).

```
{
  "launcher": {
    "id": "5f3c4232c712de665632a2a3",
    ...
  }
}
```


> **Are we missing a model you need and care about?** [Contact us](https://app.trychameleon.com/help) to request a different one.

